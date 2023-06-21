import pygame
import sys

# Spiel-Parameter
SCREEN_SIZE = (800, 600)
BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 0, 255)

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.player = Player(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(BACKGROUND_COLOR)
            self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
    
class Player:
    
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
        pygame.draw.circle(screen, PLAYER_COLOR, (self.x, self.y), 50)

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
        self.following_fields = following_fields  # TODO just a first idea
        
            
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