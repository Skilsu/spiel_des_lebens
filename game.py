import json

import pygame

import sys
from player import Player, PLAYER_SIZE_INACTIVE
from wheel import Wheel

# Spiel-Parameter
BACKGROUND_COLOR = (0, 0, 0)
WHEEL_RADIUS = 110  # Größe des Rades
WHEEL_POSITION = (1030, 380)
# WHEEL_ROTATION_SPEED = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

# Define the colors and text for each rectangle
rectangles = [
    {"color": RED, "text": "Spieler 1"},
    {"color": GREEN, "text": "Spieler 2"},
    {"color": BLUE, "text": "Spieler 3"},
    {"color": YELLOW, "text": "Spieler 4"},
    {"color": MAGENTA, "text": "Spieler 5"},
    {"color": CYAN, "text": "Spieler 6"},
]
START_POSITION_PLAYER1 = (1160, 354, 270)
WAYPOINTS = [(1160, 372, 270),  # I divide
             (1237, 257, 0), (1237, 205, 0), (1250, 145, 300),  # I first path end
             (1237, 471, 180), (1242, 515, 228), (1296, 511, 316), (1318, 470, 0), (1318, 430, 0), (1318, 389, 0),
             (1318, 347, 0), (1318, 306, 0), (1318, 265, 0), (1318, 224, 0), (1318, 185, 0),  # I second path end
             (1312, 127, 0),  # I reunion
             (1310, 73, 10), (1268, 40, 70), (1215, 40, 97), (1162, 57, 90), (1117, 43, 65), (1077, 33, 98),
             (1058, 55, 195), (1087, 86, 238), (1128, 112, 238), (1178, 157, 185), (1128, 217, 98), (1060, 191, 61),
             (1018, 166, 61), (980, 132, 35), (973, 93, 5), (948, 48, 42), (903, 38, 93), (860, 52, 142),
             (860, 100, 180), (860, 147, 180), (860, 193, 180), (860, 255, 180), (860, 302, 180), (860, 349, 180),
             (860, 395, 180), (859, 442, 178), (840, 484, 156), (833, 531, 178), (832, 578, 180), (830, 624, 176),
             (806, 665, 142), (762, 699, 105), (708, 704, 81),  # II divide
             (660, 652, 26), (647, 608, 16), (615, 580, 90), (507, 578, 90), (453, 578, 90),
             (395, 564, 75),  # II first path end
             (632, 710, 90), (568, 720, 90), (495, 710, 75), (430, 678, 60), (370, 645, 60), (353, 602, 0),
             # II second path end
             (355, 545, 0),  # II reunion
             (425, 474, 275), (525, 425, 0), (525, 378, 0), (525, 332, 1), (513, 280, 15), (486, 236, 37),
             (447, 205, 55), (407, 93, 335), (443, 55, 300), (502, 38, 285), (564, 41, 271), (615, 41, 271),
             (670, 41, 271), (722, 41, 271), (773, 38, 240), (801, 75, 180), (801, 117, 180), (801, 161, 180),
             (801, 195, 180),  # III divide
             (801, 248, 180), (801, 291, 180), (801, 335, 180), (801, 379, 180), (801, 424, 180), (782, 463, 130),
             (744, 463, 40),  # III first path end
             (747, 220, 120), (744, 266, 180), (744, 309, 180), (744, 352, 180),  # III first path end
             (730, 415, 90),  # III reunion
             (682, 400, 50), (685, 362, 0), (685, 320, 0), (685, 278, 0), (685, 236, 0), (663, 197, 70), (612, 197, 90),
             (560, 182, 45), (558, 143, 305), (605, 145, 270), (642, 125, 325), (636, 92, 55), (595, 95, 90),
             (537, 93, 105), (500, 130, 133), (463, 160, 133), (413, 243, 133), (352, 267, 145), (353, 322, 180),
             (353, 365, 180), (355, 410, 180), (352, 450, 205), (417, 515, 257), (480, 526, 270), (545, 526, 270),
             (607, 525, 265), (670, 540, 230), (703, 590, 195), (717, 640, 230), (763, 630, 340), (758, 580, 15),
             (760, 527, 285), (870, 525, 260), (923, 550, 210), (940, 600, 170), (930, 645, 160), (918, 693, 215),
             (947, 731, 250), (1001, 743, 270), (1056, 743, 270), (1107, 743, 270), (1156, 743, 270), (1209, 743, 270),
             (1258, 740, 275), (1303, 710, 325), (1317, 670, 0), (1287, 625, 60), (1238, 630, 150), (1215, 672, 130),
             (1170, 675, 60), (1167, 615, 0)  # last field
             ]

