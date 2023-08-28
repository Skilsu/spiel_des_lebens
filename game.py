import json

import pygame

import sys
from player import Player, PLAYER_SIZE_INACTIVE
from wheel import Wheel
from game_view import GameView

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
ORANGE = (255, 165, 0)

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

# TEST_POSITION = (801, 195, 180)
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
             (660, 652, 26), (647, 608, 16), (615, 580, 90), (562, 578, 90), (507, 578, 90), (453, 578, 90),
             (395, 564, 75),  # II first path end
             (632, 710, 90), (568, 720, 90), (495, 710, 75), (430, 678, 60), (370, 645, 60), (353, 602, 0),
             # II second path end
             (355, 545, 0),  # II reunion
             (367, 492, 315), (425, 474, 275), (485, 469, 280), (525, 425, 0), (525, 378, 0), (525, 332, 1),
             (513, 280, 15), (486, 236, 37),
             (447, 205, 55), (407, 145, 0), (407, 93, 335), (443, 55, 300), (502, 38, 285), (564, 41, 271),
             (615, 41, 271),
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
             ["", "Du fichtst ein Testament an. Zahle 10.000 Gerichtsgebühren.", YELLOW, [19], [14]],
             ["", "Deine Tante stirbt. Du erbst 50.000.", YELLOW, [20], [13]],
             ["", "Wenn du eine Lebensversicherung abschließen willst, zahle 5000.", WHITE, [21], [15]],
             # TODO Choice in White field + change font of text to another color because white on white
             ["", "Du verlobst Dich. Zahle 1000 für den Verlobungsring.", YELLOW, [22], [1]],
             ["", "Du gewinnst bei einem Fernsehquiz und erhältst 5000.", YELLOW, [23], [11]],
             ["Zahltag", "", RED, [24], [16]],
             ["", "Geschwindigkeitsübertretung. Zahle 1000.", YELLOW, [25], [1]],
             ["", "Du heiratest. Sammle Geschenke ein.", RED, [26], [17]],
             ["", "Du gehst auf Hochzeitsreise. Zahle 1000.", YELLOW, [27], [1]],
             ["", "Du hast einen Termin als Geschworener. Einmal aussetzen.", YELLOW, [28], [3]],
             ["", "Du verlierst deine Autoversicherung wegen Raserei.", YELLOW, [29], [18]],
             ["", "Autounfall! Zahle 4000, wenn du nicht versichert bist.", YELLOW, [30], [19]],
             ["", "Die Flitterwochen sind vorüber. Zahle 10.000 für fällige Rechnungen.", YELLOW, [31], [1]],
             # TODO Schuldscheine überprüfen
             ["", "Option auf den Kauf eines Status Symbols für 10.000", YELLOW, [32], [20]],
             # TODO choice buy statussymbol
             ["Zahltag", "", RED, [33], [16]],
             ["", "Erpressung durch den Butler. Zahle 10.000.", YELLOW, [34], [14]],
             ["", "Verspätetes Hochzeitsgeschenk. Du erhältst 80.000.", YELLOW, [35], [21]],
             ["", "Parkverbot! Einmal aussetzen.", YELLOW, [36], [3]],
             ["", "Du kaufst ein kleines Haus. Zahle 15.000.", RED, [37], [22]],  # Haus?
             ["", "Wenn du eine Feuerversicherung abschließen willst, zahle 5000.", WHITE, [38], [23]],
             # TODO Choice in White field + change font of text to another color because white on white
             ["Zahltag", "", RED, [39], [16]],
             ["Glückstag", "Du erhältst 10.000. Behalte sie oder spiele auf 150.000.", YELLOW, [40], [1]],
             # TODO Glückstag regel
             ["", "Ein Sohn! Du erhältst 1.000 von jedem Mitspieler.", YELLOW, [41], [1]],
             # TODO adding children and becoming money from every player
             ["", "Option auf den Kauf eines Status Symbols für 12.000", YELLOW, [42], [24]],
             # TODO choice buy statussymbol
             ["", "Eine Tochter! Du erhältst 1.000 von jedem Mitspieler.", YELLOW, [43], [1]],
             # TODO adding children and becoming money from every player
             ["Zahltag", "", RED, [44], [16]],
             ["", "Du gewinnst beim Pferderennen und erhältst 50.000", YELLOW, [45], [13]],
             ["", "Klage auf Schadenersatz. Dir werden 50.000 zugesprochen", ORANGE, [46], [1]],
             # TODO choice spieler auswählen und geld von ihm nehmen
             # Dieses Feld weg, da Spielfeld zu klein ["", "Zwillinge! Du erhältst 2.000 von jedem Mitspieler.", YELLOW, [47], [1]], # TODO adding children and becoming money from every player
             ["", "Steuernachzahlung. Zahle 10.000 für jedes Status Symbol.", RED, [47], [1]],
             # TODO statussymbole zählen
             ["", "Wenn du eine Aktie kaufen willst, zahle 25.000.", WHITE, [48], [25]],
             # TODO Choice in White field + change font of text to another color because white on white
             ["", "Ein Sohn! Du erhältst 1.000 von jedem Mitspieler.", YELLOW, [49], [1]],
             # TODO adding children and becoming money from every player
             # TODO implementieren von 2 Wegen
             ["", "Wenn du ein Aktionär bist, kannst du an der Börse spekulieren.", WHITE, [50], [1]],
             # TODO Choice in White field + change font of text to another color because white on white + Check aktie and spekulieren an der Börse Spielregel
             ["", "Option auf den Kauf eines Status Symbols für 10.000", YELLOW, [51], [20]],
             # TODO choice buy statussymbol
             ["", "Baisse. Wenn du ein Aktionär bist, zahle 16.000", YELLOW, [52], [26]],
             ["Zahltag", "", RED, [53], [16]],
             ["", "Zinsen auf deine Ersparnisse. Du bekommst 40.000", YELLOW, [54], [27]],
             ["", "Eine Tochter! Du erhältst 1.000 von jedem Mitspieler.", YELLOW, [55], [1]],
             # TODO adding children and becoming money from every player
             ["", "Autounfall! Zahle 6000, wenn du nicht versichert bist.", YELLOW, [56], [28]],
             ["", "Drehe das Glücksrad. Du erhältst 1.000 mal Deine Zahl.", YELLOW, [57], [1]],
             # TODO Glücksrad drehen und geld bekommen
             ["", "Eine Tochter! Du erhältst 1.000 von jedem Mitspieler.", YELLOW, [58], [1]],
             # TODO adding children and becoming money from every player
             ["", "Du gewinnst eine Rally! DU erhältst 120.000", YELLOW, [59], [29]],
             ["", "Baisse. Wenn du ein Aktionär bist, zahle 16.000", YELLOW, [60], [26]],
             ["Zahltag", "", RED, [61], [16]],
             ["", "Option auf den Kauf eines Status Symbols für 18.000", YELLOW, [62], [30]],
             # TODO choice buy statussymbol
             ["", "Deine Schallplatte ist in der Hauptrunde. Du erhältst 50.000", YELLOW, [63], [13]],
             ["", "Option auf den Kauf eines Status Symbols für 14.000", YELLOW, [64], [31]],
             # TODO choice buy statussymbol
             ["", "Klage auf Schadenersatz. Dir werden 60.000 zugesprochen", ORANGE, [65], [1]],
             # TODO choice spieler auswählen und geld von ihm nehmen
             ["Glückstag", "Du erhältst 10.000. Behalte sie oder spiele auf 150.000.", YELLOW, [66], [1]],
             # TODO Glückstag regel
             ["", "Ein Sohn! Du erhältst 1.000 von jedem Mitspieler.", YELLOW, [67], [1]],
             # TODO adding children and becoming money from every player
             ["Zahltag", "Zahle Zinsen auf Schuldscheine", RED, [68], [16]],  # TODO Zinsen auf Schuldscheine
             ["", "Hausse. Wenn du ein Aktionär bist, erhältst du 100.000", YELLOW, [69], [32]],
             ["", "Option auf den Kauf eines Status Symbols für 16.000", YELLOW, [70], [33]],
             # TODO choice buy statussymbol
             ["", "Baisse. Wenn du ein Aktionär bist, zahle 8.000", YELLOW, [71], [34]],
             ["", "Du hast zu viel Steuern gezahlt und bekommst 5.000 zurück.", YELLOW, [72], [11]],
             ["Zahltag", "Wenn du Geschäftsmann bist, erhöhe dein Einkommen auf 12.000", RED, [73], [16]],
             # TODO Erhöhung Einkommen bei Geschäftsmann
             ["", "Wenn du eine Lebensversicherung hast, erhältst du 30.000", YELLOW, [74], [35]],
             ["", "Du besteigst den Mount Everest und bekommst 50.000", YELLOW, [75], [13]],
             ["", "Eine Tochter! Du erhältst 1.000 von jedem Mitspieler.", YELLOW, [76], [1]],
             # TODO adding children and becoming money from every player
             ["", "Steuernachzahlung. Zahle ein halbes Gehalt", RED, [77], [1]],  # TODO halbes gehalt abziehen
             ["Glückstag", "Du erhältst 10.000. Behalte sie oder spiele auf 150.000.", YELLOW, [78], [1]],
             # TODO Glückstag regel
             ["", "Option auf den Kauf eines Status Symbols für 28.000", YELLOW, [79], [36]],
             # TODO choice buy statussymbol
             ["Zahltag", "", RED, [80], [16]],
             ["", "Wenn du ein Aktionär bist, kannst du an der Börse spekulieren.", WHITE, [81], [1]],
             # TODO Choice in White field + change font of text to another color because white on white + Check aktie and spekulieren an der Börse Spielregel
             ["", "Klage auf Schadenersatz. Dir werden 80.000 zugesprochen", ORANGE, [82], [1]],
             # TODO choice spieler auswählen und geld von ihm nehmen
             ["", "Du erfindest einen automatischen Cocktail-Shaker und erhältst dafür 20.000", YELLOW, [83], [37]],
             ["", "Du gewinnst ein Tennis-Turnier und bekommst 40.000", YELLOW, [84], [27]],
             ["", "Option auf den Kauf eines Status Symbols für 20.000", YELLOW, [85], [38]],
             # TODO choice buy statussymbol
             ["", "Du finanziert eine erfolglose Expedition zum Südpol. Zahle 30.000", YELLOW, [86], [39]],
             ["Zahltag", "", RED, [87], [16]],
             ["", "Wenn du eine Lebensversicherung hast, erhältst du 24.000", YELLOW, [88], [40]],
             ["", "Autounfall! Zahle 18.000, wenn du nicht versichert bist.", YELLOW, [89], [41]],
             ["", "Dein Haus ist renovierungsbedürftig. Gib deine Feuerversicherung zurück.", YELLOW, [90], [42]],
             ["", "Wenn du Aktionär bist, bekommst du 7.000", YELLOW, [91], [43]],
             ["", "Du gewinnst einen Prozess und erhältst 100.000 ", YELLOW, [92], [44]],
             ["", "Allgemeine Wahlen. Zahle 16.000 in die Parteikasse", YELLOW, [93], [45]],
             ["Zahltag", "", RED, [94], [16]],
             ["", "Wenn du Aktionär bist, bekommst du 5.000", YELLOW, [95], [46]],
             ["", "Du gewinnst in der Lotterie und erhältst 10.000", YELLOW, [96], [47]],
             ["Zahltag", "Zahle Zinsen auf Schuldscheine", RED, [97], [16]],  # TODO Zinsen auf Schuldscheine
             ["Glückstag", "Du erhältst 10.000. Behalte sie oder spiele auf 150.000.", YELLOW, [98], [1]],
             # TODO Glückstag regel
             ["", "Drehe das Glücksrad. Du erhältst 1.000 mal Deine Zahl.", YELLOW, [99], [1]],
             # TODO Glücksrad drehen und geld bekommen
             ["", "Du erbst eine Skunk-Farm. Zahle 12.000, um sie loszuwerden.", YELLOW, [100], [48]],
             ["", "GOLDMINE! Wenn du Aktionär bist, bekommst du 150.000", YELLOW, [101], [49]],
             ["", "Option auf den Kauf eines Status Symbols für 20.000", YELLOW, [102], [38]],
             # TODO choice buy statussymbol
             ["", "Drehe das Glücksrad. Du erhältst 2.000 mal Deine Zahl.", YELLOW, [103], [1]],
             # TODO Glücksrad drehen und geld bekommen
             ["", "Du machst eine Weltreise. Zahle 8.000", YELLOW, [104], [50]],
             ["Zahltag", "", RED, [105], [16]],
             ["", "Dein Onkel sitzt im Gefängnis. Zahle eine Kaution von 2.000", YELLOW, [106], [51]],
             ["", "Option auf den Kauf eines Status Symbols für 18.000", YELLOW, [107], [30]],
             # TODO choice buy statussymbol
             ["", "Du schreibst einen Bestseller und erhältst 80.000", YELLOW, [108], [21]],
             ["", "Eine Ziege frisst deine preisgekrönten Orchideen. Du setzt einmal aus, um sie zu verjagen.", YELLOW,
              [109], [3]],
             ["", "Du hast Übergewicht! Mache Urlaub auf einer Gesundheitsfarm und zahle 6.000", YELLOW, [110], [52]],
             ["", "Du bekommst eine eigene TV Serie und erhältst 40.000", YELLOW, [111], [27]],
             ["Zahltag", "", RED, [112], [16]],
             ["", "Wenn du ein Aktionär bist, kannst du an der Börse spekulieren.", WHITE, [113], [1]],
             # TODO Choice in White field + change font of text to another color because white on white + Check aktie and spekulieren an der Börse Spielregel
             ["", "Option auf den Kauf eines Status Symbols für 24.000", YELLOW, [114], [53]],
             # TODO choice buy statussymbol
             ["", "Steuernachzahlung. Zahle ein halbes Gehalt", RED, [115], [1]],  # TODO halbes gehalt abziehen
             ["", "Du entdeckst beim Tiefseetauchen einen Schatz und erhältst 20.000", YELLOW, [116], [37]],
             ["", "Klage auf Schadenersatz. Dir werden 100.000 zugesprochen", ORANGE, [117], [1]],
             # TODO choice spieler auswählen und geld von ihm nehmen
             ["", "Schenkung für wohltätige Zwecke. Zahle 16.000", YELLOW, [118], [45]],
             ["Zahltag", "Zahle Zinsen auf Schuldscheine", RED, [119], [16]],  # TODO Zinsen auf Schuldscheine
             ["", "Wenn du eine Lebensversicherung hast, erhältst du 50.000", YELLOW, [120], [54]],
             ["", "Hausse. Wenn du ein Aktionär bist, erhältst du 60.000", YELLOW, [121], [55]],
             ["", "Steuernachzahlung. Zahle 5.000 für jedes Status Symbol.", RED, [122], [1]],
             # TODO statussymbole zählen
             ["", "Option auf den Kauf eines Status Symbols für 28.000", YELLOW, [123], [36]],
             # TODO choice buy statussymbol
             ["Glückstag", "Du erhältst 10.000. Behalte sie oder spiele auf 150.000.", YELLOW, [124], [1]],
             # TODO Glückstag regel
             ["", "Dein Haus brennt. Zahle 26.000, wenn du nicht versichert bist.", YELLOW, [125], [56]],
             ["Zahltag", "", RED, [126], [16]],
             ["", "Du erhältst Tantiemen aus einem Film in Höhe von 50.000", YELLOW, [127], [13]],
             ["", "Deine Tante hinterlässt dir ihre streunenden Katzen. Zahle 12.000 Unterhaltungskosten.", YELLOW,
              [128], [48]],
             ["", "Wenn du keine Kinder hast, zahle 50.000 an ein Waisenhaus.", YELLOW, [129], [57]],
             ["", "Option auf den Kauf eines Status Symbols für 30.000", YELLOW, [130], [58]],
             # TODO choice buy statussymbol
             ["", "Du bekommst den Nobelpreis und erhältst 50.000", YELLOW, [131], [13]],
             ["", "Du gehst zum Fischen. Setze einmal aus.", YELLOW, [132], [3]],
             ["", "ÖL! Wenn du Aktionär bist, erhältst du 200.000", YELLOW, [133], [59]],
             ["Zahltag", "", RED, [134], [16]],
             ["", "Du verkaufst deine Lebensgeschichte und erhältst 100.000", YELLOW, [135], [44]],
             ["", "Verkaufe ein beliebiges Status Symbol für 250.000 an die Bank zurück.", YELLOW, [136], [1]],
             # TODO choice statussymbol and sell to bank
             ["", "Dein Haus brennt. Zahle 40.000, wenn du nicht versichert bist.", YELLOW, [137], [60]],
             ["Zahltag", "Zahle Zinsen auf Schuldscheine", RED, [138], [16]],  # TODO Zinsen auf Schuldscheine
             ["", "Du gehst zum Film. Zahle 50.000 zum Aufbau eines neuen Images.", YELLOW, [139], [61]],
             ["", "Wenn du eine Lebensversicherung hast bekommst du 100.000", YELLOW, [140], [62]],
             ["", "Wenn du Aktionär bist, bekommst du 200.000", YELLOW, [141], [59]],
             ["Glückstag", "Du erhältst 10.000. Behalte sie oder spiele auf 150.000.", YELLOW, [142], [1]],
             # TODO Glückstag regel
             ["", "Klage auf Schadenersatz. Dir werden 200.000 zugesprochen", ORANGE, [143], [1]],
             # TODO choice spieler auswählen und geld von ihm nehmen
             ["Zahltag", "", RED, [144], [16]],
             ["", "Option auf den Kauf eines Status Symbols für 50.000", YELLOW, [145], [63]],
             # TODO choice buy statussymbol
             ["", "Übernahmeangebot erfolgreich. Du erhältst 100.000", YELLOW, [146], [44]],
             ["", "Wenn du eine Lebensversicherung hast bekommst du 100.000", RED, [147], [62]],
             ["TAG DER ABRECHNUNG", "", RED, [147], [62]],  # TODO Tag der Abrechnung Spielregel
             ]
