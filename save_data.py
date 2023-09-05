import json

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

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

fieldinfo = [["Start", "Du bekommst 3000, ein Auto und eine Autoversicherung. Wähle 'Links' oder 'Rechts'", RED, [1, 4], {"add_money": 3000, "add_insurance": "car"}],
             # TODO implementieren von 2 Wegen
             ["", "Du hast dein Bankkonto überzogen. Zahle 1.000.", YELLOW, [2], {"add_money": -1000}],
             ["", "Du gewinnst ein Preisausschreiben und erhältst 5.000.", YELLOW, [3], {"add_money": 5000}],
             ["", "Du wirst angestellt. Gehalt 5.000. Du rückst 1 Feld vor.", RED, [15], {"set_income": 5000, "more_steps": 1}],
             ["", "Du machst die Aufnahmeprüfung. Einmal aussetzen.", YELLOW, [5], {"pause": "value"}], # value not important, what to do?
             ["", "Studiengebühren sind fällig. Zahle 2.000.", RED, [6], {"add_money": -2000}],
             ["", "Du fällst durch eine Prüfung. Einmal aussetzen.", YELLOW, [7], {"pause": "value"}],
             ["", "Du bekommst 1.000 für deine Dissertation.", YELLOW, [8], {"add_money": 1000}],
             ["", "Du gewinnst beim Pferderennen und erhältst 1.000.", YELLOW, [9], {"add_money": 1000}],
             ["", "Arzt! Einkommen 10.000. Du rückst 6 Felder vor.", YELLOW, [10], {"set_income": 10000, "job": "Arzt", "more_steps": 6}],
             ["", "Journalist! Einkommen 20.000. Du rückst 5 Felder vor.", YELLOW, [11], {"set_income": 20000, "job": "Journalist", "more_steps": 5}],
             ["", "Anwalt! Einkommen 15.000. Du rückst 4 Felder vor.", YELLOW, [12], {"set_income": 15000, "job": "Anwalt", "more_steps": 4}],
             ["", "Lehrer! Einkommen 8.000. Du rückst 3 Felder vor.", YELLOW, [13], {"set_income": 8000, "job": "Lehrer", "more_steps": 3}],
             ["", "Physiker! Einkommen 10.000. Du rückst 2 Felder vor.", YELLOW, [14], {"set_income": 10000, "job": "Physiker", "more_steps": 2}],
             ["", "Bachelor! Wenn du noch kein Einkommen hast beträgt dein Einkommen jetzt 6.000.", RED, [15], {"set_income": 6000, "more_steps": 1}],
             ["Zahltag", "", RED, [16], {"payday": "value"}], # value not important, what to do?
             ["", "Du hast Geburtstag und erhältst 1.000.", YELLOW, [17], {"add_money": 1000}],
             ["", "Du gewinnst in der Lotterie und erhältst 50.000.", YELLOW, [18], {"add_money": 50000}],
             ["", "Du fichtst ein Testament an. Zahle 10.000 Gerichtsgebühren.", YELLOW, [19], {"add_money": -10000}],
             ["", "Deine Tante stirbt. Du erbst 50.000.", YELLOW, [20], {"add_money": 50000}],
             ["", "Wenn du eine Lebensversicherung abschließen willst, zahle 5000.", WHITE, [21], {"choice_in_field": "value", "add_money": -5000, "add_insurance": 'life'}], # value not important, what to do?
             ["", "Du verlobst Dich. Zahle 1000 für den Verlobungsring.", YELLOW, [22], {"add_money": -1000}],
             ["", "Du gewinnst bei einem Fernsehquiz und erhältst 5000.", YELLOW, [23], {"add_money": 5000}],
             ["Zahltag", "", RED, [24], {"payday": "value"}],
             ["", "Geschwindigkeitsübertretung. Zahle 1000.", YELLOW, [25], {"add_money": -1000}],
             ["", "Du heiratest. Sammle Geschenke ein.", RED, [26], [17]], # TODO ab hier
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
             ["", "Ein Sohn! Du erhältst 1.000 von jedem Mitspieler.", YELLOW, [56, 49], [1]],
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
             ["", "Autounfall! Zahle 6000, wenn du nicht versichert bist.", YELLOW, [62], [28]],
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
             # TODO Choice in White field + change font of text to another color because white on white + Check aktie
             #  and spekulieren an der Börse Spielregel
             ["", "Klage auf Schadenersatz. Dir werden 80.000 zugesprochen", ORANGE, [82], [1]],
             # TODO choice spieler auswählen und geld von ihm nehmen
             ["", "Du erfindest einen automatischen Cocktail-Shaker und erhältst dafür 20.000", YELLOW, [83], [37]],
             ["", "Du gewinnst ein Tennis-Turnier und bekommst 40.000", YELLOW, [84], [27]],
             ["", "Option auf den Kauf eines Status Symbols für 20.000", YELLOW, [85, 92], [38]],
             # TODO choice buy statussymbol
             ["", "Du finanziert eine erfolglose Expedition zum Südpol. Zahle 30.000", YELLOW, [86], [39]],
             ["Zahltag", "", RED, [87], [16]],
             ["", "Wenn du eine Lebensversicherung hast, erhältst du 24.000", YELLOW, [88], [40]],
             ["", "Autounfall! Zahle 18.000, wenn du nicht versichert bist.", YELLOW, [89], [41]],
             ["", "Dein Haus ist renovierungsbedürftig. Gib deine Feuerversicherung zurück.", YELLOW, [90], [42]],
             ["", "Wenn du Aktionär bist, bekommst du 7.000", YELLOW, [91], [43]],
             ["", "Du gewinnst einen Prozess und erhältst 100.000 ", YELLOW, [96], [44]],
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


def save_json(filename):
    fields = []
    for idx, info in enumerate(fieldinfo):
        fields.append({"color": info[2],
                       "following_fields": info[3],
                       "x": WAYPOINTS[idx][0],
                       "y": WAYPOINTS[idx][1],
                       "rotation": WAYPOINTS[idx][2],
                       "action": info[4],
                       "title": info[0],
                       "text": info[1]})

    json_dict = {"fields": fields}
    with open(f"{filename}.json", "w") as outfile:
        json.dump(json_dict, outfile)


save_json("fields")