statussymbols = [["Rolls Royce", "Millionärs-Einkommen aus Vermietung ", 1000],
                 ["Villa in Südfrankreich", "Millionärs-Einkommen aus Vermietung ", 2000],
                 ["Kunstsammlung", "Millionärs-Einkommen aus Ausstellungen ", 3000],
                 ["Rennpferde", "Millionärs-Einkommen aus Geldpreisen ", 3000],
                 ["Luxus-Yacht", "Millionärs-Einkommen aus Charteraufträgen ", 4000],
                 ["Privat-Jet", "Millionärs-Einkommen aus Charterflügen ", 4000]]

bullycards = [["Verpflichtungs-Karte", "Der Inhaber dieser Karte kann von einem Mitspieler seiner Wahl verlangen, "
                                       "die Hälfte des Betrages, den er bezahlen muss, mitzutragen, sofern dieser "
                                       "über 6.000 liegt.", 6000],
              ["Befreiungs-Karte", "Der Inhaber dieser Karte ist berechtigt, Zahlungen aufgrund der "
                                   "Berechtigungskarte oder Verpflichtungskarte eines Mitspielers zu verweigern.", 0],
              ["Berechtigungskarte", "Der Inhaber dieser Karte ist berechtigt, von einem Mitspieler seiner Wahl die "
                                     "Hälfte eines Gewinnes zu verlangen, sofern dieser Gewinn über 10.000 beträgt.",
               10000]]

FIELDS_Vorlage = [{"title": "",
                   "text": "",
                   "following_field": [4],
                   "x": 1160,
                   "y": 372,
                   "rotation": 270,
                   "color": None,
                   "action": []}]

fieldinfo = [["Start", "Du bekommst 3000, ein Auto und eine Autoversicherung", RED, [4], [0]],
             # TODO implementieren von 2 Wegen
             ["", "Du hast dein Bankkonto überzogen. Zahle 1.000.", YELLOW, [2], [1]],
             ["", "Du gewinnst ein Preisausschreiben und erhältst 5.000.", YELLOW, [3], [11]],
             ["", "Du wirst angestellt. Gehalt 5.000. Du rückst 1 Feld vor.", RED, [15], [12]],
             ["", "Du machst die Aufnahmeprüfung. Einmal aussetzen.", YELLOW, [5], [3]],
             ["", "Studiengebühren sind fällig. Zahle 2.000.", RED, [6], [4]],
             ["", "Du fällst durch eine Prüfung. Einmal aussetzen.", YELLOW, [7], [3]],
             ["", "Du bekommst 1.000 für deine Dissertation.", YELLOW, [8], [2]],
             ["", "Du gewinnst beim Pferderennen und erhältst 1.000.", YELLOW, [9], [2]],
             ["", "Artzt! Einkommen 10.000. Du rückst 6 Felder vor.", YELLOW, [10], [5]],
             ["", "Journalist! Einkommen 20.000. Du rückst 5 Felder vor.", YELLOW, [11], [6]],
             ["", "Anwalt! Einkommen 15.000. Du rückst 4 Felder vor.", YELLOW, [12], [7]],
             ["", "Lehrer! Einkommen 8.000. Du rückst 3 Felder vor.", YELLOW, [13], [8]],
             ["", "Physiker! Einkommen 10.000. Du rückst 2 Felder vor.", YELLOW, [14], [9]],
             ["", "Bachelor! Wenn du noch kein Einkommen hast beträgt dein Einkommen jetzt 6.000.", RED, [15], [10]],
             ["Zahltag", "", RED, [16], [16]],
             ["", "Du hast Geburtstag und erhältst 1.000.", YELLOW, [17], [2]],
             ["", "Du gewinnst in der Lotterie und erhältst 50.000.", YELLOW, [18], [13]],
             ["", "Du fichst ein Testament an. Zahle 10.000 Gerichtsgebühren.", YELLOW, [19], [14]],
             ["", "Deine Tante stirbt. Du erbst 50.000", YELLOW, [20], [13]]]

