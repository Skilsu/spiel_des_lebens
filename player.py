import pygame

PLAYER_SIZE_ACTIVE = (25, 40)
PLAYER_SIZE_INACTIVE = (15, 15)

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, rotation, color, active=False):
        super(Player, self).__init__()

        self.x = x
        self.y = y
        self.rotation = rotation
        self.active = active
        self.color = color

        image = pygame.image.load("graphics/car.png").convert_alpha()
        self.image_without_rotation = pygame.transform.scale(image, PLAYER_SIZE_ACTIVE).convert_alpha()

        """if self.active:
            self.image = pygame.transform.rotate(self.image_without_rotation, self.rotation)
        else:"""
        self.image = pygame.Surface(PLAYER_SIZE_INACTIVE, pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (7.5, 7.5), 5)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.moving = False

        self.current_waypoint = 0
        """
        self.x_new = x
        self.y_new = y
        self.rotation_new = rotation

        self.rate = 0
        self.moved = False

        self.money = 10000
        self.children = []
        self.status_symbols = []
        self.bully_cards = []
        self.income = 0"""

    """def update(self, pressed_keys):
        if pressed_keys[pygame.K_SPACE]:
            self.active = True
            self.image = pygame.transform.rotate(self.image_without_rotation, self.rotation)
            print("pressd")"""

    def update(self, x=0, y=0, rotation=0):
        if not self.moving:
            self.image = pygame.transform.rotate(self.image_without_rotation, self.rotation)
        else:
            self.x = x
            self.y = y
            self.rotation = rotation
            #self.image = pygame.transform.rotate(self.image_without_rotation, rotation)
            #self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self):
        if self.active:
            self.image = pygame.transform.rotate(self.image_without_rotation, self.rotation)
        else:
            self.image = pygame.Surface(PLAYER_SIZE_INACTIVE, pygame.SRCALPHA)
            pygame.draw.circle(self.image, self.color, (7.5, 7.5), 5)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))




    def change_money(self, amount):
        self.money = self.money + amount

    def payday(self):
        self.money = self.money + self.income