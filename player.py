import pygame

PLAYER_SIZE_ACTIVE = (25, 40)
PLAYER_SIZE_INACTIVE = (15, 15)


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, rotation, color, name="", number=-1, active=False):
        super(Player, self).__init__()

        self.name = name
        self.x = x
        self.y = y
        self.rotation = rotation
        self.active = active
        self.color = color
        self.steps_to_go = 0
        self.player_number = number

        image = pygame.image.load("graphics/car.png").convert_alpha()
        self.image_without_rotation = pygame.transform.scale(image, PLAYER_SIZE_ACTIVE).convert_alpha()

        """if self.active:
            self.image = pygame.transform.rotate(self.image_without_rotation, self.rotation)
        else:"""
        self.image = pygame.Surface(PLAYER_SIZE_INACTIVE, pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (7.5, 7.5), 5)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.moving = False

        self.current_field = 0

        self.x_new = x
        self.y_new = y
        self.rotation_new = rotation
        self.rate = 30

        # game logic
        self.money = 0
        self.children = []
        self.status_symbols = []
        self.action_cards = []
        self.car = False
        self.life = False
        self.fire = False
        self.debt = 0
        self.income = 0
        self.pause = False
        self.job = None

    """def update(self, pressed_keys):
            if pressed_keys[pygame.K_SPACE]:
                self.active = True
                self.image = pygame.transform.rotate(self.image_without_rotation, self.rotation)
                print("pressd")"""

    def move(self):
        if self.rate > 1:
            self.rate -= 1
            self.x += (self.x_new - self.x) / self.rate
            self.y += (self.y_new - self.y) / self.rate
            self.rotation += (self.rotation_new - self.rotation) / self.rate
        else:
            self.rate = 30
            self.moving = False

    def draw(self):
        if self.active:
            self.image = pygame.transform.rotate(self.image_without_rotation, self.rotation)
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
        else:
            self.image = pygame.Surface(PLAYER_SIZE_INACTIVE, pygame.SRCALPHA)
            pygame.draw.circle(self.image, self.color, (7.5, 7.5), 5)
            if self.current_field == 0:
                self.rect = self.image.get_rect(topleft=(self.x, self.y))
            elif self.player_number <= 0:
                self.rect = self.image.get_rect(topleft=(self.x, self.y))
            elif self.player_number == 1:
                self.rect = self.image.get_rect(midtop=(self.x, self.y))
            elif self.player_number == 2:
                self.rect = self.image.get_rect(midleft=(self.x, self.y))
            elif self.player_number == 3:
                self.rect = self.image.get_rect(center=(self.x, self.y))
            elif self.player_number == 4:
                self.rect = self.image.get_rect(bottomleft=(self.x, self.y))
            elif self.player_number == 5:
                self.rect = self.image.get_rect(midbottom=(self.x, self.y))

    def act(self, action):
        """
        [{"act with more steps": False,
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
        """
        if action["add_money"] != 0:
            self.money += action["add_money"]
        if action["pause"]:
            self.pause = not self.pause
        if action["set income"] != 0:
            self.income = action["set income"]
        if action["go more steps"] != -1:
            self.steps_to_go = action["go more steps"]
        if action.get("add insurance") == "car":
            self.car = True
        if action.get("add insurance") == "fire":
            self.fire = True
        if action.get("add insurance") == "life":
            self.life = True
        if action.get("lose insurance") == "car":
            self.car = False
        if action.get("lose insurance") == "fire":
            self.fire = False
        if action.get("lose insurance") == "life":
            self.life = False
        if action["payday"]:
            self.money += self.income
        if action["income if 0"] != 0 and self.income == 0:
            self.income = action["income if 0"]
        if self.money < 0:
            self.money += 20000
            self.debt += 1
        if action["job"] is not None:
            self.job = action["job"]

    def change_money(self, amount):
        self.money = self.money + amount

    def payday(self):
        self.money = self.money + self.income
