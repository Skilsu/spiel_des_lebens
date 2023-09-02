import pygame

PLAYER_SIZE_ACTIVE = (25, 40)
PLAYER_SIZE_INACTIVE = (15, 15)

WHITE = (255, 255, 255)
RED = (255, 0, 0)

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

        image = pygame.image.load("graphics/other_cars/car_baby_blue.png").convert_alpha()
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
        self.has_moved = False

        self.choosed_path = False
        self.following_field_number = 0
        self.player_returned = False
        self.has_steps_to_go = False

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
        self.aktie = False

    """def update(self, pressed_keys):
            if pressed_keys[pygame.K_SPACE]:
                self.active = True
                self.image = pygame.transform.rotate(self.image_without_rotation, self.rotation)
                print("pressd")"""

    def __str__(self):  # Not complete
        print(f"{self.name=} \n"
              f"{self.active=} \n"
              f"{self.steps_to_go=} \n"
              f"{self.player_number=} \n\n"
              f"{self.moving=} \n\n"
              f"{self.current_field=} \n\n"
              f"game logic"
              f"{self.money=} \n"
              f"{self.children=} \n"
              f"{self.status_symbols=} \n"
              f"{self.action_cards=} \n"
              f"{self.car=} \n"
              f"{self.life=} \n"
              f"{self.fire=} \n"
              f"{self.debt=} \n"
              f"{self.income=} \n"
              f"{self.pause=} \n"
              f"{self.job=} \n"
              f"{self.aktie=} \n")


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

    def act(self, fields, field): # field = self.fields[current_player.current_field]
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
        "income if 0": 0,
        "job": None,
        "aktie": False
        }]
        """
        """if action["add_money"] != 0:
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
        if action["aktie"]:
            self.aktie = True"""



        if self.moving:
            self.move()
            return 'player_turn'
        else:
            if self.steps_to_go > 0:

                if self.current_field == 0:
                    if not self.player_returned:
                        self.acting(field)
                        self.player_returned = True
                        return 'player_turn'

                if (tuple(field.color) == RED or tuple(field.color) == WHITE) and not self.current_field == 0:

                    if (not self.player_returned) and self.has_moved and not self.has_steps_to_go:
                        self.acting(field)

                        return 'player returning'




                # choice for which path the player will go
                if len(field.following_fields) > 1:
                    if not self.choosed_path:
                        return 'choose_path'
                self.choosed_path = False

                self.player_returned = False

                self.update_position(fields, field)
                print(fields[self.current_field])



                return 'player_turn'
            else:
                if not self.has_steps_to_go:
                    self.acting(field)


                # for more steps to go action # not perfectly tested for later on
                if self.steps_to_go > 0:
                    self.has_steps_to_go = True
                    return 'player returning'
        return 'next_player'
    def acting(self, field):
        actions = field.get_actions()
        for action in actions:
            action.act(self)

    def move(self):
        if self.rate > 1:
            self.rate -= 1
            self.x += (self.x_new - self.x) / self.rate
            self.y += (self.y_new - self.y) / self.rate
            self.rotation += (self.rotation_new - self.rotation) / self.rate
        else:
            self.rate = 30
            self.moving = False



    def update_position(self, fields, field):
        self.has_moved = True
        self.steps_to_go -= 1
        self.moving = True

        following_field_number = field.get_following_field(self.following_field_number)
        self.following_field_number = 0
        following_field = fields[following_field_number]


        self.x_new = following_field.x
        self.y_new = following_field.y

        rotation_new = following_field.rotation
        if self.rotation > 180:
            rotation_modified = rotation_new + 360
            diff = abs(self.rotation - rotation_modified)
        else:
            rotation_modified = rotation_new - 360
            diff = abs(self.rotation - rotation_modified)

        if diff < abs(rotation_new - self.rotation):
            rotation_new = rotation_modified
        self.rotation_new = rotation_new

        self.current_field = following_field_number


    def check_choose_path(self, clicked_object):
        if clicked_object == 'Links':
            print('Links')
            self.choosed_path = True
            self.following_field_number = 0
            return True
        elif clicked_object == 'Rechts':
            print('Rechts')
            self.choosed_path = True
            self.following_field_number = 1
            return True
        return False