from abc import ABC, abstractmethod

import pygame
from pygame.locals import *


class ButtonInterface(ABC):
    def __init__(self, x, y, width, height, bg_color, hover_color, active_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.active_color = active_color
        self.active = False
        self.hovered = False

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass


class TextButton(ButtonInterface):
    def __init__(self, x, y, width, height, text, bg_color, txt_color, active_color, hover_color, font):
        super().__init__(x, y, width, height, bg_color, hover_color, active_color)
        self.text = font.render(text, True, txt_color)

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


class ImageButton(ButtonInterface):
    def __init__(self, x, y, width, height, image_path, bg_color, hover_color, active_color, border_color=(0, 0, 0),
                 border_size=10):
        super().__init__(x, y, width, height, bg_color, hover_color, active_color)

        self.image_rect = pygame.Rect(x + border_size, y + border_size, width - 2 * border_size,
                                      height - 2 * border_size)

        self.image = pygame.image.load(image_path).convert_alpha()  # Lädt das Bild
        self.image = pygame.transform.scale(self.image, (
        self.image_rect.width, self.image_rect.height)).convert_alpha()  # Skaliert das Bild auf die Größe innerhalb des Rahmens

        self.border_color = border_color
        self.player_number = None
        self.font = pygame.font.SysFont("comicsans", 48)

    def draw(self, screen):
        color = self.hover_color if self.hovered else self.active_color if self.active else self.bg_color
        pygame.draw.rect(screen, color, self.rect)  # Hintergrundrechteck
        pygame.draw.rect(screen, self.border_color, self.rect, 2)  # Rahmen
        screen.blit(self.image, self.image_rect.topleft)  # Zeichnet das Bild innerhalb des Rahmens

        if self.player_number is not None:
            num_text = self.font.render(str(self.player_number), True, (250, 250, 250))
            num_pos = (self.rect.x + (self.rect.width - num_text.get_width()) // 2,
                       self.rect.y - num_text.get_height())
            screen.blit(num_text, num_pos)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True
        elif event.type == MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hovered = not self.active  # Hover nur, wenn der Button nicht aktiv ist
            else:
                self.hovered = False
        return False