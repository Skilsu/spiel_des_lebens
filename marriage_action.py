import pygame
import sys

from wheel import Wheel


WHEEL_RADIUS = 250  # Größe des Rades
WHITE = (255, 255, 255)


class MarriageAction:
    def __init__(self, screen, players, current_player, wheel_from_game):
        pygame.init()
        self.screen = screen
        self.wheel = Wheel((self.screen.get_width() / 2, self.screen.get_height() / 2), WHEEL_RADIUS)
        self.clock = pygame.time.Clock()
        self.players = [player for player in players if player != current_player]
        self.current_player = current_player
        self.font = pygame.font.Font(None, 35)
        self.font_text = pygame.font.Font(None, 25)
        self.spinned_wheel = False

        self.text = ""
        self.sum_money = 0
        self.subtract_money = 0
        self.state = ""

        self.base_text_instruction = [
            "Drehe das Glücksrad und erhalte",
            "von den anderen Spielern:"
        ]
        self.instructions = [
            "- 2.000, wenn eine 1, 2 oder 3 gedreht wurde",
            "- 1.000, wenn eine 4, 5 oder 6 gedreht wurde",
            "- nichts, wenn eine 7, 8, 9 oder 10 gedreht wurde"
        ]

        self.wheel_from_game = wheel_from_game


    def redraw_window(self):
        self.screen.fill((0, 0, 0))

        self.draw_player_infos()
        self.draw_instruction_text()
        self.draw_get_money_text()

        self.wheel.draw(self.screen)
        self.wheel.update()

    def draw_instruction_text(self):

        x_position = 1100
        y_position = 75
        spacing = 30

        for line in self.base_text_instruction:
            text_surface = self.font.render(line, True, WHITE)
            self.screen.blit(text_surface, (x_position, y_position))
            y_position += spacing
        y_position += spacing
        for line in self.instructions:
            text_surface = self.font.render(line, True, WHITE)
            self.screen.blit(text_surface, (x_position + 10, y_position))
            y_position += spacing



    def draw_player_infos(self):
        spacing = 130

        for i, player in enumerate(self.players):
            y_position = 5 + i * spacing

            # Draw the rectangle
            pygame.draw.rect(self.screen, player.color, (5, y_position, 290, 120))
            # Render the text
            name_surface = self.font.render(player.name, True, WHITE)
            self.screen.blit(name_surface, (10, y_position + 5))

            money_surface = self.font_text.render("Money: " + str(player.money), True, WHITE)
            self.screen.blit(money_surface, (10, y_position + 35))

        # current player
        rect_position = (self.screen.get_width() / 2 - 200, self.screen.get_height() / 2 - 400)
        # Draw the rectangle
        pygame.draw.rect(self.screen, self.current_player.color, (*rect_position, 400, 120))
        # Render the text
        name_surface = self.font.render(f"Aktueller Spieler: ({self.current_player.name})", True, WHITE)
        self.screen.blit(name_surface, (rect_position[0] + 5, rect_position[1] + 5))

        money_surface = self.font_text.render("Money: " + str(self.current_player.money), True, WHITE)
        self.screen.blit(money_surface, (rect_position[0] + 5, rect_position[1] + 35))

    def draw_get_money_text(self):
        text_surface = self.font.render(self.text, True, WHITE)

        # Zentriere den Text
        x_pos_centered = (self.screen.get_width() - text_surface.get_width()) // 2

        self.screen.blit(text_surface, (x_pos_centered, 800))


    def act(self):

        if self.state == '':
            if self.spinned_wheel and self.wheel.has_stopped():
                self.spinned_wheel = False
                selected_number = self.wheel.get_selected_number()
                if selected_number in (1, 2, 3):
                    self.subtract_money = 2000
                    self.sum_money = self.subtract_money * len(self.players)
                    self.text = f"Ziehe von allen Spielern 2000 ab und füge die Summe: {self.sum_money} auf dein Konto"

                    self.state = 'wait'

                elif selected_number in (4, 5, 6):
                    self.subtract_money = 1000
                    self.sum_money = self.subtract_money * len(self.players)
                    self.text = f"Ziehe von allen Spielern 1000 ab und füge die Summe: {self.sum_money} auf dein Konto"
                    self.state = 'wait'

                elif selected_number in (7, 8, 9, 10):
                    self.text = "Leider bekommst du keine Geschenke"
                    self.state = 'steps_to_go'

        elif self.state == 'subtract_and_add':
            self.sum_and_subtract_player_money()

            self.base_text_instruction = [
                "Drehe das Rad nochmal und",
                "laufe um die angezeigte Anzahl"

            ]
            self.instructions = []
            self.state = "steps_to_go"
        elif self.state == 'steps_to_go':
            if self.spinned_wheel and self.wheel.has_stopped():
                self.spinned_wheel = False
                selected_number = self.wheel.get_selected_number()
                self.current_player.steps_to_go = selected_number

                # self.wheel_from_game.selected_number = selected_number TODO hauptbildschirm gezeigte nummer im Rad synchronisieren (Nice to have)

                self.state = 'return'


    def sum_and_subtract_player_money(self):
        self.current_player.add_money(self.sum_money)


        for player in self.players:
            player.subtract_money(self.subtract_money)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_SPACE:
                        if self.state == 'wait':
                            self.state = 'subtract_and_add'

                        if self.state == 'return':
                            return 'player_turn'
                        elif self.state == "" or self.state == 'steps_to_go':
                            self.wheel.spin()
                            self.spinned_wheel = True

            self.act()

            self.redraw_window()
            pygame.display.update()
            self.clock.tick(60)

