import pygame
import sys
import math

# Spiel-Parameter
SCREEN_SIZE = (1400, 800)
BACKGROUND_COLOR = (0, 0, 0)
WHEEL_RADIUS = 100 #Größe des Rades
WHEEL_POSITION = (1030,380)
WHEEL_ROTATION_SPEED = 5

PLAYER_SIZE = (25,25)
START_POSITION_PLAYER1 = (1170, 350)


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.player = Player(200,200)
        self.board_image = pygame.image.load('spiel des lebens spielbrett.jpg')
        self.board_image = pygame.transform.scale(self.board_image, (1100,800))

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
        #selected_number_surface = self.font.render(str(self.selected_number), True, (0, 0, 0))
        #self.screen.blit(selected_number_surface, WHEEL_POSITION)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    #pygame.quit()
                    #sys.exit()



            self.screen.blit(self.board_image, (300,0))
            self.draw_wheel()
            self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.money = 10000
        self.position = 0
        self.children = []
        self.status_symbols = []
        self.bully_cards = []
        self.income = 0

    # that can be changed
    def draw(self, screen):
        #pygame.draw.circle(screen, PLAYER_COLOR, (self.x, self.y), 50)

        player = pygame.transform.scale(pygame.image.load("car_pink.png"), PLAYER_SIZE)
        screen.blit(player, START_POSITION_PLAYER1)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def change_money(self, amount):
        self.money = self.money + amount

    def payday(self):
        self.money = self.money + self.income


class Field:
    def __init__(self, following_fields, title="", text="") -> None:
        if title == "":
            self.title = None
        else:
            self.title = title
        if text == "":
            self.text = None
        else:
            self.text = text
        #self.following_fields = following_fields  # TODO just a first idea

    def move(self, left_moves):
        return left_moves - 1


class yellow_field(Field):
    def __init__(self) -> None:
        super().__init__()

    def move(self, left_moves):
        left_moves = super().move(self, left_moves)
        if left_moves > 0:
            return
        else:
            # TODO do something
            pass


class orange_field(Field):
    def __init__(self, amount_of_money) -> None:
        super().__init__()
        self.amount_of_money = amount_of_money

    def move(self, left_moves):
        left_moves = super().move(self, left_moves)
        if left_moves > 0:
            return
        else:
            self.text = "Klage auf Schadenersatz. Dir werden " + self.amount_of_money + " zugesprochen."
            # TODO wähle einen anderen spieler
            # TODO ziehe diesem Spieler self.amount_of_money ab und addiere es bei dir


class white_field(Field):
    def __init__(self) -> None:
        super().__init__()

    def move(self, left_moves, wants_to_act):
        left_moves = super().move(self, left_moves)
        if wants_to_act:
            # TODO do what to do
            pass
        else:
            return


class red_field(Field):
    def __init__(self) -> None:
        super().__init__()

    def move(self, left_moves):
        left_moves = super().move(self, left_moves)
        # TODO do what has to be done
        return left_moves


class stop_field(Field):
    def __init__(self) -> None:
        super().__init__()

    def move(self, left_moves):
        left_moves = super().move(self, left_moves)
        # TODO do what has to be done
        return 0


class customs_field(Field):
    def __init__(self) -> None:
        super().__init__()
        self.first_player = False

    def move(self, left_moves):
        left_moves = super().move(self, left_moves)
        if self.first_player:
            # TODO: Add code for the first player's move
            pass
        else:
            # TODO: Add code for the other players' move
            pass


if __name__ == "__main__":
    Game().run()
