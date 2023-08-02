import pygame
import sys
import math
import random
from player import Player

# from field import ... Import hier Felder

# Spiel-Parameter
BACKGROUND_COLOR = (0, 0, 0)
WHEEL_RADIUS = 100  # Größe des Rades
WHEEL_POSITION = (1030, 380)
WHEEL_ROTATION_SPEED = 5


START_POSITION_PLAYER1 = (1170, 350)
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
               (660, 652, 26)]


class Game:

    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        #self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.player = []
        """self.player.append(Player(1170, 360, (0, 212, 28)))
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
        self.player.append(Player(1185, 411, (0, 68, 220)))"""
        for point in WAYPOINTS:
            self.player.append(Player(point[0], point[1], (255, 0, 255), rotation=point[2], active=True))
        self.board_image = pygame.image.load('graphics/spiel des lebens spielbrett.jpg').convert()
        self.board_image = pygame.transform.scale(self.board_image, (1100, 800))

        self.font = pygame.font.Font(None, 30)
        self.wheel_angle = 0
        self.selected_number = 0

    def get_color(self, number):
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
        return colors[number % len(colors)]

    def spin_wheel(self):
        return random.randint(1, 10)

    def draw_wheel(self):
        for i in range(10):
            angle_start = math.radians(self.wheel_angle + i * 360 / 10)
            angle_end = math.radians(self.wheel_angle + (i + 1) * 360 / 10)
            color = self.get_color(i)
            pygame.draw.arc(self.screen, color,
                            pygame.Rect(WHEEL_POSITION[0] - WHEEL_RADIUS, WHEEL_POSITION[1] - WHEEL_RADIUS,
                                        2 * WHEEL_RADIUS, 2 * WHEEL_RADIUS), angle_start, angle_end, WHEEL_RADIUS)

        for i in range(10):
            angle = math.radians(self.wheel_angle + i * 360 / 10)
            start_pos = (
                WHEEL_POSITION[0] + WHEEL_RADIUS * math.cos(angle),
                WHEEL_POSITION[1] + WHEEL_RADIUS * math.sin(angle)
            )
            end_pos = (
                WHEEL_POSITION[0] + WHEEL_RADIUS * 0.9 * math.cos(angle),
                WHEEL_POSITION[1] + WHEEL_RADIUS * 0.9 * math.sin(angle)
            )
            pygame.draw.line(self.screen, (255, 255, 255), start_pos, end_pos, 2)
            number_surface = self.font.render(str(i + 1), True, (0, 0, 0))
            number_pos = (
                WHEEL_POSITION[0] + WHEEL_RADIUS * 0.8 * math.cos(angle),
                WHEEL_POSITION[1] + WHEEL_RADIUS * 0.8 * math.sin(angle)
            )
            self.screen.blit(number_surface, number_pos)
        # selected_number_surface = self.font.render(str(self.selected_number), True, (0, 0, 0))
        # self.screen.blit(selected_number_surface, WHEEL_POSITION)

    def run(self):
        running = True
        rate = 15
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        return 'game_pausing'

            self.player[0].y_new = 257
            self.player[0].x_new = 1237
            self.player[0].rotation_new = 360
            
            if rate > 1:
                rate -= 1
                self.player[0].move(rate)
            self.screen.blit(self.board_image, (300, 0))
            self.draw_wheel()
            
            for player in self.player:
                player.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    Game(pygame.display.set_mode((1400, 800))).run()
