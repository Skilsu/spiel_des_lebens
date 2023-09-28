import sys

import pygame
from pygame.locals import *

from ButtonInterface import ImageButton, TextButton

# Farben
WHITE = (255, 255, 255)
BABY_BLUE = (173, 216, 230)
LIGHT_BROWN = (210, 180, 140)
DARK_BROWN = (139, 69, 19)
SELECTED_BROWN = ((LIGHT_BROWN[0] + DARK_BROWN[0]) // 2,
                  (LIGHT_BROWN[1] + DARK_BROWN[1]) // 2,
                  (LIGHT_BROWN[2] + DARK_BROWN[2]) // 2)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class GameIntro:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen

        self.font = pygame.font.SysFont("comicsans", 36)

        # Creating Buttons
        self.number_buttons = self.create_number_buttons()

        self.back_button = TextButton(10, self.screen.get_height() - 60, 150, 50, "Zurück", BLACK, WHITE,
                                  BLACK, RED, self.font)
        self.ok_button = TextButton(self.screen.get_width() - 160, self.screen.get_height() - 60, 150, 50, "OK", BLACK,
                                WHITE, BLACK, GREEN, self.font)

        self.image_buttons = self.create_image_buttons()

        self.number_of_selected_cars = None

        self.state = 'player_number'

        # Auto auswahl
        self.current_selection = 0

        self.selected_cars = []
        self.are_all_cars_selected = False

    def create_image_buttons(self):
        colors = [BABY_BLUE, GREEN, (255, 165, 0), (128, 0, 128), RED,
                  (255, 219, 0)]  # Orange, Lila hinzugefügt
        car_images = ["graphics/other_cars/car_baby_blue.png", "graphics/other_cars/car_green.png",
                      "graphics/other_cars/car_orange.png", "graphics/other_cars/car_purple.png",
                      "graphics/other_cars/car_red.png",
                      "graphics/other_cars/car_yellow.png"]

        button_width_cars, button_height_cars = 250, 250
        button_gap_cars = 20

        start_x_cars = 50  # Anfangs-x-Koordinate
        start_y_cars = 400
        image_buttons = []
        for i, (color, car_image) in enumerate(zip(colors, car_images)):
            btn_x = start_x_cars + i * (button_width_cars + button_gap_cars)
            btn = ImageButton(btn_x, start_y_cars, button_width_cars, button_height_cars, car_image, color,
                              SELECTED_BROWN, color)
            image_buttons.append(btn)

        return image_buttons

    def create_number_buttons(self):
        button_width = 300  # Breite der Schaltflächen
        button_height = 100  # Höhe der Schaltflächen
        button_gap = 30  # Abstand zwischen den Schaltflächen

        start_x = (self.screen.get_width() - button_width) // 2  # Zentrierte x-Koordinate für alle Schaltflächen
        start_y = 250  # Anfangs-y-Koordinate

        number_buttons = [
            TextButton(start_x, start_y + i * (button_height + button_gap), button_width, button_height, str(i + 2),
                       DARK_BROWN, WHITE, SELECTED_BROWN, SELECTED_BROWN, self.font) for i in
            range(5)
        ]
        return number_buttons

    def draw_title(self, text):
        title_font = pygame.font.SysFont("comicsans", 48)
        pygame.draw.rect(self.screen, BABY_BLUE,
                         (0, 0, self.screen.get_width(), int(0.2 * self.screen.get_height())))
        title_text = title_font.render(text, True, WHITE)
        title_text_rect = title_text.get_rect(
            center=(self.screen.get_width() // 2, int(0.15 * self.screen.get_height())))
        margin = 10
        title_frame_rect = pygame.Rect(title_text_rect.left - margin, title_text_rect.top - margin,
                                       title_text_rect.width + 2 * margin, title_text_rect.height + 2 * margin)
        pygame.draw.rect(self.screen, LIGHT_BROWN, title_frame_rect)
        pygame.draw.rect(self.screen, WHITE, title_frame_rect, 2)
        self.screen.blit(title_text, title_text_rect.topleft)
        pygame.draw.line(self.screen, WHITE, (0, title_frame_rect.bottom),
                         (self.screen.get_width(), title_frame_rect.bottom), 2)

    def draw_player_selection_display(self):
        text = f"Ausgewählt: {self.current_selection}/{self.number_of_selected_cars}"
        selection_display_font = pygame.font.SysFont("comicsans", 40)
        rendered_text = selection_display_font.render(text, True, WHITE)
        position = (20, 200)
        self.screen.blit(rendered_text, position)

    def draw_not_all_cars_selected_text(self):
        text = 'Nicht alle Autos ausgewählt'
        text_surface = self.font.render(text, True, RED)
        self.screen.blit(text_surface, (615, 250))

    def run(self):
        running = True
        while running:

            self.screen.fill(LIGHT_BROWN)

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
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return 'game_pausing'


                # Move this outside of MOUSEBUTTONDOWN to handle hover
                if self.state == 'player_number':
                    for index, button in enumerate(self.number_buttons):
                        if button.handle_event(event) and event.type == MOUSEBUTTONDOWN:
                            self.number_of_selected_cars = index + 2
                            for btn in self.number_buttons:
                                btn.active = False
                            button.active = True



                elif self.state == 'choose_color':
                    for btn in self.image_buttons:
                        if btn.handle_event(event) and event.type == MOUSEBUTTONDOWN:
                            if btn.player_number is None and self.current_selection < self.number_of_selected_cars:  # Auto wurde noch nicht ausgewählt
                                self.current_selection += 1
                                btn.player_number = self.current_selection
                            elif btn.player_number is not None:  # Auto wurde bereits ausgewählt
                                deselected_number = btn.player_number
                                btn.player_number = None
                                self.current_selection -= 1
                                # Aktualisieren der player_number für alle anderen ausgewählten Autos
                                for other_btn in self.image_buttons:
                                    if other_btn.player_number and other_btn.player_number > deselected_number:
                                        other_btn.player_number -= 1
                            else:
                                print("Maximale Anzahl an Spielern erreicht!") # TODO maybe show this line on screen


                if event.type == MOUSEBUTTONDOWN:
                    if self.back_button.rect.collidepoint(event.pos):
                        # Zurück-Logik
                        print("Zurück Button gedrückt")
                        if self.state == 'choose_color':  # Return to previous state
                            self.state = 'player_number'

                    if self.ok_button.rect.collidepoint(event.pos) and self.number_of_selected_cars is not None:
                        if self.state == 'choose_color':

                            if self.current_selection == self.number_of_selected_cars:
                                self.selected_cars = [(btn.player_number, btn.bg_color) for btn in self.image_buttons if btn.player_number is not None]
                                self.selected_cars.sort(key=lambda x: x[0])
                                return 'game_intro_order_decision'
                            else:
                                self.are_all_cars_selected = True
                        if self.state == 'player_number':

                            self.state = 'choose_color'


                self.ok_button.handle_event(event)
                self.back_button.handle_event(event)

            if self.current_selection == self.number_of_selected_cars:
                self.are_all_cars_selected = False
            # Draw buttons based on the state
            if self.state == 'player_number':
                for button in self.number_buttons:
                    button.draw(self.screen)
            elif self.state == 'choose_color':
                self.back_button.draw(self.screen)
                self.draw_player_selection_display()

                if self.are_all_cars_selected:
                    self.draw_not_all_cars_selected_text()
                for button in self.image_buttons:
                    button.draw(self.screen)

            if self.number_of_selected_cars is not None:
                self.ok_button.draw(self.screen)

            pygame.display.update()


if __name__ == "__main__":
    GameIntro(pygame.display.set_mode((1700, 930))).run()