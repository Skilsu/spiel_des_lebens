import sys
import pygame
from pygame.locals import *
from wheel import Wheel

WHEEL_RADIUS = 250  # Größe des Rades
WHITE = (255, 255, 255)

# for Wheel
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

car_colors = {
    'baby_blue':  (173, 216, 230),
    'green':  (0, 255, 0),
    'orange':  (255, 165, 0),
    'purple':  (128, 0, 128),
    'red':  (255, 0, 0),
    'yellow':  (255, 219, 0)
}




class GameIntro:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen

        self.font = pygame.font.Font(None, 35)
        font_large = pygame.font.Font(None, 70)
        self.wheel = Wheel((self.screen.get_width()/2, self.screen.get_height()/2), WHEEL_RADIUS, colors, self.font, font_large)
        self.clock = pygame.time.Clock()
        self.players_data = []
        self.players_data = [(1, (173, 216, 230)), (2, (0, 255, 0)), (3, (255, 165, 0)), (4, (128, 0, 128)), (5, (255, 0, 0)),
                             (6, (255, 219, 0))] # debug zwecke
        self.players_data = [{'player_number': num, 'car_color': color} for num, color in self.players_data]
        image_directory = 'graphics/other_cars/'

        for player in self.players_data:
            color_name = [name for name, rgb in car_colors.items() if rgb == player["car_color"]][0]
            car_image_path = image_directory + "car_" + color_name + ".png"
            player["car_image"] = pygame.image.load(car_image_path).convert_alpha()
            player["car_image"] = pygame.transform.scale(player["car_image"], (80, 80))
        print(self.players_data)


    def draw_player_infos(self):

        for i, player in enumerate(self.players_data):
            # Draw the rectangle
            pygame.draw.rect(self.screen, player['car_color'], (5, 5 + 800 * i / len(self.players_data), 290, 120))

            # Render the text
            name_surface = self.font.render(f"Spieler: {player['player_number']}", True, WHITE)
            self.screen.blit(name_surface, (10, 10 + 800 * i / len(self.players_data)))


            self.screen.blit(player["car_image"], (200, 10 + 800 * i / len(self.players_data)))


    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return 'game_pausing'
                    if event.key == K_SPACE:

                        self.wheel.spin()

            self.wheel.update()
            self.screen.fill((0, 0, 0))
            self.draw_player_infos()
            self.wheel.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    GameIntro(pygame.display.set_mode((1700, 930))).run()



