import pygame
import sys

from Button import Button

# Farbdefinitionen
BLACK = (0, 0, 0)
GREY = (105, 105, 105)

BUTTON_SIZE_WIDTH = 600


class MainMenu:
    def __init__(self, screen):
        pygame.init()

        self.screen = screen

        # Buttons erstellen
        self.start_button = Button(GREY, 550, 400, BUTTON_SIZE_WIDTH, 100, 'Spiel starten')
        self.instructions_button = Button(GREY, 550, 550, BUTTON_SIZE_WIDTH, 100, 'Anleitung')
        self.quit_button = Button(GREY, 550, 700, BUTTON_SIZE_WIDTH, 100, 'Spiel beenden')

        # Game Logo
        self.image_logo = pygame.image.load("graphics/game_logo.png").convert_alpha()
        self.image_logo = pygame.transform.scale(self.image_logo, (600, 300))

    def redraw_window(self):
        # Hintergrundfarbe
        self.screen.fill(BLACK)

        # Zeichne die Buttons
        self.start_button.draw(self.screen, BLACK)
        self.instructions_button.draw(self.screen, BLACK)
        self.quit_button.draw(self.screen, BLACK)

        self.screen.blit(self.image_logo, (550, 100))

    def run(self):
        run = True
        while run:
            self.redraw_window()
            pygame.display.update()
            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():


                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_over(pos):
                        print('Spiel starten geklickt')
                        return 'game_intro_choose_player'
                    if self.instructions_button.is_over(pos):
                        print('Anleitung geklickt')
                        # Hier können Sie die Logik zum Anzeigen der Anleitung hinzufügen
                        return 'instruction'
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
                    if self.instructions_button.is_over(pos):
                        self.instructions_button.color = (255, 255, 0)
                    else:
                        self.instructions_button.color = GREY
                    if self.quit_button.is_over(pos):
                        self.quit_button.color = (255, 0, 0)
                    else:
                        self.quit_button.color = GREY


if __name__ == "__main__":
    MainMenu(pygame.display.set_mode((1700, 930))).run()
