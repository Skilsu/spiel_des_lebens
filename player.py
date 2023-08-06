import pygame

PLAYER_SIZE_ACTIVE = (25, 40)
PLAYER_SIZE_INACTIVE = (15, 15)


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, rotation, color, name="", active=False):
        super(Player, self).__init__()

        self.name = name
        self.x = x
        self.y = y
        self.rotation = rotation
        self.active = active
        self.color = color
        self.steps_to_go = 0

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
        self.rate = 5

        # game logic
        self.money = 10000
        self.children = []
        self.status_symbols = []
        self.bully_cards = []
        self.insurance = []
        self.depth = 0
        self.income = 0
        self.pause = False

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
            self.rate = 5
            self.moving = False

    def draw(self):
        if self.active:
            self.image = pygame.transform.rotate(self.image_without_rotation, self.rotation)
        else:
            self.image = pygame.Surface(PLAYER_SIZE_INACTIVE, pygame.SRCALPHA)
            pygame.draw.circle(self.image, self.color, (7.5, 7.5), 5)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

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
            self.pause = True
        if action["set income"] != 0:
            self.income = action["set income"]
        if action["go more steps"] != -1:
            self.steps_to_go = action["go more steps"]
        if action.get("add insurance") == "car" and "car" not in self.insurance:
            self.insurance.append("car")
        if action.get("add insurance") == "fire" and "fire" not in self.insurance:
            self.insurance.append("fire")
        if action.get("add insurance") == "live" and "live" not in self.insurance:
            self.insurance.append("live")
        if action.get("lose insurance") == "car" and "car" in self.insurance:
            self.insurance.remove("car")
        if action.get("lose insurance") == "fire" and "fire" in self.insurance:
            self.insurance.remove("fire")
        if action.get("lose insurance") == "live" and "live" in self.insurance:
            self.insurance.remove("live")
        if action["payday"]:
            self.money += self.income
        if action["income if 0"] != 0 and self.income == 0:
            self.income = action["income if 0"]

    def change_money(self, amount):
        self.money = self.money + amount

    def payday(self):
        self.money = self.money + self.income
