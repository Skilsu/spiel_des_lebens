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
actioncards = [["Verpflichtungs-Karte", "Der Inhaber dieser Karte kann von einem Mitspieler seiner Wahl verlangen, "
                                        "die Hälfte des Betrages, den er bezahlen muss, mitzutragen, sofern dieser "
                                        "über 6.000 liegt.", 6000],
               ["Befreiungs-Karte", "Der Inhaber dieser Karte ist berechtigt, Zahlungen aufgrund der "
                                    "Berechtigungskarte oder Verpflichtungskarte eines Mitspielers zu verweigern.", 0],
               ["Berechtigungskarte", "Der Inhaber dieser Karte ist berechtigt, von einem Mitspieler seiner Wahl die "
                                      "Hälfte eines Gewinnes zu verlangen, sofern dieser Gewinn über 10.000 beträgt.",
                10000]]  # TODO Button auf spieler rect um anderem spieler aktion zu ermöglichen

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

actions = [[False, 3000, False, 0, -1, "car", None, False, False, False, 0, None, False],
           # + 3.000 und Autoversicherung
           [False, -1000, False, 0, -1, None, None, False, False, False, 0, None, False],  # - 1.000
           [False, 1000, False, 0, -1, None, None, False, False, False, 0, None, False],  # + 1.000
           [False, 0, True, 0, -1, None, None, False, False, False, 0, None, False],  # Pause
           [True, -2000, False, 0, -1, None, None, False, False, False, 0, None, False],  # - 2.000 immer
           [False, 0, False, 10000, 6, None, None, False, False, False, 0, "Arzt", False],
           # Einkommen 10.000 und 6 Felder vor
           [False, 0, False, 20000, 5, None, None, False, False, False, 0, "Journalist", False],
           # Einkommen 20.000 und 5 Felder vor
           [False, 0, False, 15000, 4, None, None, False, False, False, 0, "Anwalt", False],
           # Einkommen 15.000 und 4 Felder vor
           [False, 0, False, 8000, 3, None, None, False, False, False, 0, "Lehrer", False],
           # Einkommen 8.000 und 3 Felder vor
           [False, 0, False, 10000, 2, None, None, False, False, False, 0, "Physiker", False],
           # Einkommen 10.000 und 2 Felder vor
           [True, 0, False, 0, 1, None, None, False, False, False, 6000, None, False],
           # Einkommen 6.000 und 1 Feld vor wenn Einkommen vorher 0
           [False, 5000, False, 0, -1, None, None, False, False, False, 0, None, False],  # + 5.000
           [True, 0, False, 5000, 1, None, None, False, False, False, 0, None, False],
           # Einkommen 5.000 und 1 Feld vor immer
           [False, 50000, False, 0, -1, None, None, False, False, False, 0, None, False],  # + 50.000
           [False, -10000, False, 0, -1, None, None, False, False, False, 0, None, False],  # -10.000
           [False, -5000, False, 0, -1, "life", None, False, False, False, 0, None, False],
           # Lebensversicherung abgeschlossen und 5.000 gezahlt
           [False, 0, False, 0, -1, None, None, True, False, False, 0, None, False],  # Payday
           [False, 0, False, 0, -1, None, None, False, True, False, 0, None, False],  # Marriage
           [False, 0, False, 0, -1, None, "car", False, False, False, 0, None, False],  # Autoversicherung verloren
           [False, -4000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 4.000 TODO Versicherung prüfen!
           [False, -10000, False, 0, -1, None, None, False, False, True, 0, None, False],  # Buy Statussymbol for 10.000
           [False, 0, False, 0, -1, None, None, False, False, False, 0, None, False],
           [False, 0, False, 0, -1, None, None, False, False, False, 0, None, False],
           [False, 0, False, 0, -1, None, None, False, False, False, 0, None, False],
           [False, 0, False, 0, -1, None, None, False, False, False, 0, None, False]]

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
                    "add insurance": None,  # "car", "fire", "life"
                    "lose insurance": None,
                    "payday": False,
                    "marriage": False,
                    "buy statussymbol": False,
                    "income if 0": 0,
                    "job": None,
                    "aktie": False
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
                    "income if 0": action[10],
                    "job": action[11],
                    "aktie": action[12]
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
ACTIONCARDS = []
for card in actioncards:
    ACTIONCARDS.append({"name": card[0], "description": card[1], "limit": card[2]})


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
    for card in actioncards:
        ACTIONCARDS.append({"name": card[0], "description": card[1], "limit": card[2]})
    data_dict = {"fields": fields, "actions": ACTIONS, "action_cards": ACTIONCARDS, "status_symbols": STATUSSYMBOLS}
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
        self.current_field = 0

        self.board_image = pygame.image.load('graphics/spiel des lebens spielbrett_gimp 1.png').convert()
        self.board_image = pygame.transform.scale(self.board_image, (1100, 800))

        # Für Wheel
        self.colors = colors

        # Schriftart für die Zahlen in Wheel
        self.font_text = pygame.font.Font(None, 25)
        self.font = pygame.font.Font(None, 35)
        self.font_big = pygame.font.Font(None, 50)
        self.font_large = pygame.font.Font(None, 70)
        self.font_large_bolt = pygame.font.Font(None, 70)
        self.font_large_bolt.set_bold(True)

        self.wheel_fields = self.draw_wheel_fields()
        self.active_fields = []
        self.wheel = Wheel(WHEEL_POSITION, WHEEL_RADIUS, self.colors, self.font, self.font_large)

        self.players = pygame.sprite.Group()
        spacing = 1

        self.clickable_objects = []
        for field in self.wheel_fields:
            self.clickable_objects.append(field)
        self.motion_action = -1
        self.pos = (0, 0)

        for i in range(self.player_number):
            player = Player(START_POSITION_PLAYER1[0],
                            START_POSITION_PLAYER1[1] + (i * (PLAYER_SIZE_INACTIVE[1] + spacing)),
                            START_POSITION_PLAYER1[2], self.colors[i], name="Player " + str(i + 1), number=i)

            self.players.add(player)
        print(len(self.players.sprites()))

    def draw_circle_with_i(self):

        circle_center = (335, 40)

        # Draw the circle
        pygame.draw.circle(self.screen, BLUE, circle_center, 30)

        # Draw the "i" symbol in white
        text = self.font_large_bolt.render("i", True, WHITE)
        text_rect = text.get_rect(center=circle_center)
        self.screen.blit(text, text_rect)

    def draw_current_player(self, current_player):
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

        pygame.draw.rect(self.screen, YELLOW, (x - 5, y, 290, y_box))

        # Render the text
        y += 5
        name_surface = self.font.render(current_player.name, True, BLACK)
        self.screen.blit(name_surface, (x, y))
        y += 25

        if current_player.job is not None:
            job_title = self.font_text.render("Beruf: " + current_player.job, True, BLACK)
            self.screen.blit(job_title, (x, y))
            y += 20

        money_surface = self.font_text.render("Money: " + str(current_player.money), True, BLACK)
        self.screen.blit(money_surface, (x, y))
        y += 20

        income_surface = self.font_text.render("Income: " + str(current_player.income), True, BLACK)
        self.screen.blit(income_surface, (x, y))
        y += 20

        if current_player.children:
            children_surface = self.font_text.render("Kinder: ", True, BLACK)
            self.screen.blit(children_surface, (x, y))
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
                    self.screen.blit(image, rect)
                    dx += 25
                y += 25

        if current_player.status_symbols:
            y = self.draw_single_info_rect(
                GREEN, x, y, 290, 35, rolls_royce, "1 Rolls Royce", "Rolls Royce")
            y = self.draw_single_info_rect(
                GREEN, x, y, 290, 35, villa, "1 Villa in Südfrankreich", "Villen in Südfrankreich")
            y = self.draw_single_info_rect(
                GREEN, x, y, 290, 35, kunst, "1 Kunstsammlung", "Kunstsammlungen")
            y = self.draw_single_info_rect(
                GREEN, x, y, 290, 35, pferd, "1 Rennpferd", "Rennpferde")
            y = self.draw_single_info_rect(
                GREEN, x, y, 290, 35, yacht, "1 Luxus-Yacht", "Luxus-Yachten")
            y = self.draw_single_info_rect(
                GREEN, x, y, 290, 35, jet, "1 Privat-Jet", "Privat-Jets")
        if current_player.car:
            y = self.draw_single_info_rect(GREEN, x, y, 290, 35, 1, "Autoversicherung")
        if current_player.life:
            y = self.draw_single_info_rect(GREEN, x, y, 290, 35, 1, "Lebensversicherung")
        if current_player.fire:
            y = self.draw_single_info_rect(GREEN, x, y, 290, 35, 1, "Feuerversicherung")

        if current_player.debt > 0:
            pygame.draw.rect(self.screen, CYAN, (x, y, 290, 75))
            y += 5

            debt_title = self.font.render("Schuldschein", True, BLACK)
            self.screen.blit(debt_title, (x_text, y))

            y += 25
            if current_player.debt == 1:
                debt_text_str = "Du hast 1 Schuldschein."
            else:
                debt_text_str = "Du hast " + str(current_player.debt) + " Schuldscheine."
            debt_text = self.font_text.render(debt_text_str, True, BLACK)
            self.screen.blit(debt_text, (x_text, y))

            y += 20
            debt_money = self.font_text.render("Wert: " + str(current_player.debt * 20000), True, BLACK)
            self.screen.blit(debt_money, (x_text, y))

            y += 35

        if current_player.action_cards:
            y = self.draw_single_info_rect(
                GREEN, x, y, 290, 35, verpflichtung, "1x Verpflichtungs Karte", "x Verpflichtungs Karten")
            y = self.draw_single_info_rect(
                GREEN, x, y, 290, 35, befreiung, "1x Befreiungs Karte", "x Befreiungs Karten")
            y = self.draw_single_info_rect(
                GREEN, x, y, 290, 35, berechtigung, "1x Berechtigungs Karte", "x Berechtigungs Karten")

        if current_player.pause:
            y = self.draw_single_info_rect(
                RED, x, y, 275, 35, 1, "Aussetzen!")

    def draw_single_info_rect(self, color, x, y, hight, witdh, amount=0, single=None, more=None):
        if amount > 0:
            pygame.draw.rect(self.screen, color, (x, y, hight, witdh))
            y += 5

            if amount == 1:
                title = self.font.render(single, True, BLACK)
            else:
                title = self.font.render(str(amount) + " " + more, True, BLACK)
            self.screen.blit(title, (x + 5, y))
            return y + 40
        return y

    def descriptions(self, x, y):

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
            self.screen.blit(text_surface, (1415, 705 + i * line_height))

    def draw_wheel_fields(self, active_fields=None):
        rects = []
        if active_fields is None:
            active_fields = []
        for idx, color in enumerate(self.colors):
            rect_x = 305 + 1100 * idx / len(self.colors)
            rect_y = 805
            rect_width = 100
            rect_height = 120
            if idx in active_fields:
                i = idx + 5
                if i > 9:
                    i -= 10
                pygame.draw.rect(self.screen, self.colors[i],
                                 (rect_x - 5, rect_y - 5, rect_width + 10, rect_height + 10))
            rects.append(pygame.draw.rect(self.screen, color, (rect_x, rect_y, rect_width, rect_height)))
            num_x = rect_x + rect_width / 2
            num_y = rect_y + rect_height / 2

            if idx >= 5:
                num_surface = self.font_big.render(str(idx + 1), True, BLACK)
            else:
                num_surface = self.font_big.render(str(idx + 1), True, WHITE)
            num_rect = num_surface.get_rect(center=(num_x, num_y))

            self.screen.blit(num_surface, num_rect)
        return rects

    def draw_field_info(self):

        pygame.draw.rect(self.screen, FIELDS[self.current_field]["color"], (0, 800, 300, 130))

        # Render the text
        if FIELDS[self.current_field]["color"] == YELLOW:
            text_color = BLACK
        else:
            text_color = WHITE

        title_surface = self.font.render(FIELDS[self.current_field]["title"], True, text_color)
        self.screen.blit(title_surface, (10, 810))

        text_lines = []
        text = FIELDS[self.current_field]["text"]
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
            self.screen.blit(text_surface, (10, 840 + i * line_height))

    def draw_player_infos(self, current_player):
        for i, player in enumerate(self.players):

            # Draw the rectangle
            pygame.draw.rect(self.screen, player.color, (5, 5 + 800 * i / len(rectangles), 290, 120))

            # Render the text
            name_surface = self.font.render(player.name, True, WHITE)
            self.screen.blit(name_surface, (10, 10 + 800 * i / len(rectangles)))

            money_surface = self.font_text.render("Money: " + str(player.money), True, WHITE)
            self.screen.blit(money_surface, (10, 35 + 800 * i / len(rectangles)))
            income_surface = self.font_text.render("Income: " + str(player.income), True, WHITE)
            self.screen.blit(income_surface, (10, 55 + 800 * i / len(rectangles)))
            if player.pause:
                pause_surface = self.font_text.render("Aussetzen!", True, WHITE)
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

    def find_pos(self, pos):
        for idx, rect in enumerate(self.clickable_objects):
            if rect.collidepoint(pos):
                return idx
        return -1

    def run(self):
        running = True
        while running:

            current_player = self.players.sprites()[self.player_turn_index]
            if current_player.pause and not self.state == 'next_player':
                self.state = 'player returning'

            self.pos = pygame.mouse.get_pos()

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
                            self.current_field = current_player.current_field
                            current_player.has_moved = False
                        elif self.state == 'player_moving':
                            pass
                        else:
                            current_player.active = True
                            self.wheel.spin()
                            # self.player_turn_index = (self.player_turn_index + 1) % self.player_number
                            if not current_player.moving:
                                current_player.update()

                            self.spinned_wheel = True

                if event.type == pygame.MOUSEMOTION:
                    if self.motion_action >= 0 and self.motion_action in self.active_fields:
                        self.active_fields.remove(self.motion_action)
                    i = self.find_pos(self.pos)
                    if i not in self.active_fields:
                        self.motion_action = i
                    if i not in self.active_fields:
                        self.active_fields.append(i)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    i = self.find_pos(self.pos)
                    if i not in self.active_fields:
                        self.active_fields.append(i)
                    elif self.motion_action is not i:
                        self.active_fields.remove(i)
                    self.motion_action = -1

            self.wheel.update()
            self.screen.fill((0, 0, 0))
            self.draw_field_info()

            if self.spinned_wheel and self.wheel.has_stopped():
                self.spinned_wheel = False
                self.state = 'player_moving'
                self.selected_number = self.wheel.get_selected_number()
                self.active_fields = [self.selected_number - 1]

                current_player.steps_to_go = self.selected_number
                current_player.moving = False

            if self.state == 'player_moving':
                if current_player.moving:
                    current_player.move()
                else:
                    if current_player.steps_to_go > 0:
                        if current_player.has_moved or current_player.current_field == 0:
                            if FIELDS[current_player.current_field]["color"] == RED or \
                                    FIELDS[current_player.current_field]["color"] == WHITE:
                                if ACTIONS[FIELDS[current_player.current_field]["action"][0]]["income if 0"] == 0 \
                                        or current_player.income == 0:  # Einzelfallbehandlung! Sinnvoll?
                                    current_player.act(
                                        ACTIONS[
                                            FIELDS[current_player.current_field]["action"][0]])  # TODO What if more???
                                    self.state = 'player returning'
                                    self.current_field = current_player.current_field
                        current_player.has_moved = True
                        if current_player.steps_to_go > 0:
                            current_player = self.update_player(current_player)
                    else:
                        current_player.act(
                            ACTIONS[FIELDS[current_player.current_field]["action"][0]])  # TODO What if more???
                        self.current_field = current_player.current_field

                        if current_player.steps_to_go > 0:
                            current_player = self.update_player(current_player)
                            self.state = 'player returning'
                        else:
                            self.state = 'next_player'

            self.draw_player_infos(current_player)
            self.draw_current_player(current_player)
            self.wheel_fields = self.draw_wheel_fields(self.active_fields)
            self.screen.blit(self.board_image, (300, 0))
            self.draw_circle_with_i()
            self.wheel.draw(self.screen)

            for entity in self.players:
                entity.draw()
                self.screen.blit(entity.image, entity.rect)

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    Game(pygame.display.set_mode((1700, 930))).run()
