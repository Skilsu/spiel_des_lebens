import pygame
import sys

from Button import Button

# Farbdefinitionen
BLACK = (0, 0, 0)
GREY = (105, 105, 105)

BUTTON_SIZE_WIDTH = 600


class PauseMenu:
    def __init__(self, screen):
        pygame.init()

        self.screen = screen

        # Buttons erstellen
        self.start_button = Button(GREY, 550, 200, BUTTON_SIZE_WIDTH, 100, 'Weiter Spielen')
        self.restart_button = Button(GREY, 550, 350, BUTTON_SIZE_WIDTH, 100, 'Neues Spiel starten')
        self.instructions_button = Button(GREY, 550, 500, BUTTON_SIZE_WIDTH, 100, 'Anleitung')
        self.quit_button = Button(GREY, 550, 650, BUTTON_SIZE_WIDTH, 100, 'Spiel beenden')

    def redraw_window(self):
        # Hintergrundfarbe
        self.screen.fill(BLACK)

        # Zeichne die Buttons
        self.start_button.draw(self.screen, BLACK)
        self.instructions_button.draw(self.screen, BLACK)
        self.quit_button.draw(self.screen, BLACK)
        self.restart_button.draw(self.screen, BLACK)

    def run(self):
        run = True
        while run:
            self.redraw_window()
            pygame.display.update()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_over(pos):
                        print('Weiter spielen geklickt')
                        return 'resume'
                    if self.instructions_button.is_over(pos):
                        print('Anleitung geklickt')
                        return 'instruction'
                    if self.restart_button.is_over(pos):
                        print("Spiel neustarten geklickt")
                        return "restart_game"
                    if self.quit_button.is_over(pos):
                        print('Spiel beenden geklickt')
                        run = False
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    if self.start_button.is_over(pos):
                        self.start_button.color = (0, 255, 0)
                    else:
                        self.start_button.color = GREY
                    if self.restart_button.is_over(pos):
                        self.restart_button.color = (0, 255, 0)
                    else:
                        self.restart_button.color = GREY
                    if self.instructions_button.is_over(pos):
                        self.instructions_button.color = (255, 255, 0)
                    else:
                        self.instructions_button.color = GREY
                    if self.quit_button.is_over(pos):
                        self.quit_button.color = (255, 0, 0)
                    else:
                        self.quit_button.color = GREY


if __name__ == "__main__":
    PauseMenu(pygame.display.set_mode((1700, 930))).run()