actions = [[False, 3000, False, 0, -1, "car", None, False, False, False, 0],  # + 3.000 und Autoversicherung
           [False, -1000, False, 0, -1, None, None, False, False, False, 0],  # - 1.000
           [False, 1000, False, 0, -1, None, None, False, False, False, 0],  # + 1.000
           [False, 0, True, 0, -1, None, None, False, False, False, 0],  # Pause
           [True, -2000, False, 0, -1, None, None, False, False, False, 0],  # - 2.000 immer
           [False, 0, False, 10000, 6, None, None, False, False, False, 0],  # Einkommen 10.000 und 6 Felder vor
           [False, 0, False, 20000, 5, None, None, False, False, False, 0],  # Einkommen 20.000 und 5 Felder vor
           [False, 0, False, 15000, 4, None, None, False, False, False, 0],  # Einkommen 15.000 und 4 Felder vor
           [False, 0, False, 8000, 3, None, None, False, False, False, 0],  # Einkommen 8.000 und 3 Felder vor
           [False, 0, False, 10000, 2, None, None, False, False, False, 0],  # Einkommen 10.000 und 2 Felder vor
           [True, 0, False, 0, 1, None, None, False, False, False, 6000],
           # Einkommen 6.000 und 1 Feld vor wenn Einkommen vorher 0
           [False, 5000, False, 0, -1, None, None, False, False, False, 0],  # + 5.000
           [True, 0, False, 5000, 1, None, None, False, False, False, 0],  # Einkommen 5.000 und 1 Feld vor immer
           [False, 50000, False, 0, -1, None, None, False, False, False, 0],  # + 50.000
           [False, -10000, False, 0, -1, None, None, False, False, False, 0],  # -10.000
           [False, -5000, False, 0, -1, "live", None, False, False, False, 0],
           # Lebensversicherung abgeschlossen und 5.000 gezahlt
           [False, 0, False, 0, -1, None, None, True, False, False, 0],  # Payday
           [False, 0, False, 0, -1, None, None, False, True, False, 0],  # Marriage
           [False, 0, False, 0, -1, None, "car", False, False, False, 0],  # Autoversicherung verloren
           [False, -4000, False, 0, -1, None, None, False, False, False, 0],  # - 4.000 TODO Versicherung prüfen!
           [False, -10000, False, 0, -1, None, None, False, False, True, 0],  # Buy Statussymbol for 10.000
           [False, 0, False, 0, -1, None, None, False, False, False, 0],
           [False, 0, False, 0, -1, None, None, False, False, False, 0],
           [False, 0, False, 0, -1, None, None, False, False, False, 0],
           [False, 0, False, 0, -1, None, None, False, False, False, 0]]

"""
self.player.append(Player(1170, 360, (0, 212, 28)))
        self.player.append(Player(1185, 360, (255, 0, 0)))
        self.player.append(Player(1200, 360, (0, 212, 28)))
        self.player.append(Player(1215, 360, (255, 255, 0)))
        self.player.append(Player(1230, 360, (0, 212, 28)))
        self.player.append(Player(1245, 360, (255, 255, 0)))
        self.player.append(Player(1245, 411, (0, 68, 220)))
        self.player.append(Player(1230, 411, (255, 0, 0)))
        self.player.append(Player(1215, 411, (0, 68, 220)))
        self.player.append(Player(1200, 411, (255, 0, 0)))
        self.player.append(Player(1170, 411, (255, 255, 0)))
        self.player.append(Player(1185, 411, (0, 68, 220)))
"""