actions_neu = [{"add_money": 3000, "add_insurance": "car"}]
actions = [[False, 3000, False, 0, -1, "car", None, False, False, False, 0, None, False],
           # + 3.000 und Autoversicherung   #0
           [False, -1000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 1.000                        #1
           [False, 1000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 1.000                         #2
           [False, 0, True, 0, -1, None, None, False, False, False, 0, None, False],
           # Pause                               #3
           [True, -2000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 2.000 immer                   #4
           [False, 0, False, 10000, 6, None, None, False, False, False, 0, "Arzt", False],  # 5
           # Einkommen 10.000 und 6 Felder vor
           [False, 0, False, 20000, 5, None, None, False, False, False, 0, "Journalist", False],  # 6
           # Einkommen 20.000 und 5 Felder vor
           [False, 0, False, 15000, 4, None, None, False, False, False, 0, "Anwalt", False],  # 7
           # Einkommen 15.000 und 4 Felder vor
           [False, 0, False, 8000, 3, None, None, False, False, False, 0, "Lehrer", False],  # 8
           # Einkommen 8.000 und 3 Felder vor
           [False, 0, False, 10000, 2, None, None, False, False, False, 0, "Physiker", False],  # 9
           # Einkommen 10.000 und 2 Felder vor
           [True, 0, False, 0, 1, None, None, False, False, False, 6000, None, False],  # 10
           # Einkommen 6.000 und 1 Feld vor wenn Einkommen vorher 0
           [False, 5000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 5.000                                                 #11
           [True, 0, False, 5000, 1, None, None, False, False, False, 0, None, False],  # 12
           # Einkommen 5.000 und 1 Feld vor immer
           [False, 50000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 50.000                                               #13
           [False, -10000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # -10.000                                               #14
           [False, -5000, False, 0, -1, "life", None, False, False, False, 0, None, False],
           # Lebensversicherung abgeschlossen und 5.000 gezahlt    #15
           [False, 0, False, 0, -1, None, None, True, False, False, 0, None, False],
           # Payday TODO Schikane Karte erhalten, nur wenn keine besitzt #16
           [False, 0, False, 0, 0, None, None, False, True, False, 0, None, False],
           # Marriage TODO Heirat Spielregel                            #17
           [False, 0, False, 0, -1, None, "car", False, False, False, 0, None, False],
           # Autoversicherung verloren                                 #18
           [False, -4000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 4.000 TODO Versicherung prüfen!                      #19
           [False, -10000, False, 0, -1, None, None, False, False, True, 0, None, False],
           # Buy Statussymbol for 10.000                            #20
           [False, 80000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 80.000                                                #21
           [True, -15000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # -15.000 immer                                          #22
           [False, -5000, False, 0, -1, "fire", None, False, False, False, 0, None, False],
           # Feuerversicherung abgeschlossen und 5.000 gezahlt     #23
           [False, -12000, False, 0, -1, None, None, False, False, True, 0, None, False],
           # Buy Statussymbol for 12.000                            #24
           [False, -25000, False, 0, -1, None, None, False, False, False, 0, None, True],
           # Aktie gekauft und 25.000 gezahlt                       #25
           [False, -16000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 16.000 TODO Aktie prüfen!                           #26
           [False, 40000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 40.000                                               #27
           [False, -6000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 6.000 TODO Versicherung prüfen!                       #28
           [False, 120000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 120.000                                             #29
           [False, -18000, False, 0, -1, None, None, False, False, True, 0, None, False],
           # Buy Statussymbol for 18.000                            #30
           [False, -14000, False, 0, -1, None, None, False, False, True, 0, None, False],
           # Buy Statussymbol for 14.000                            #31
           [False, 100000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 100.000 TODO Aktie prüfen!                          #32
           [False, -16000, False, 0, -1, None, None, False, False, True, 0, None, False],
           # Buy Statussymbol for 16.000                            #33
           [False, -8000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 8.000 TODO Aktie prüfen!                             #34
           [False, 30000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 30.000 TODO Versicherung prüfen!                      #35
           [False, -28000, False, 0, -1, None, None, False, False, True, 0, None, False],
           # Buy Statussymbol for 28.000                            #36
           [False, 20000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 20.000                                                #37
           [False, -20000, False, 0, -1, None, None, False, False, True, 0, None, False],
           # Buy Statussymbol for 20.000                            #38
           [False, -30000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 30.000                                               #39
           [False, 24000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 24.000 TODO Versicherung prüfen!                      #40
           [False, -18000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 18.000 TODO Versicherung prüfen!                     #41
           [False, 0, False, 0, -1, None, "fire", False, False, False, 0, None, False],
           # Feuerversicherung verloren                               #42
           [False, 7000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 7.000 TODO Aktie prüfen!                               #43
           [False, 100000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 100.000                                              #44
           [False, -16000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # -16.000                                                #45
           [False, 5000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 5.000 TODO Aktie prüfen!                               #46
           [False, 10000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 10.000                                                #47
           [False, -12000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 12.000                                               #48
           [False, 150000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 150.000 TODO Aktie prüfen!                          #49
           [False, -8000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 8.000                                                 #50
           [False, -2000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 2.000                                                 #51
           [False, -6000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 6.000                                                 #52
           [False, -24000, False, 0, -1, None, None, False, False, True, 0, None, False],
           # Buy Statussymbol for 24.000                            #53
           [False, 40000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 40.000 TODO Versicherung prüfen!                      #54
           [False, 60000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 60.000 TODO Aktie prüfen!                            #55
           [False, -26000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 26.000 TODO Versicherung (fire) prüfen!              #56
           [False, -50000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 50.000 TODO Kinder prüfen                            #57
           [False, -30000, False, 0, -1, None, None, False, False, True, 0, None, False],
           # Buy Statussymbol for 30.000                            #58
           [False, 200000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 200.000 TODO Aktie prüfen!                          #59
           [False, -40000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 40.000 TODO Versicherung (fire) prüfen!              #60
           [False, -50000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # - 50.000                                               #61
           [False, 100000, False, 0, -1, None, None, False, False, False, 0, None, False],
           # + 100.000 TODO Versicherung (life) prüfen!             #62
           [False, -50000, False, 0, -1, None, None, False, False, True, 0, None, False],
           # Buy Statussymbol for 50.000                            #63
           ]

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
"""for idx, waypoint in enumerate(WAYPOINTS[len(fieldinfo):]):
    FIELDS.append({"title": "",
                   "text": "Add 1.000.",
                   "following_field": [idx + 21],
                   "x": waypoint[0],
                   "y": waypoint[1],
                   "rotation": waypoint[2],
                   "color": YELLOW,
                   "action": [2]})"""
"""for field in FIELDS:
    print(field)"""
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

    with open(f"{filename}.json", "w") as outfile:
        json.dump(json_dict, outfile)


class Game:

    def __init__(self, screen, player_number=1):
        self.player_number = player_number
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
        self.font_text = pygame.font.Font(None, 25) # verwendet in draw_current_player
        self.font = pygame.font.Font(None, 35) # verwendet in draw_current_player
        self.font_big = pygame.font.Font(None, 50) # draw wheel fields
        self.font_large = pygame.font.Font(None, 70)
        self.font_large_bolt = pygame.font.Font(None, 70) # verwendet in draw_circle_with_i
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
        # print(len(self.players.sprites()))

        """# printing one car
        self.car_image = pygame.transform.scale(pygame.image.load("graphics/car_red.png").convert_alpha(), (25, 40)).convert_alpha()
        self.car_image = pygame.transform.rotate(self.car_image, TEST_POSITION[2])
        self.car_rect = self.car_image.get_rect(topleft=(TEST_POSITION[0], TEST_POSITION[1]))"""

        self.game_view = GameView()

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
        if current_player.aktie:
            y = self.draw_single_info_rect(GREEN, x, y, 290, 35, 1, "Aktie")

        if current_player.debt > 0:
            pygame.draw.rect(self.screen, CYAN, (x, y, 290, 75))
            y += 5

            debt_title = self.font.render("Schuldschein", True, BLACK)
            self.screen.blit(debt_title, (x_text, y))

            y += 25
            # TODO Wieso if?
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

    def draw_player_infos(self):
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
            self.screen.fill(BACKGROUND_COLOR)


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

                                    """for action in self.field[current_player.current_field].actions:
                                        action.act(current_player)"""

                                    current_player.act(
                                        ACTIONS[
                                            FIELDS[current_player.current_field]["action"][0]])  # TODO What if more???
                                    self.state = 'player returning'
                                    self.current_field = current_player.current_field
                        current_player.has_moved = True
                        if current_player.steps_to_go > 0:
                            # following_field = current_player.current_field.get_following_field()
                            # current_player.update_position(self.fields(following_field))

                            current_player.update_position(
                                FIELDS[FIELDS[current_player.current_field]["following_field"][0]]["x"],
                                FIELDS[FIELDS[current_player.current_field]["following_field"][0]]["y"],
                                FIELDS[FIELDS[current_player.current_field]["following_field"][0]]["rotation"],
                                FIELDS[current_player.current_field]["following_field"][0])
                    else:
                        current_player.act(
                            ACTIONS[FIELDS[current_player.current_field]["action"][0]])  # TODO What if more???
                        self.current_field = current_player.current_field

                        if current_player.steps_to_go > 0:
                            # following_field = current_player.current_field.get_following_field()
                            # current_player.update_position(self.fields(following_field))

                            current_player.update_position(
                                FIELDS[FIELDS[current_player.current_field]["following_field"][0]]["x"],
                                FIELDS[FIELDS[current_player.current_field]["following_field"][0]]["y"],
                                FIELDS[FIELDS[current_player.current_field]["following_field"][0]]["rotation"],
                                FIELDS[current_player.current_field]["following_field"][0])

                            self.state = 'player returning'
                        else:
                            self.state = 'next_player'

            self.game_view.draw(self.screen, FIELDS[self.current_field], self.players, current_player)


            #self.draw_field_info()
            #self.draw_player_infos()
            #self.draw_current_player(current_player)
            self.wheel_fields = self.draw_wheel_fields(self.active_fields)
            #self.screen.blit(self.board_image, (300, 0))
            #self.draw_circle_with_i()
            self.wheel.draw(self.screen)

            for entity in self.players:
                entity.draw()
                self.screen.blit(entity.image, entity.rect)

            # self.screen.blit(self.car_image, self.car_rect)

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    Game(pygame.display.set_mode((1700, 930))).run()
