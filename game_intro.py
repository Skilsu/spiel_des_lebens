import sys

import pygame
from pygame.locals import *


class Button:
    def __init__(self, x, y, width, height, text, bg_color, txt_color, active_color, hover_color, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = font.render(text, True, txt_color)
        self.bg_color = bg_color
        self.txt_color = txt_color
        self.active_color = active_color
        self.active = False
        self.hover_color = hover_color
        self.hovered = False

    def draw(self, screen):
        color = self.hover_color if self.hovered else self.active_color if self.active else self.bg_color
        pygame.draw.rect(screen, color, self.rect)
        screen.blit(self.text, (self.rect.x + (self.rect.width - self.text.get_width()) // 2,
                                self.rect.y + (self.rect.height - self.text.get_height()) // 2))

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.hovered = False
            return True
        elif event.type == MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hovered = not self.active  # Only hover if the button is not active
            else:
                self.hovered = False
        return False


class ImageButton:
    def __init__(self, x, y, width, height, image_path, bg_color, hover_color, active_color, border_color=(0, 0, 0),
                 border_size=10):
        self.rect = pygame.Rect(x, y, width, height)
        self.image_rect = pygame.Rect(x + border_size, y + border_size, width - 2 * border_size,
                                      height - 2 * border_size)

        self.image = pygame.image.load(image_path).convert_alpha()  # Lädt das Bild
        self.image = pygame.transform.scale(self.image, (
        self.image_rect.width, self.image_rect.height)).convert_alpha()  # Skaliert das Bild auf die Größe innerhalb des Rahmens

        self.bg_color = bg_color
        self.border_color = border_color
        self.active_color = active_color
        self.active = False
        self.hover_color = hover_color
        self.hovered = False

    def draw(self, screen):
        color = self.hover_color if self.hovered else self.active_color if self.active else self.bg_color
        pygame.draw.rect(screen, color, self.rect)  # Hintergrundrechteck
        pygame.draw.rect(screen, self.border_color, self.rect, 2)  # Rahmen
        screen.blit(self.image, self.image_rect.topleft)  # Zeichnet das Bild innerhalb des Rahmens

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True
        elif event.type == MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hovered = not self.active  # Hover nur, wenn der Button nicht aktiv ist
            else:
                self.hovered = False
        return False


class GameIntro:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.title_font = pygame.font.SysFont("comicsans", 48)
        self.font = pygame.font.SysFont("comicsans", 36)
        # Farben
        self.WHITE = (255, 255, 255)
        self.BABY_BLUE = (173, 216, 230)
        self.LIGHT_BROWN = (210, 180, 140)
        self.DARK_BROWN = (139, 69, 19)
        self.SELECTED_BROWN = (
            (self.LIGHT_BROWN[0] + self.DARK_BROWN[0]) // 2,
            (self.LIGHT_BROWN[1] + self.DARK_BROWN[1]) // 2,
            (self.LIGHT_BROWN[2] + self.DARK_BROWN[2]) // 2
        )
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        button_width = 300  # Breite der Schaltflächen
        button_height = 100  # Höhe der Schaltflächen
        button_gap = 30  # Abstand zwischen den Schaltflächen

        start_x = (self.screen.get_width() - button_width) // 2  # Zentrierte x-Koordinate für alle Schaltflächen
        start_y = 250  # Anfangs-y-Koordinate

        self.buttons = [
            Button(start_x, start_y + i * (button_height + button_gap), button_width, button_height, str(i + 2),
                   self.DARK_BROWN, self.WHITE, self.SELECTED_BROWN, self.DARK_BROWN, self.font) for i in range(5)
        ]
        self.back_button = Button(10, self.screen.get_height() - 60, 150, 50, "Zurück", self.BLACK, self.WHITE,
                                  self.BLACK, self.RED, self.font)
        self.ok_button = Button(self.screen.get_width() - 160, self.screen.get_height() - 60, 150, 50, "OK", self.BLACK,
                                self.WHITE, self.BLACK, self.GREEN, self.font)
        self.selected = None

        self.state = 'player_number'

        self.colors = [self.BABY_BLUE, self.GREEN, (255, 165, 0), (128, 0, 128), self.RED,
                  (255, 255, 0)]  # Orange, Lila hinzugefügt
        self.car_images = ["other_cars/car_baby_blue.png", "other_cars/car_green.png", "other_cars/car_orange.png", "other_cars/car_purple.png", "other_cars/car_red.png",
                      "other_cars/car_yellow.png"]

        button_width_cars, button_height_cars = 250, 250  # Beispielgröße
        button_gap_cars = 20

        start_x_cars = 50  # Anfangs-x-Koordinate
        start_y_cars = 400
        self.color_buttons = []
        for i, (color, car_image) in enumerate(zip(self.colors, self.car_images)):
            btn_x = start_x_cars + i * (button_width_cars + button_gap_cars)
            btn = ImageButton(btn_x, start_y_cars, button_width_cars, button_height_cars, car_image, color, self.SELECTED_BROWN, color, border_size=20)
            self.color_buttons.append(btn)

    def draw_title(self, text):
        pygame.draw.rect(self.screen, self.BABY_BLUE,
                         (0, 0, self.screen.get_width(), int(0.2 * self.screen.get_height())))
        title_text = self.title_font.render(text, True, self.WHITE)
        title_text_rect = title_text.get_rect(
            center=(self.screen.get_width() // 2, int(0.15 * self.screen.get_height())))
        margin = 10
        title_frame_rect = pygame.Rect(title_text_rect.left - margin, title_text_rect.top - margin,
                                       title_text_rect.width + 2 * margin, title_text_rect.height + 2 * margin)
        pygame.draw.rect(self.screen, self.LIGHT_BROWN, title_frame_rect)
        pygame.draw.rect(self.screen, self.WHITE, title_frame_rect, 2)
        self.screen.blit(title_text, title_text_rect.topleft)
        pygame.draw.line(self.screen, self.WHITE, (0, title_frame_rect.bottom),
                         (self.screen.get_width(), title_frame_rect.bottom), 2)

    def run(self):
        running = True
        while running:
            self.screen.fill(self.LIGHT_BROWN)

            # Title
            if self.state == 'player_number':
                self.draw_title("Anzahl der Spieler")
            elif self.state == 'choose_color':
                self.draw_title("Wähle die Farben der Spieler")

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                # Move this outside of MOUSEBUTTONDOWN to handle hover
                if self.state == 'player_number':
                    for index, button in enumerate(self.buttons):
                        if button.handle_event(event):
                            if event.type == MOUSEBUTTONDOWN:
                                self.selected = index+2
                                for btn in self.buttons:
                                    btn.active = False
                                button.active = True

                elif self.state == 'choose_color':
                    for btn in self.color_buttons:
                        btn.handle_event(event)
                        btn.draw(self.screen)

                if event.type == MOUSEBUTTONDOWN:
                    if self.back_button.rect.collidepoint(event.pos):
                        # Zurück-Logik
                        print("Zurück Button gedrückt")
                        if self.state == 'choose_color':  # Return to previous state
                            self.state = 'player_number'

                    if self.ok_button.rect.collidepoint(event.pos) and self.selected is not None:
                        if self.state == 'player_number':
                            print(f"Sie haben {self.selected} Spieler ausgewählt.")
                            self.state = 'choose_color'

                self.back_button.handle_event(event)
                self.ok_button.handle_event(event)

            # Draw buttons based on the state
            if self.state == 'player_number':
                for button in self.buttons:
                    button.draw(self.screen)
            elif self.state == 'choose_color':
                for button in self.color_buttons:
                    button.draw(self.screen)

            # Draw back and ok buttons
            self.back_button.draw(self.screen)
            if self.selected is not None:
                self.ok_button.draw(self.screen)

            pygame.display.update()


if __name__ == "__main__":
    GameIntro(pygame.display.set_mode((1700, 930))).run()