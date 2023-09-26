import pygame
import sys

from Button import Button
from ButtonInterface import TextButton

# Farbdefinitionen
BLACK = (0, 0, 0)
GREY = (105, 105, 105)
RED = (250, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

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

        # Buttons erstellen
        font = pygame.font.SysFont('comicsans', 60)
        self.start_button_i = TextButton(550, 200, BUTTON_SIZE_WIDTH, 100, 'Weiter Spielen',
                                         GREY, BLACK, RED, GREEN, font)
        self.instructions_button_i = TextButton(550, 500, BUTTON_SIZE_WIDTH, 100, 'Anleitung',
                                                GREY, BLACK, RED, YELLOW, font)
        self.quit_button_i = TextButton(550, 650, BUTTON_SIZE_WIDTH, 100, 'Spiel beenden',
                                        GREY, BLACK, RED, RED, font)
        self.restart_button_i = TextButton(550, 350, BUTTON_SIZE_WIDTH, 100, 'Neues Spiel starten',
                                        GREY, BLACK, RED, GREEN, font)

        self.buttons = [self.start_button_i, self.instructions_button_i, self.quit_button_i,
                        self.restart_button_i]

    def redraw_window(self):
        # Hintergrundfarbe
        self.screen.fill(BLACK)

        # Zeichne die Buttons
        for btn in self.buttons:
            btn.draw(self.screen)

    def click_event(self, event_pos):
        if self.start_button_i.rect.collidepoint(event_pos):
            print('Weiter spielen geklickt')
            return 'resume'
        if self.restart_button_i.rect.collidepoint(event_pos):
            print('Neustarten geklickt')
            return 'restart'
        if self.instructions_button_i.rect.collidepoint(event_pos):
            print('Anleitung geklickt')
            return 'instruction'
        if self.quit_button_i.rect.collidepoint(event_pos):
            print('Spiel beenden geklickt')
            pygame.quit()
            sys.exit()

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
                    result = self.click_event(event.pos)
                    if result is not None:
                        return result

                # hover over
                for btn in self.buttons:
                    btn.handle_event(event)

if __name__ == "__main__":
    PauseMenu(pygame.display.set_mode((1700, 930))).run()
