import pygame
import sys

from wheel import Wheel


WHEEL_RADIUS = 250  # Größe des Rades
WHITE = (255, 255, 255)


class MarriageAction:
    def __init__(self, screen, players, current_player):
        pygame.init()
        self.screen = screen
        self.wheel = Wheel((self.screen.get_width() / 2, self.screen.get_height() / 2), WHEEL_RADIUS)
        self.clock = pygame.time.Clock()
        self.players = [player for player in players if player != current_player]
        self.current_player = current_player
        self.font = pygame.font.Font(None, 35)
        self.font_text = pygame.font.Font(None, 25)
        self.spinned_wheel = False


    def redraw_window(self):
        self.screen.fill((0, 0, 0))

        self.draw_player_infos()
        self.draw_instruction_text()

        self.wheel.draw(self.screen)
        self.wheel.update()

    def draw_instruction_text(self):
        base_text = [
            "Drehe das Glücksrad und erhalte von den anderen",
            "Spielern:"
        ]

        instructions = [
            "- 2.000, wenn eine 1, 2 oder 3 gedreht wurde",
            "- 1.000, wenn eine 4, 5 oder 6 gedreht wurde",
            "- nichts, wenn eine 7, 8, 9 oder 10 gedreht wurde"
        ]

        x_position = 1100
        y_position = 75
        spacing = 30

        for line in base_text:
            text_surface = self.font.render(line, True, WHITE)
            self.screen.blit(text_surface, (x_position, y_position))
            y_position += spacing
        y_position += spacing
        for line in instructions:
            text_surface = self.font.render(line, True, WHITE)
            self.screen.blit(text_surface, (x_position + 10, y_position))
            y_position += spacing



    def draw_player_infos(self):
        for i, player in enumerate(self.players):

            # Draw the rectangle
            pygame.draw.rect(self.screen, player.color, (5, 5 + 800 * i / len(player.name), 290, 120))
            # Render the text
            name_surface = self.font.render(player.name, True, WHITE)
            self.screen.blit(name_surface, (10, 10 + 800 * i / len(player.name)))

            money_surface = self.font_text.render("Money: " + str(player.money), True, WHITE)
            self.screen.blit(money_surface, (10, 35 + 800 * i / len(player.name)))

        # current player
        rect_position = (self.screen.get_width() / 2 - 200, self.screen.get_height() / 2 - 400)
        # Draw the rectangle
        pygame.draw.rect(self.screen, self.current_player.color, (*rect_position, 400, 120))
        # Render the text
        name_surface = self.font.render(f"Aktueller Spieler: ({self.current_player.name})", True, WHITE)
        self.screen.blit(name_surface, (rect_position[0] + 5, rect_position[1] + 5))

        money_surface = self.font_text.render("Money: " + str(self.current_player.money), True, WHITE)
        self.screen.blit(money_surface, (rect_position[0] + 5, rect_position[1] + 35))


    def act(self):
        if self.spinned_wheel and self.wheel.has_stopped():
            self.spinned_wheel = False
            selected_number = self.wheel.get_selected_number()
            if selected_number in (1, 2, 3):
                print("zwischen 1-3")
            elif selected_number in (4, 5, 6):
                print("zwischen 4-6")
            elif selected_number in (7, 8, 9, 10):
                print("zwischen 7-10")

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
                        self.wheel.spin()
                        self.spinned_wheel = True

            self.act()




            self.redraw_window()
            pygame.display.update()
            self.clock.tick(60)

