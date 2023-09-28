import pygame

from actions import ChoiceInFieldAction

PLAYER_SIZE_ACTIVE = (25, 40)
PLAYER_SIZE_INACTIVE = (15, 15)

WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Player:

    def __init__(self, x, y, rotation, color, car_image, name="", number=-1, active=False):
        self.name = name
        self.x = x
        self.y = y
        self.rotation = rotation
        self.active = active
        self.color = color
        self.steps_to_go = 0
        self.player_number = number

        self.image_without_rotation = pygame.transform.scale(car_image, PLAYER_SIZE_ACTIVE).convert_alpha()

        self.image = pygame.Surface(PLAYER_SIZE_INACTIVE, pygame.SRCALPHA)
        #pygame.draw.circle(self.image, self.color, (7.5, 7.5), 5) doesnt need it?
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.is_moving = False

        self.current_field_number = 0

        self.x_following_field = x
        self.y_following_field = y
        self.rotation_following_field = rotation
        self.moving_rate = 30
        self.has_moved = False

        self.choosed_path = False
        self.following_field_number = 0
        self.player_returned = False
        self.has_steps_to_go = False

        self.choosing_in_field = False
        self.choice_in_field_checked = False
        self.choice_in_field_checked_goon = False

        # game logic
        self.money = 0
        self.children = 0
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
        self.married = False

    def __str__(self):  # Not complete
        print(f"{self.name=} \n"
              f"{self.active=} \n"
              f"{self.steps_to_go=} \n"
              f"{self.player_number=} \n\n"
              f"{self.is_moving=} \n\n"
              f"{self.current_field_number=} \n\n"
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
              
              f"{self.aktie=} \n")

    def draw(self):
        if self.active:
            self.image = pygame.transform.rotate(self.image_without_rotation, self.rotation)
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
        else:
            self.image = pygame.Surface(PLAYER_SIZE_INACTIVE, pygame.SRCALPHA)
            pygame.draw.circle(self.image, self.color, (7.5, 7.5), 5)
            if self.current_field_number == 0:
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

        if self.is_moving:
            self.move()
            return 'player_turn'
        else:
            # Marriage field
            if self.current_field_number == 25:
                if not self.married:
                    self.married = True
                    return 'marriage_action'

            if self.steps_to_go > 0:

                if self.current_field_number == 0:
                    if not self.player_returned:
                        self.acting(field)
                        self.player_returned = True
                        return 'player_turn'

                if (tuple(field.color) == RED or tuple(field.color) == WHITE) and not self.current_field_number == 0:

                    if self.current_field_number == 15:
                        self.has_steps_to_go = False

                    if ((not self.player_returned) and self.has_moved and not self.has_steps_to_go):


                        self.acting(field)

                        # choice in field
                        if not self.choice_in_field_checked and not self.choice_in_field_checked_goon:
                            if self.choosing_in_field:
                                return 'choose_in_field'



                        return 'player returning'


                # choice for which path the player will go
                if len(field.following_fields) > 1:
                    if not self.choosed_path:
                        return 'choose_path'
                self.choosed_path = False

                self.player_returned = False

                self.update_position(fields, field)
                print(fields[self.current_field_number])



                return 'player_turn'

            else:
                if not self.has_steps_to_go or self.current_field_number == 15: # Zahltag
                    self.acting(field)

                    # choice in field
                    if not self.choice_in_field_checked and not self.choice_in_field_checked_goon:
                        if self.choosing_in_field:
                            return 'choose_in_field'



                # for more steps to go action
                if self.steps_to_go > 0:
                    self.has_steps_to_go = True
                    return 'player returning'

        self.choosing_in_field = False
        return 'next_player'

    def acting(self, field):
        actions = field.get_actions()
        for action in actions:
            action.act(self)
            if isinstance(action, ChoiceInFieldAction):
                if not self.choice_in_field_checked_goon:
                    break

    def add_money(self, money):
        self.money += money
        # check money here as well, because MoneyAction can subtract money too
        self.check_money()

    def subtract_money(self, money):
        self.money -= money
        self.check_money()

    def check_money(self):
        if self.money < 0:
            self.money += 20000
            self.debt += 1

    def move(self):
        if self.moving_rate > 1:
            self.moving_rate -= 1
            self.x += (self.x_following_field - self.x) / self.moving_rate
            self.y += (self.y_following_field - self.y) / self.moving_rate
            self.rotation += (self.rotation_following_field - self.rotation) / self.moving_rate
        else:
            self.moving_rate = 30
            self.is_moving = False

    def update_position(self, fields, field):
        self.has_moved = True
        self.steps_to_go -= 1
        self.is_moving = True

        following_field_number = field.get_following_field(self.following_field_number)
        self.following_field_number = 0
        following_field = fields[following_field_number]


        self.x_following_field = following_field.x
        self.y_following_field = following_field.y

        rotation_new = following_field.rotation
        if self.rotation > 180:
            rotation_modified = rotation_new + 360
            diff = abs(self.rotation - rotation_modified)
        else:
            rotation_modified = rotation_new - 360
            diff = abs(self.rotation - rotation_modified)

        if diff < abs(rotation_new - self.rotation):
            rotation_new = rotation_modified
        self.rotation_following_field = rotation_new

        self.current_field_number = following_field_number

    def check_choose_path(self, clicked_object):
        # no other option to check path and choice in field
        if self.choosing_in_field:
            if clicked_object == 'Links':
                print('Ja')
                self.choosing_in_field = False
                self.choice_in_field_checked_goon = True
                return True
            elif clicked_object == 'Rechts':
                print('Nein')
                self.choosing_in_field = False
                self.choice_in_field_checked = True
                return True
        else:
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


