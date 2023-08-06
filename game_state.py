import pygame.display

from main_menu import MainMenu
from game import Game
from pause_menu import PauseMenu

SCREEN_SIZE = (1700, 930)


class GameState:
    def __init__(self):
        self.state = 'main_menu'
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.main_menu = MainMenu(self.screen)
        self.game = Game(self.screen)
        self.pause_menu = PauseMenu(self.screen)

    def event_handler(self):
        if self.state == 'main_menu':
            self.state = self.main_menu.run()
        elif self.state == 'game_playing':
            self.state = self.game.run()
        elif self.state == 'game_pausing':
            self.state = self.pause_menu.run()


game_state = GameState()

while True:
    game_state.event_handler()
