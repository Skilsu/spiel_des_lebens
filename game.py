import pygame
import sys

class game:

    def __init__(self) -> None:
        self.players = []
        self.board = []
    
class player:
    
    def __init__(self) -> None:
        self.money = 10000
        self.position = 0
        self.children = []
        self.status_symbols = []
        self.bully_cards = []
        self.income = 0
        
    def change_money(self, amount):
        self.money = self.money + amount
        
    def payday(self):
        self.money = self.money + self.income
        
class field:
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

class yellow_field(field):
    def __init__(self) -> None:
        super().__init__()
    
    def move(self, left_moves):
        left_moves = super().move(self, left_moves)
        if left_moves > 0:
            return
        else:
            # TODO do something
            pass  
        
class orange_field(field):
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
        
class white_field(field):
    def __init__(self) -> None:
        super().__init__()
    
    def move(self, left_moves, wants_to_act):
        left_moves = super().move(self, left_moves)
        if wants_to_act:
            # TODO do what to do
            pass
        else:
            return
        
class red_field(field):
    def __init__(self) -> None:
        super().__init__()
    
    def move(self, left_moves):
        left_moves = super().move(self, left_moves)
        # TODO do what has to be done
        return left_moves
        
class stop_field(field):
    def __init__(self) -> None:
        super().__init__()
        
    def move(self, left_moves):
        left_moves = super().move(self, left_moves)
        # TODO do what has to be done
        return 0

class customs_field(field):
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
