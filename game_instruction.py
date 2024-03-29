import sys
import pygame

from ButtonInterface import TextButton

BLACK = (0, 0, 0)
GREY = (105, 105, 105)
WHITE = (250, 250, 250)
RED = (250, 0, 0)
YELLOW = (255, 255, 0)


class GameInstruction:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen

        # mini darstellung vom spiel
        self.image_mini_game = pygame.image.load("graphics/mini_gameboard.png").convert_alpha()
        self.image_mini_game = pygame.transform.scale(self.image_mini_game, (1000, 400))

        # Zurück Button und vollständige Regeln
        font = pygame.font.SysFont('comicsans', 30)
        self.return_button = TextButton(25, 855, 250, 50, 'Zurück', GREY, BLACK, GREY, RED, font)
        self.full_rules_button = TextButton(1375, 855, 300, 50, 'Vollständige Regeln', GREY, BLACK, GREY, YELLOW, font)
        self.buttons = [self.return_button, self.full_rules_button]

    def redraw_window(self):
        # Hintergrundfarbe
        self.screen.fill(BLACK)

        pygame.draw.line(self.screen, WHITE, (600, 430), (1675, 430))
        pygame.draw.line(self.screen, WHITE, (600, 0), (600, 430))

        # TODO show only when full rules are implemented
        """for btn in self.buttons:
            btn.draw(self.screen)"""
        self.return_button.draw(self.screen)

        self.screen.blit(self.image_mini_game, (650, 25))

        y_offset_top = 15  # Startpunkt für den oberen Anleitungstext
        instructions_top = [
            ("Wie man spielt", ""),
            ("1. Wähle die Spieleranzahl & Fahrzeuge:",
             "Jeder Spieler wählt ein eigenes Auto und bekommt einen eigenes Feld links im Bereich Gesamt Spielerinfo."),
            ("2. Drehen zur Ermittlung der Reihenfolge:",
             "Jeder Spieler dreht das Glücksrad um die Nummer eines jeden Spielers zu ermitteln. Die Reihenfolge richtet sich nach der Höhe der gedrehten Zahl, das heißt der Spieler mit der höchsten Zahl beginnt."),
            ("3. Wahl des Berufsweges:",
             "Direkt am Anfang des Spiels muss entschieden werden, welchen Weg ein Spieler einschlagen will."),
            ("4. Bedeutung der Feldfarben:", ""),
            ("- Gelb:", "Wenn man auf diesem Felder landet, muss den Anweisungen gefolgt werden."),
            ("- Rot:",
             "Wenn ein Spieler auf einem dieser Felder landet oder daran vorbeikommt, muss er die Anweisungen befolgen."),
            ("- Orange:",
             "Wenn man auf einem dieser Felder landet, kann ein beliebiger Gegenspieler über die angezeigte Summe auf \"Schadenersatz\" verklagt werden. Wenn erforderlich, muss dieser sich das Geld von der Bank leihen."),

        ]
        for header, desc in instructions_top:
            y_offset_top = self.render_instruction(header, desc, 15, y_offset_top,
                                                   580)  # 580 ist etwas kleiner als die x-Position Ihrer vertikalen Linie

        y_offset_bottom = 475  # Startpunkt für den unteren Anleitungstext
        instructions_bottom_left = [
            ("- Weiß:",
             "Wenn ein Spieler auf einem dieser Felder landet oder daran vorbeikommt, muss er entscheiden, ob er die dort gebotene Gelegenheit wahrnimmt oder nicht."),
            ("- Stop-Zeichen:",
             "An den Feldern \"Heirat\" und \"Tag der Abrechnung\" muss angehalten werden. Diese Felder müssen nicht mit genauer Augenzahl erreicht werden."),

        ]
        for header, desc in instructions_bottom_left:
            y_offset_bottom = self.render_instruction(header, desc, 625, y_offset_bottom,
                                                      500)  # Nutzt fast die Hälfte des verfügbaren Bereichs für Kapitel 4

        y_offset_bottom_right = 475  # Startpunkt für das rechte untere Anleitungstext
        instructions_bottom_right = [
            ("5. Gewinner des Spiels:",
             "Das Spiel endet, wenn der letzte Spieler entweder den Altersruhesitz oder die Herrschaftliche Villa erreicht hat. Der Spieler mit dem meisten Geld ist der Gewinner des Spiels.")
        ]
        for header, desc in instructions_bottom_right:
            y_offset_bottom_right = self.render_instruction(header, desc, 1150, y_offset_bottom_right,
                                                            500)  # Startet nach Kapitel 4 und nutzt den Rest des Bereichs für Kapitel 5

    def render_instruction(self, header, desc, x_pos, y_offset, max_width):
        header_font = pygame.font.SysFont('comicsans', 22, bold=True)
        header_text = header_font.render(header, True, WHITE)
        self.screen.blit(header_text, (x_pos, y_offset))
        y_offset += header_text.get_height() + 5  # 5 Pixel Abstand

        instruction_font = pygame.font.SysFont('comicsans', 18)
        wrapped_desc = self.wrap_text(desc, instruction_font, max_width)  # Zeilenumbruch nach gegebener max_width
        for line in wrapped_desc:
            desc_text = instruction_font.render(line, True, WHITE)
            self.screen.blit(desc_text, (x_pos, y_offset))
            y_offset += desc_text.get_height() + 5

        return y_offset  # Neuer Y-Offset nach dem Rendern

    def wrap_text(self, text, font, max_width):
        # Teilt den Text in Zeilen auf, sodass jede Zeile die gegebene max_width nicht überschreitet
        words = text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            if font.size(current_line + word)[0] <= max_width:
                current_line += ' ' + word
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        return lines

    def click_event(self, event_pos):
        if self.return_button.rect.collidepoint(event_pos):
            print('Return Button')
            return 'back'
        # TODO show only when full rules are implemented
        """if self.full_rules_button_i.rect.collidepoint(event_pos):
            print('Vollständige Anleitung')"""

    def run(self):
        run = True
        while run:
            self.redraw_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                # handle click-event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    result = self.click_event(event.pos)
                    if result is not None:
                        return result

                # hover over TODO show only when full rules are implemented
                """ for btn in self.buttons:
                    btn.handle_event(event)"""
                self.return_button.handle_event(event)

            pygame.display.update()


if __name__ == "__main__":
    GameInstruction(pygame.display.set_mode((1700, 930))).run()