ACTIONS_Vorlage = [{"act with more steps": False,
                    "add_money": 0,
                    "pause": False,
                    "set income": 0,
                    "go more steps": 0,  # -1 = planned, 0 = stay, number = go directed
                    "add insurance": None,
                    "lose insurance": None,
                    "payday": False,
                    "marriage": False,
                    "buy statussymbol": False,
                    "income if 0": 0
                    }]

ACTIONS = []
for action in actions:
    ACTIONS.append({"act with more steps": action[0],
                    "add_money": action[1],
                    "pause": action[2],
                    "set income": action[3],
                    "go more steps": action[4],  # -1 = planned, 0 = stay, number = go directed
                    "add insurance": action[5],
                    "lose insurance": action[6],
                    "payday": action[7],
                    "marriage": action[8],
                    "buy statussymbol": action[9],
                    "income if 0": action[10]
                    })
FIELDS = []
for idx, info in enumerate(fieldinfo):
    FIELDS.append({"title": info[0],
                   "text": info[1],
                   "following_field": info[3],
                   "x": WAYPOINTS[idx][0],
                   "y": WAYPOINTS[idx][1],
                   "rotation": WAYPOINTS[idx][2],
                   "color": info[2],
                   "action": info[4]})
for idx, waypoint in enumerate(WAYPOINTS[len(fieldinfo):]):
    FIELDS.append({"title": "",
                   "text": "Add 1.000.",
                   "following_field": [idx + 21],
                   "x": waypoint[0],
                   "y": waypoint[1],
                   "rotation": waypoint[2],
                   "color": YELLOW,
                   "action": [2]})
for field in FIELDS:
    print(field)
STATUSSYMBOLS = []
for symbol in statussymbols:
    STATUSSYMBOLS.append({"name": symbol[0], "description": symbol[1], "value": symbol[2]})
BULLYCARDS = []
for card in bullycards:
    BULLYCARDS.append({"name": card[0], "description": card[1], "limit": card[2]})


def read_json(filename):
    with open(f"{filename}.json", "r") as infile:
        return json.load(infile)


def save_json(filename, json_dict):
    fields = []
    for idx, waypoint in enumerate(WAYPOINTS):
        fields.append({"title": fieldinfo[0],
                       "text": fieldinfo[1],
                       "following_field": [idx + 1],
                       "x": waypoint[0],
                       "y": waypoint[1],
                       "rotation": waypoint[2],
                       "color": fieldinfo[2],
                       "action": None})
    for symbol in statussymbols:
        STATUSSYMBOLS.append({"name": symbol[0], "description": symbol[1], "value": symbol[2]})
    for card in bullycards:
        BULLYCARDS.append({"name": card[0], "description": card[1], "limit": card[2]})
    data_dict = {"fields": fields, "actions": ACTIONS, "bully_cards": BULLYCARDS, "status_symbols": STATUSSYMBOLS}
    save_json("data", data_dict)
    with open(f"{filename}.json", "w") as outfile:
        json.dump(json_dict, outfile)


