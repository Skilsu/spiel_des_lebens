import pygame.display

from main_menu import MainMenu
from game import Game
from pause_menu import PauseMenu
from game_intro_choose_player import GameIntro as GameIntroChoosePlayer
from game_intro_order_decision import GameIntro as GameIntroOrderDecision
from game_instruction import GameInstruction

SCREEN_SIZE = (1700, 930)


class GameState:
    def __init__(self):
        self.state = 'main_menu'

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Game of Life')
        self.main_menu = MainMenu(self.screen)
        self.game = Game(self.screen)
        self.pause_menu = PauseMenu(self.screen)
        self.game_intro_choose_player = GameIntroChoosePlayer(self.screen)
        self.game_intro_order_decision = GameIntroOrderDecision(self.screen)
        self.game_instruction = GameInstruction(self.screen)

        self.previous_state = None

    def event_handler(self):
        if self.state == 'main_menu':
            self.previous_state = self.state
            self.state = self.main_menu.run()
        elif self.state == 'game_intro_choose_player':
            self.previous_state = self.state
            self.state = self.game_intro_choose_player.run()
            self.game_intro_order_decision.append_players_data(self.game_intro_choose_player.selected_cars)
        elif self.state == 'game_intro_order_decision':
            self.previous_state = self.state
            self.state = self.game_intro_order_decision.run()
        elif self.state == 'game_playing':
            self.previous_state = self.state
            self.state = self.game.run()
        elif self.state == 'game_pausing':
            self.state = self.pause_menu.run()
            if self.state == 'resume':
                self.state = self.previous_state
            if self.state == "restart_game":
                self.__init__()
        elif self.state == 'instruction':
            self.state = self.game_instruction.run()
            if self.state == 'back':
                self.state = self.previous_state


game_state = GameState()

while True:
    game_state.event_handler()
