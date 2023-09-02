import pygame
import random
import math


class Wheel:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
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
        self.font = pygame.font.Font(None, 35)
        self.font_large = pygame.font.Font(None, 70)
        self.angle = 0
        self.target_angle = 0
        self.is_spinning = False
        self.selected_number = random.randint(1, 10)
        self.has_spun = False

    def draw_sector(self, n, screen):
        start_angle = (n * 36 + self.angle) % 360
        end_angle = ((n + 1) * 36 + self.angle) % 360
        if start_angle > end_angle:
            end_angle += 360

        points = [self.center]
        for a in range(start_angle, end_angle + 1, 5):
            x = self.center[0] + self.radius * math.cos(math.radians(a))
            y = self.center[1] + self.radius * math.sin(math.radians(a))
            points.append((x, y))
        pygame.draw.polygon(screen, self.colors[n], points)

        text_angle = (start_angle + end_angle) / 2
        text_x = self.center[0] + (self.radius * 0.65) * math.cos(math.radians(text_angle)) - 10
        text_y = self.center[1] + (self.radius * 0.65) * math.sin(math.radians(text_angle)) - 10
        text = self.font.render(str(n + 1), True, (0, 0, 0))
        screen.blit(text, (text_x, text_y))

    def draw_selected_number(self, screen):
        if not self.is_spinning and self.has_spun:
            text = self.font_large.render(str(self.selected_number), True, (0, 0, 0))
            screen.blit(text, (self.center[0] - text.get_width() // 2, self.center[1] - text.get_height() // 2))

    def draw_pointer(self, screen):
        pointer_position = (self.center[0] + self.radius - 20, self.center[1])
        pygame.draw.polygon(screen, (255, 255, 255),
                            [pointer_position, (pointer_position[0] + 30, pointer_position[1] - 15),
                             (pointer_position[0] + 30, pointer_position[1] + 15)])

    def draw(self, screen):
        for i in range(10):
            self.draw_sector(i, screen)
        self.draw_selected_number(screen)
        self.draw_pointer(screen)

    def spin(self):
        if not self.is_spinning:
            self.target_angle = self.angle + random.randint(360, 720)
            self.is_spinning = True
            self.has_spun = True

    def update(self):
        if self.is_spinning:
            if self.angle < self.target_angle:
                self.angle += 10
            else:
                self.is_spinning = False

        if not self.is_spinning and self.has_spun:
            self.selected_number = 1 + ((-self.angle // 36) % 10)

    def get_selected_number(self):
        return self.selected_number  # TODO hier ändern self.selected_number

    def has_stopped(self):
        return not self.is_spinning and self.has_spun
