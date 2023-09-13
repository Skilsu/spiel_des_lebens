import collections
import sys
import pygame
from pygame.locals import *
from wheel import Wheel

# TODO Bug when starting from game_state => stichwahl isnt correct
# TODO Bug when pausing the game on stichwahl

WHEEL_RADIUS = 250  # Größe des Rades
WHITE = (255, 255, 255)

# for Wheel
colors = [
    (168, 0, 185),  # Lila
    (255, 0, 255),  # pink
    (255, 0, 0),  # rot
    (255, 73, 0),  # rot-orange
    (255, 109, 0),  # orange-rot
    (255, 146, 0),  # orange
    (255, 182, 0),  # orange-gelb
    (255, 219, 0),  # gelb-orange
    (255, 255, 0),  # gelb
    (200, 255, 0)  # gelb-grün
]

car_colors = {
    'baby_blue':  (173, 216, 230),
    'green':  (0, 255, 0),
    'orange':  (255, 165, 0),
    'purple':  (128, 0, 128),
    'red':  (255, 0, 0),
    'yellow':  (255, 219, 0)
}


class GameIntro:
    def __init__(self, screen):

        pygame.init()
        self.screen = screen

        self.font = pygame.font.Font(None, 35)
        self.wheel = Wheel((self.screen.get_width()/2, self.screen.get_height()/2), WHEEL_RADIUS)
        self.clock = pygame.time.Clock()
        self.players_data = None
        self.image_directory = 'graphics/other_cars/'

        self.spinned_wheel = False
        self.player_turn_index = 0
        self.current_player = None
        self.state = ''
        self.text = ''
        self.additional_turn_players = []

        self.is_round_over = False
        self.duplicates = False
        self.players_data = None
        # for debug
        """players_data = [(1, (173, 216, 230)), (2, (0, 255, 0)), (3, (255, 165, 0)), (4, (128, 0, 128)), (5, (255, 0, 0)), (6, (255, 219, 0))]
        self.players_data = [{'player_number': num, 'car_color': color} for num, color in players_data]
        for player in self.players_data:
            color_name = [name for name, rgb in car_colors.items() if rgb == player["car_color"]][0]
            car_image_path = self.image_directory + "car_" + color_name + ".png"
            player["car_image"] = pygame.image.load(car_image_path).convert_alpha()
            player["car_image"] = pygame.transform.scale(player["car_image"], (80, 80))
            player["wheeled_number"] = 0"""

    def append_players_data(self, players_data):
        self.players_data = [{'player_number': num, 'car_color': color} for num, color in players_data]
        for player in self.players_data:
            color_name = [name for name, rgb in car_colors.items() if rgb == player["car_color"]][0]
            car_image_path = self.image_directory + "car_" + color_name + ".png"
            player["car_image"] = pygame.image.load(car_image_path).convert_alpha()
            player["car_image"] = pygame.transform.scale(player["car_image"], (80, 80))
            player["wheeled_number"] = 0


    def draw_player_infos(self):

        spacing = 130

        for i, player in enumerate(self.players_data):
            y_position = 5 + i * spacing

            # Zeichnen des Rechtecks
            pygame.draw.rect(self.screen, player['car_color'], (5, y_position, 290, 120))

            # Darstellung des Texts
            name_surface = self.font.render(f"Spieler: {player['player_number']}", True, WHITE)
            self.screen.blit(name_surface, (10, y_position + 5))

            # Darstellung des Platzes
            order_number = self.font.render(f"Platz: {i + 1}", True, WHITE)
            self.screen.blit(order_number, (10, y_position + 35))

            # Darstellung der gedrehten Zahl
            number_surface = self.font.render(f"Zahl: {player['wheeled_number']}", True, WHITE)
            self.screen.blit(number_surface, (10, y_position + 90))

            # Darstellung des Spieler-Autos
            self.screen.blit(player["car_image"], (200, y_position + 5))

    def draw_player_turn_text(self):
        if self.is_round_over:
            self.text = "Aktuelle Reihenfolge"

            # Es gibt Stichwahl
            if self.duplicates and self.additional_turn_players:

                result_str = 'Stichwahl zwischen:\n'

                for pair in self.additional_turn_players:
                    for player in pair:
                        result_str += 'Spieler {} & '.format(player['player_number'])
                    result_str = result_str[:-3] + '\n'

                text_for_stichwahl = result_str

            # Es gibt keine Stichwahl
            else:
                text_for_stichwahl = 'Spiel wird gestartet'

            lines = text_for_stichwahl.split('\n')

            y_pos = 800

            for line in lines:
                text_surface = self.font.render(line, True, WHITE)
                x_pos_centered = (self.screen.get_width() - text_surface.get_width()) // 2
                self.screen.blit(text_surface, (x_pos_centered, y_pos))
                y_pos += text_surface.get_height()
        else:
            self.text = f"Spieler: {self.current_player['player_number']} drehe das Rad um deine Reihenfolge zu bestimmen"
        text_surface = self.font.render(self.text, True, WHITE)

        # Zentriere den Text
        x_pos_centered = (self.screen.get_width() - text_surface.get_width()) // 2

        self.screen.blit(text_surface, (x_pos_centered, 150))

    def redraw_window(self):
        self.wheel.update()
        self.screen.fill((0, 0, 0))
        self.draw_player_infos()
        self.wheel.draw(self.screen)
        self.draw_player_turn_text()

    def act(self, players):
        if self.spinned_wheel and self.wheel.has_stopped():
            self.spinned_wheel = False
            self.current_player['wheeled_number'] = self.wheel.get_selected_number()
            self.state = 'next_player'

            # ein kompletter durchgang
            if self.player_turn_index == (len(players) - 1):

                self.is_round_over = True

                # Sortiere die Spieler nach der gedrehten Zahl
                players.sort(key=lambda x: x['wheeled_number'], reverse=True)

                self.update_player_positions(players)

                self.check_duplicate(players)
                self.state = 'order'

    def update_player_positions(self, updated_players):
        # Finde die Indizes der zu aktualisierenden Spieler in self.players_data
        indices_to_update = []
        for i, original_player in enumerate(self.players_data):
            for updated_player in updated_players:
                if original_player['player_number'] == updated_player['player_number']:
                    indices_to_update.append(i)

        # Aktualisiere die Spieler an den gefundenen Indizes
        for i, index in enumerate(indices_to_update):
            self.players_data[index] = updated_players[i]

    def check_duplicate(self, players):
        # Überprüfe, ob es Duplikate gibt
        numbers = [player['wheeled_number'] for player in players]
        duplicates = [item for item, count in collections.Counter(numbers).items() if count > 1]

        if duplicates:
            self.duplicates = True
            # Wenn es Duplikate gibt, führe eine zusätzliche Runde für die betroffenen Spieler durch
            for duplicate_number in duplicates:
                # Spieler, die erneut drehen müssen
                self.additional_turn_players.append([player for player in players if
                                           player['wheeled_number'] == duplicate_number])

    def run(self):
        running = True
        while running:

            if not self.duplicates:
                players_data = self.players_data
            self.current_player = players_data[self.player_turn_index]

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return 'game_pausing'
                    if event.key == K_SPACE:
                        if self.state == '':
                            self.wheel.spin()
                            self.spinned_wheel = True

                        if self.state == 'next_player':
                            self.state = ''
                            self.player_turn_index = (self.player_turn_index + 1) % len(players_data)
                            self.current_player = players_data[self.player_turn_index]

                        if self.state == 'order':

                            if self.duplicates and self.additional_turn_players:
                                players_data = self.additional_turn_players.pop(0)
                                self.is_round_over = False
                                self.player_turn_index = (self.player_turn_index + 1) % len(players_data)
                                self.state = ''

                            else:
                                print(self.players_data)
                                return 'game_playing'

            self.act(players_data)

            self.redraw_window()
            pygame.display.update()
            self.clock.tick(120)


if __name__ == "__main__":
    GameIntro(pygame.display.set_mode((1700, 930))).run()



