import pygame
import sys

from player import Player, PLAYER_SIZE_INACTIVE
from wheel import Wheel
from game_view import GameView
from game_adapter import load_fields

# Spiel-Parameter
WHEEL_RADIUS = 110  # Größe des Rades
WHEEL_POSITION = (1030, 380)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

statussymbols = [["Rolls Royce", "Millionärs-Einkommen aus Vermietung ", 1000],
                 ["Villa in Südfrankreich", "Millionärs-Einkommen aus Vermietung ", 2000],
                 ["Kunstsammlung", "Millionärs-Einkommen aus Ausstellungen ", 3000],
                 ["Rennpferde", "Millionärs-Einkommen aus Geldpreisen ", 3000],
                 ["Luxus-Yacht", "Millionärs-Einkommen aus Charteraufträgen ", 4000],
                 ["Privat-Jet", "Millionärs-Einkommen aus Charterflügen ", 4000]]
actioncards = [["Verpflichtungs-Karte", "Der Inhaber dieser Karte kann von einem Mitspieler seiner Wahl verlangen, "
                                        "die Hälfte des Betrages, den er bezahlen muss, mitzutragen, sofern dieser "
                                        "über 6.000 liegt.", 6000],
               ["Befreiungs-Karte", "Der Inhaber dieser Karte ist berechtigt, Zahlungen aufgrund der "
                                    "Berechtigungskarte oder Verpflichtungskarte eines Mitspielers zu verweigern.", 0],
               ["Berechtigungskarte", "Der Inhaber dieser Karte ist berechtigt, von einem Mitspieler seiner Wahl die "
                                      "Hälfte eines Gewinnes zu verlangen, sofern dieser Gewinn über 10.000 beträgt.",
                10000]]  # TODO Button auf spieler rect um anderem spieler aktion zu ermöglichen


STATUSSYMBOLS = []
for symbol in statussymbols:
    STATUSSYMBOLS.append({"name": symbol[0], "description": symbol[1], "value": symbol[2]})

ACTIONCARDS = []
for card in actioncards:
    ACTIONCARDS.append({"name": card[0], "description": card[1], "limit": card[2]})


class Game:

    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.state = ''
        self.player_turn_index = 0

        self.spinned_wheel = False
        self.selected_number = 0
        self.current_field = 0

        self.clicked_object = None

        self.fields = load_fields()

        # self.wheel_fields = self.draw_wheel_fields()
        self.wheel = Wheel(WHEEL_POSITION, WHEEL_RADIUS)

        self.players = pygame.sprite.Group()

        self.game_view = GameView()
        self.is_game_started = False

    def create_players(self, players_data):
        spacing = 1
        for i, player_data in enumerate(players_data):
            player = Player(self.fields[0].x,
                            self.fields[0].y + (i * (PLAYER_SIZE_INACTIVE[1] + spacing)),
                            self.fields[0].rotation, player_data['car_color'], player_data['car_image'],
                            f"Spieler {player_data['player_number']}", player_data['player_number'])
            self.players.add(player)

    def check_spinned_wheel(self, current_player):
        if self.spinned_wheel and self.wheel.has_stopped():
            self.spinned_wheel = False
            self.state = 'player_turn'
            self.selected_number = self.wheel.get_selected_number()
            # self.active_fields = [self.selected_number - 1]

            current_player.steps_to_go = self.selected_number
            current_player.moving = False

    def run(self):
        running = True
        while running:

            current_player = self.players.sprites()[self.player_turn_index]
            if current_player.pause and not self.state == 'next_player':
                self.state = 'player returning'

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        return 'game_pausing'

                    if event.key == pygame.K_SPACE:
                        if self.state == 'player returning':
                            current_player.player_returned = True
                            self.state = 'player_turn'
                        elif self.state == 'next_player':
                            self.state = ''
                            current_player.active = False
                            self.player_turn_index = (self.player_turn_index + 1) % len(self.players)
                            current_player = self.players.sprites()[self.player_turn_index]
                            current_player.active = True
                            self.current_field = current_player.current_field
                            current_player.has_moved = False
                        elif self.state == 'player_turn':
                            pass
                        elif self.state == '':
                            self.is_game_started = True
                            current_player.active = True
                            self.wheel.spin()
                            self.spinned_wheel = True
                        elif self.state == 'marriage_action':
                            self.state = 'marriage'

                """if event.type == pygame.MOUSEMOTION:
                    if self.motion_action >= 0 and self.motion_action in self.active_fields:
                        self.active_fields.remove(self.motion_action)
                    i = self.find_pos(self.pos)
                    if i not in self.active_fields:
                        self.motion_action = i
                    if i not in self.active_fields:
                        self.active_fields.append(i)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    i = self.find_pos(self.pos)
                    if i not in self.active_fields:
                        self.active_fields.append(i)
                    elif self.motion_action is not i:
                        self.active_fields.remove(i)
                    self.motion_action = -1"""

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked_object = self.game_view.get_clickable_object(pos)

            self.check_spinned_wheel(current_player)

            if self.state == 'player_turn':
                self.state = current_player.act(self.fields, self.fields[current_player.current_field])
                self.current_field = current_player.current_field

            self.game_view.draw(self.screen, self.fields[self.current_field], self.players, current_player, self.wheel, self.is_game_started)

            if self.state == 'choose_path':
                self.game_view.draw_choose_path(self.screen)
                if current_player.check_choose_path(self.clicked_object):
                    self.clicked_object = ''
                    self.state = 'player_turn'

            if self.state == 'choose_in_field':
                self.game_view.draw_choose_in_field(self.screen)
                if current_player.check_choose_path(self.clicked_object):
                    self.clicked_object = ''
                    self.state = 'player_turn'

            if self.state == 'marriage':
                # for debug
                from marriage_action import MarriageAction

                marriage_action = MarriageAction(self.screen, self.players.sprites(), current_player, self.wheel)

                self.state = marriage_action.run()

            if self.state == 'game_pausing':
                return 'game_pausing'


            # self.wheel_fields = self.draw_wheel_fields(self.active_fields) # TODO nur wenn glückstag action vorhanden ist und die choice auf spielen gesetzt wurde, zeige die felder

            pygame.display.update()
            self.clock.tick(120)


if __name__ == "__main__":
    Game(pygame.display.set_mode((1700, 930))).run()
