import pygame

PLAYER_SIZE = (25, 40)


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, color, rotation=270, active=False):

        # general attributes
        self.active = active
        self.color = color

        # pygame attributes
        self.x = x
        self.y = y
        self.x_new = x
        self.y_new = y
        self.rotation = rotation
        self.rotation_new = rotation
        self.rate = 15

        # game logic
        self.money = 10000
        self.children = []
        self.status_symbols = []
        self.bully_cards = []
        self.income = 0

    # that can be changed
    def draw(self, screen):
        # pygame.draw.circle(screen, PLAYER_COLOR, (self.x, self.y), 50)
        if self.active:
            player = pygame.transform.scale(pygame.image.load("graphics/car.png"), PLAYER_SIZE).convert_alpha()
            player = pygame.transform.rotate(player, self.rotation)
            screen.blit(player, (self.x, self.y))
        else:
            player = pygame.draw.circle(surface=screen, center=(self.x, self.y), radius=5, color=self.color)

    def move(self):
        if self.rate > 1:
            self.rate -= 1
            self.x += (self.x_new - self.x) / self.rate
            self.y += (self.y_new - self.y) / self.rate
            self.rotation += (self.rotation_new - self.rotation) / self.rate
        else:
            self.rate = 15

    def change_money(self, amount):
        self.money = self.money + amount

    def payday(self):
        self.money = self.money + self.income
