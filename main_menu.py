import pygame
import sys


# Button Klasse
class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


class MainMenu:
    def __init__(self, screen):
        pygame.init()

        # Bildschirmeinstellungen
        WIDTH, HEIGHT = 1400, 800
        self.screen = screen
        # self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # Farbdefinitionen
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREY = (105, 105, 105)

        self.BUTTON_SIZE_WIDTH = 600

        # Buttons erstellen
        self.start_button = Button(self.GREY, 550, 400, self.BUTTON_SIZE_WIDTH, 100, 'Spiel starten')
        self.instructions_button = Button(self.GREY, 550, 550, self.BUTTON_SIZE_WIDTH, 100, 'Anleitung')
        self.quit_button = Button(self.GREY, 550, 700, self.BUTTON_SIZE_WIDTH, 100, 'Spiel beenden')

        # Game Logo
        self.image_logo = pygame.image.load("graphics/game_logo.png").convert_alpha()
        self.image_logo = pygame.transform.scale(self.image_logo, (600, 300))

    def redraw_window(self):
        # Hintergrundfarbe
        self.screen.fill((self.BLACK))

        # Zeichne die Buttons
        self.start_button.draw(self.screen, self.BLACK)
        self.instructions_button.draw(self.screen, self.BLACK)
        self.quit_button.draw(self.screen, self.BLACK)

        self.screen.blit(self.image_logo, (550,100))

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
                        print('Spiel starten geklickt')
                        return 'game_intro_choose_player'
                    if self.instructions_button.is_over(pos):
                        print('Anleitung geklickt')
                        # Hier können Sie die Logik zum Anzeigen der Anleitung hinzufügen
                    if self.quit_button.is_over(pos):
                        print('Spiel beenden geklickt')
                        run = False
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    if self.start_button.is_over(pos):
                        self.start_button.color = (0, 255, 0)
                    else:
                        self.start_button.color = self.GREY
                    if self.instructions_button.is_over(pos):
                        self.instructions_button.color = (255, 255, 0)
                    else:
                        self.instructions_button.color = self.GREY
                    if self.quit_button.is_over(pos):
                        self.quit_button.color = (255, 0, 0)
                    else:
                        self.quit_button.color = self.GREY


if __name__ == "__main__":
    MainMenu(pygame.display.set_mode((1700, 930))).run()