class Game:

    def __init__(self, screen, player_number=1):
        self.player_number = 4  # DEBUG Zwecke

        pygame.init()
        self.screen = screen
        # self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.state = ''
        self.player_turn_index = 0

        self.spinned_wheel = False
        self.selected_number = 0

        self.board_image = pygame.image.load('graphics/spiel des lebens spielbrett.jpg').convert()
        self.board_image = pygame.transform.scale(self.board_image, (1100, 800))

        # Für Wheel
        self.colors = [
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
        # Schriftart für die Zahlen in Wheel
        self.font = pygame.font.Font(None, 35)
        self.font_large = pygame.font.Font(None, 70)
        self.wheel = Wheel(WHEEL_POSITION, WHEEL_RADIUS, self.colors, self.font, self.font_large)

        self.players = pygame.sprite.Group()
        spacing = 1

        for i in range(self.player_number):
            player = Player(START_POSITION_PLAYER1[0],
                            START_POSITION_PLAYER1[1] + (i * (PLAYER_SIZE_INACTIVE[1] + spacing)),
                            START_POSITION_PLAYER1[2], self.colors[i], name="Player " + str(i + 1))

            self.players.add(player)
        print(len(self.players.sprites()))

    def draw_current_player(self, current_player):
        pygame.draw.rect(self.screen, YELLOW, (1405, 5, 290, 790))

        # Render the text
        name_surface = self.font.render(current_player.name, True, BLACK)
        self.screen.blit(name_surface, (1410, 10))

        text_font = pygame.font.Font(None, 25)
        money_surface = text_font.render("Money: " + str(current_player.money), True, BLACK)
        self.screen.blit(money_surface, (1410, 35))
        income_surface = text_font.render("Income: " + str(current_player.income), True, BLACK)
        self.screen.blit(income_surface, (1410, 55))

        # TODO als nächstes umsetzen (würde ich gerne machen)
        """
        self.children = []
        self.status_symbols = []
        self.bully_cards = []
        self.insurance = []
        self.debt = 0
        self.income = 0
        self.pause = False
        """
        if current_player.pause:
            pause_surface = self.font.render("Aussetzen!", True, BLACK)
            self.screen.blit(pause_surface, (1410, 780))

    def draw_wheel_fields(self):
        for idx, color in enumerate(self.colors):
            rect_x = 305 + 1100 * idx / len(self.colors)
            rect_y = 805
            rect_width = 100
            rect_height = 120

            pygame.draw.rect(self.screen, color, (rect_x, rect_y, rect_width, rect_height))

            num_x = rect_x + rect_width / 2
            num_y = rect_y + rect_height / 2

            text_font = pygame.font.Font(None, 50)
            if idx >= 5:
                num_surface = text_font.render(str(idx + 1), True, BLACK)
            else:
                num_surface = text_font.render(str(idx + 1), True, WHITE)
            num_rect = num_surface.get_rect(center=(num_x, num_y))

            self.screen.blit(num_surface, num_rect)

    def draw_field_info(self, current_player):
        if current_player.current_field == 0:
            field = 0
        elif self.state == 'player returning':
            field = current_player.current_field - 1
        else:
            field = current_player.current_field

        pygame.draw.rect(self.screen, FIELDS[field]["color"], (0, 800, 300, 130))

        # Render the text
        if FIELDS[field]["color"] == YELLOW:
            text_color = BLACK
        else:
            text_color = WHITE

        title_surface = self.font.render(FIELDS[field]["title"], True, text_color)
        self.screen.blit(title_surface, (10, 810))

        text_font = pygame.font.Font(None, 25)
        text_lines = []
        text = FIELDS[field]["text"]
        max_line_width = 270  # Leave some padding on each side

        # Split the text into lines based on the width of the box
        words = text.split()
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if text_font.size(test_line)[0] <= max_line_width:
                current_line = test_line
            else:
                text_lines.append(current_line)
                current_line = word + " "
        if current_line:
            text_lines.append(current_line)

        line_height = text_font.get_linesize()
        for i, line in enumerate(text_lines):
            text_surface = text_font.render(line, True, text_color)
            self.screen.blit(text_surface, (10, 840 + i * line_height))

    def draw_player_infos(self, current_player):
        for i, player in enumerate(self.players):

            # Draw the rectangle
            pygame.draw.rect(self.screen, player.color, (5, 5 + 800 * i / len(rectangles), 290, 120))

            # Render the text
            name_surface = self.font.render(player.name, True, WHITE)
            self.screen.blit(name_surface, (10, 10 + 800 * i / len(rectangles)))

            text_font = pygame.font.Font(None, 25)
            money_surface = text_font.render("Money: " + str(player.money), True, WHITE)
            self.screen.blit(money_surface, (10, 35 + 800 * i / len(rectangles)))
            income_surface = text_font.render("Income: " + str(player.income), True, WHITE)
            self.screen.blit(income_surface, (10, 55 + 800 * i / len(rectangles)))
            if player.pause:
                pause_surface = text_font.render("Aussetzen!", True, WHITE)
                self.screen.blit(pause_surface, (10, 100 + 800 * i / len(rectangles)))

    def update_player(self, current_player):
        current_player.steps_to_go -= 1
        current_player.moving = True

        # TODO implement choice???
        current_player.x_new = FIELDS[FIELDS[current_player.current_field]["following_field"][0]]["x"]
        current_player.y_new = FIELDS[FIELDS[current_player.current_field]["following_field"][0]]["y"]

        rotation_new = FIELDS[FIELDS[current_player.current_field]["following_field"][0]]["rotation"]

        if current_player.rotation > 180:
            rotation_modified = rotation_new + 360
            diff = abs(current_player.rotation - rotation_modified)
        else:
            rotation_modified = rotation_new - 360
            diff = abs(current_player.rotation - rotation_modified)

        if diff < abs(rotation_new - current_player.rotation):
            rotation_new = rotation_modified
        current_player.rotation_new = rotation_new
        current_player.current_field = FIELDS[current_player.current_field]["following_field"][0]

        return current_player

    def run(self):
        running = True
        while running:

            current_player = self.players.sprites()[self.player_turn_index]
            pause = True
            while pause:
                if current_player.pause:
                    current_player.pause = False

                    self.player_turn_index = (self.player_turn_index + 1) % self.player_number
                    current_player = self.players.sprites()[self.player_turn_index]
                else:
                    pause = False
            # print(current_player.color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        return 'game_pausing'

                    if event.key == pygame.K_SPACE:
                        if self.state == 'player returning':
                            self.state = 'player_moving'
                        elif self.state == 'next_player':
                            self.state = ''
                            current_player.active = False
                            self.player_turn_index = (self.player_turn_index + 1) % self.player_number
                            current_player = self.players.sprites()[self.player_turn_index]
                            current_player.active = True
                        else:
                            current_player.active = True
                            self.wheel.spin()
                            # self.player_turn_index = (self.player_turn_index + 1) % self.player_number
                            if not current_player.moving:
                                current_player.update()

                            self.spinned_wheel = True

            self.wheel.update()
            self.screen.fill((0, 0, 0))
            self.draw_field_info(current_player)

            if self.spinned_wheel and self.wheel.has_stopped():
                self.spinned_wheel = False
                self.state = 'player_moving'
                self.selected_number = self.wheel.get_selected_number()

                current_player.steps_to_go = self.selected_number
                current_player.moving = False
                print(self.selected_number)

            if self.state == 'player_moving':
                if current_player.moving:
                    current_player.move()
                else:
                    if current_player.steps_to_go > 0:
                        if FIELDS[current_player.current_field]["color"] == RED:
                            current_player.act(
                                ACTIONS[FIELDS[current_player.current_field]["action"][0]])  # TODO What if more???
                            self.state = 'player returning'

                        if current_player.steps_to_go > 0:
                            current_player = self.update_player(current_player)
                    else:
                        current_player.act(
                            ACTIONS[FIELDS[current_player.current_field]["action"][0]])  # TODO What if more???

                        if current_player.steps_to_go > 0:
                            current_player = self.update_player(current_player)
                            self.state = 'player returning'
                        else:
                            self.state = 'next_player'

            self.draw_player_infos(current_player)
            self.draw_current_player(current_player)
            self.draw_wheel_fields()
            self.screen.blit(self.board_image, (300, 0))
            self.wheel.draw(self.screen)

            for entity in self.players:
                entity.draw()
                self.screen.blit(entity.image, entity.rect)

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    Game(pygame.display.set_mode((1700, 930))).run()
