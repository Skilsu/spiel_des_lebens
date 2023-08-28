import pygame


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

# Colors for Wheel
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

# Define the colors and text for each rectangle # TODO this must have the logic like order_decision
rectangles = [
    {"color": RED, "text": "Spieler 1"},
    {"color": GREEN, "text": "Spieler 2"},
    {"color": BLUE, "text": "Spieler 3"},
    {"color": YELLOW, "text": "Spieler 4"},
    {"color": MAGENTA, "text": "Spieler 5"},
    {"color": CYAN, "text": "Spieler 6"},
]

class GameView:

    def __init__(self):
        # Fonts
        self.font_large_bolt = pygame.font.Font(None, 70)
        self.font_large_bolt.set_bold(True)
        self.font = pygame.font.Font(None, 35)
        self.font_text = pygame.font.Font(None, 25)
        self.font_big = pygame.font.Font(None, 50)

        self.board_image = pygame.image.load('graphics/spiel des lebens spielbrett_gimp 1.png').convert()
        self.board_image = pygame.transform.scale(self.board_image, (1100, 800))

        self.clickable_objects = []
        self.register_clickable_objects()

    # this method draw all the screen elements
    def draw(self, screen, current_field, players, current_player, wheel):
        self.draw_field_info(screen, current_field)
        self.draw_player_infos(screen, players)
        screen.blit(self.board_image, (300, 0))
        self.draw_current_player(screen, current_player)
        self.draw_circle_with_i(screen)
        wheel.draw(screen)

        for player in players:
            player.draw()
            screen.blit(player.image, player.rect)

    def register_clickable_objects(self):
        self.clickable_circle_with_i()


    def clickable_circle_with_i(self):
        circle_center = (335, 40)
        circle_radius = 30

        image = pygame.Surface((2 * circle_radius, 2 * circle_radius), pygame.SRCALPHA)
        rect = image.get_rect(center=circle_center)
        self.clickable_objects.append((rect, "Blue Circle"))

    def draw_circle_with_i(self, screen):
        circle_center = (335, 40)
        circle_radius = 30

        pygame.draw.circle(screen, BLUE, circle_center, circle_radius)
        image = pygame.Surface((2 * circle_radius, 2 * circle_radius), pygame.SRCALPHA)
        rect = image.get_rect(center=circle_center)

        screen.blit(image, rect)

        # Draw the "i" symbol in white
        text = self.font_large_bolt.render("i", True, WHITE)
        text_rect = text.get_rect(center=circle_center)
        screen.blit(text, text_rect)

    def draw_current_player(self, screen, current_player):
        y = 5
        x = 1410
        x_text = 1415
        y_box = 75

        verpflichtung = 0
        befreiung = 0
        berechtigung = 0
        rolls_royce = 0
        villa = 0
        kunst = 0
        pferd = 0
        yacht = 0
        jet = 0

        for card in current_player.action_cards:
            if card == "Verpflichtungs-Karte":
                verpflichtung += 1
            elif card == "Befreiungs-Karte":
                befreiung += 1
            elif card == "Berechtigungskarte":
                berechtigung += 1
        for symbol in current_player.status_symbols:
            if symbol == "Rolls Royce":
                rolls_royce += 1
            elif symbol == "Villa in Südfrankreich":
                villa += 1
            elif symbol == "Kunstsammlung":
                kunst += 1
            elif symbol == "Rennpferde":
                pferd += 1
            elif symbol == "Luxus-Yacht":
                yacht += 1
            elif symbol == "Privat-Jet":
                jet += 1

        if verpflichtung > 0:
            y_box += 45
        if befreiung > 0:
            y_box += 45
        if berechtigung > 0:
            y_box += 45
        if rolls_royce > 0:
            y_box += 45
        if villa > 0:
            y_box += 45
        if kunst > 0:
            y_box += 45
        if pferd > 0:
            y_box += 45
        if yacht > 0:
            y_box += 45
        if jet > 0:
            y_box += 45

        if current_player.car:
            y_box += 45
        if current_player.life:
            y_box += 45
        if current_player.fire:
            y_box += 45

        if current_player.pause:
            y_box += 45
        if current_player.debt > 0:
            y_box += 85
        if current_player.job is not None:
            y_box += 25
        if current_player.children:
            dy = int(len(current_player.children) / 11 + 1)
            dy *= 25
            y_box += dy + 5

        pygame.draw.rect(screen, YELLOW, (x - 5, y, 290, y_box))

        # Render the text
        y += 5
        name_surface = self.font.render(current_player.name, True, BLACK)
        screen.blit(name_surface, (x, y))
        y += 25

        if current_player.job is not None:
            job_title = self.font_text.render("Beruf: " + current_player.job, True, BLACK)
            screen.blit(job_title, (x, y))
            y += 20

        money_surface = self.font_text.render("Money: " + str(current_player.money), True, BLACK)
        screen.blit(money_surface, (x, y))
        y += 20

        income_surface = self.font_text.render("Income: " + str(current_player.income), True, BLACK)
        screen.blit(income_surface, (x, y))
        y += 20

        if current_player.children:
            children_surface = self.font_text.render("Kinder: ", True, BLACK)
            screen.blit(children_surface, (x, y))
            y += 20

            dy = 0
            for i in range(int(len(current_player.children) / 11) + 1):
                dx = 0
                for child in current_player.children[11 * i: 11 * (i + 1)]:
                    image = pygame.Surface((20, 20), pygame.SRCALPHA)
                    if child == "boy":
                        pygame.draw.circle(image, BLUE, (10, 10), 10)
                    else:
                        pygame.draw.circle(image, RED, (10, 10), 10)
                    rect = image.get_rect(topleft=(x_text + dx, y + dy))
                    screen.blit(image, rect)
                    dx += 25
                y += 25

        if current_player.status_symbols:
            y = self.draw_single_info_rect(
                screen, GREEN, x, y, 290, 35, rolls_royce, "1 Rolls Royce", "Rolls Royce")
            y = self.draw_single_info_rect(
                screen, GREEN, x, y, 290, 35, villa, "1 Villa in Südfrankreich", "Villen in Südfrankreich")
            y = self.draw_single_info_rect(
                screen, GREEN, x, y, 290, 35, kunst, "1 Kunstsammlung", "Kunstsammlungen")
            y = self.draw_single_info_rect(
                screen, GREEN, x, y, 290, 35, pferd, "1 Rennpferd", "Rennpferde")
            y = self.draw_single_info_rect(
                screen, GREEN, x, y, 290, 35, yacht, "1 Luxus-Yacht", "Luxus-Yachten")
            y = self.draw_single_info_rect(
                screen, GREEN, x, y, 290, 35, jet, "1 Privat-Jet", "Privat-Jets")
        if current_player.car:
            y = self.draw_single_info_rect(screen, GREEN, x, y, 290, 35, 1, "Autoversicherung")
        if current_player.life:
            y = self.draw_single_info_rect(screen, GREEN, x, y, 290, 35, 1, "Lebensversicherung")
        if current_player.fire:
            y = self.draw_single_info_rect(screen, GREEN, x, y, 290, 35, 1, "Feuerversicherung")
        if current_player.aktie:
            y = self.draw_single_info_rect(screen, GREEN, x, y, 290, 35, 1, "Aktie")

        if current_player.debt > 0:
            pygame.draw.rect(screen, CYAN, (x, y, 290, 75))
            y += 5

            debt_title = self.font.render("Schuldschein", True, BLACK)
            screen.blit(debt_title, (x_text, y))

            y += 25
            # TODO Wieso if?
            if current_player.debt == 1:
                debt_text_str = "Du hast 1 Schuldschein."
            else:
                debt_text_str = "Du hast " + str(current_player.debt) + " Schuldscheine."
            debt_text = self.font_text.render(debt_text_str, True, BLACK)
            screen.blit(debt_text, (x_text, y))

            y += 20
            debt_money = self.font_text.render("Wert: " + str(current_player.debt * 20000), True, BLACK)
            screen.blit(debt_money, (x_text, y))

            y += 35

        if current_player.action_cards:
            y = self.draw_single_info_rect(
                screen, GREEN, x, y, 290, 35, verpflichtung, "1x Verpflichtungs Karte", "x Verpflichtungs Karten")
            y = self.draw_single_info_rect(
                screen, GREEN, x, y, 290, 35, befreiung, "1x Befreiungs Karte", "x Befreiungs Karten")
            y = self.draw_single_info_rect(
                screen, GREEN, x, y, 290, 35, berechtigung, "1x Berechtigungs Karte", "x Berechtigungs Karten")

        if current_player.pause:
            y = self.draw_single_info_rect(
                screen, RED, x, y, 275, 35, 1, "Aussetzen!")

    def draw_single_info_rect(self, screen, color, x, y, height, width, amount=0, single=None, more=None):
        if amount > 0:
            pygame.draw.rect(screen, color, (x, y, height, width))
            y += 5

            if amount == 1:
                title = self.font.render(single, True, BLACK)
            else:
                title = self.font.render(str(amount) + " " + more, True, BLACK)
            screen.blit(title, (x + 5, y))
            return y + 40
        return y

    def descriptions(self, screen, x, y):

        debt_description_str = "Ein Schuldschein entspricht 20.000 Schulden. Du kannst einen Schuldschein zu " \
                               "jederzeit im Spiel für 22.000 abbezahlen oder du musst deine Schulden am Ende des" \
                               " Spiels für 25.000 begleichen."
        words = debt_description_str.split()
        text_lines = []
        max_line_width = 280
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if self.font_text.size(test_line)[0] <= max_line_width:
                current_line = test_line
            else:
                text_lines.append(current_line)
                current_line = word + " "
        if current_line:
            text_lines.append(current_line)

        line_height = self.font_text.get_linesize()
        for i, line in enumerate(text_lines):
            text_surface = self.font_text.render(line, True, BLACK)
            screen.blit(text_surface, (1415, 705 + i * line_height))

    """def draw_wheel_fields(self, screen):
       rects = []
        if active_fields is None:
            active_fields = []

        for idx, color in enumerate(colors):
            rect_x = 305 + 1100 * idx / len(colors)
            rect_y = 805
            rect_width = 100
            rect_height = 120
            if idx in active_fields:
                i = idx + 5
                if i > 9:
                    i -= 10
                pygame.draw.rect(screen, colors[i],
                                 (rect_x - 5, rect_y - 5, rect_width + 10, rect_height + 10))
            #rects.append(pygame.draw.rect(screen, color, (rect_x, rect_y, rect_width, rect_height)))
            num_x = rect_x + rect_width / 2
            num_y = rect_y + rect_height / 2

            if idx >= 5:
                num_surface = self.font_big.render(str(idx + 1), True, BLACK)
            else:
                num_surface = self.font_big.render(str(idx + 1), True, WHITE)
            num_rect = num_surface.get_rect(center=(num_x, num_y))

            screen.blit(num_surface, num_rect)
        return rects"""

    def draw_field_info(self, screen, current_field): # current_field = FIELDS[self.current_field]

        pygame.draw.rect(screen, current_field["color"], (0, 800, 300, 130))

        # Render the text
        if current_field["color"] == YELLOW or current_field["color"] == WHITE:
            text_color = BLACK
        else:
            text_color = WHITE

        title_surface = self.font.render(current_field["title"], True, text_color)
        screen.blit(title_surface, (10, 810))

        text_lines = []
        text = current_field["text"]
        max_line_width = 270  # Leave some padding on each side

        # Split the text into lines based on the width of the box
        words = text.split()
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if self.font_text.size(test_line)[0] <= max_line_width:
                current_line = test_line
            else:
                text_lines.append(current_line)
                current_line = word + " "
        if current_line:
            text_lines.append(current_line)

        line_height = self.font_text.get_linesize()
        for i, line in enumerate(text_lines):
            text_surface = self.font_text.render(line, True, text_color)
            screen.blit(text_surface, (10, 840 + i * line_height))

    def draw_player_infos(self, screen, players):
        for i, player in enumerate(players):

            # Draw the rectangle
            pygame.draw.rect(screen, player.color, (5, 5 + 800 * i / len(rectangles), 290, 120))
            # Render the text
            name_surface = self.font.render(player.name, True, WHITE)
            screen.blit(name_surface, (10, 10 + 800 * i / len(rectangles)))

            money_surface = self.font_text.render("Money: " + str(player.money), True, WHITE)
            screen.blit(money_surface, (10, 35 + 800 * i / len(rectangles)))
            income_surface = self.font_text.render("Income: " + str(player.income), True, WHITE)
            screen.blit(income_surface, (10, 55 + 800 * i / len(rectangles)))
            if player.pause:
                pause_surface = self.font_text.render("Aussetzen!", True, WHITE)
                screen.blit(pause_surface, (10, 100 + 800 * i / len(rectangles)))

    def get_clickable_object(self, pos):
        for rect, obj_name in self.clickable_objects:
            if rect.collidepoint(pos):
                # TODO info logic
                print(f"You clicked on the {obj_name}")