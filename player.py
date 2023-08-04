import pygame

PLAYER_SIZE = (25, 40)

class Player(pygame.sprite.Sprite):

    def __init__(self, waypoints, color, start_waypoint=0, active=False):
        super(Player, self).__init__()
        self.waypoints = waypoints
        self.current_waypoint = start_waypoint
        self.position = self.waypoints[start_waypoint][:2]
        self.rotation = self.waypoints[start_waypoint][2]
        self.color = color
        self.active = active

        self.moved = False


        self.money = 10000
        self.children = []
        self.status_symbols = []
        self.bully_cards = []
        self.income = 0


    # that can be changed
    def draw(self, screen):
        # pygame.draw.circle(screen, PLAYER_COLOR, (self.x, self.y), 50)
        if self.active:
            player = pygame.transform.scale(pygame.image.load("graphics/car.png"), PLAYER_SIZE).convert_alpha()
            player = pygame.transform.rotate(player, self.rotation)
            screen.blit(player, self.position)
        else:
            player = pygame.draw.circle(surface=screen, center=self.position, radius=5, color=self.color)

    def move(self, random_number_from_wheel):
        next_waypoint = self.current_waypoint + random_number_from_wheel
        if next_waypoint >= len(self.waypoints):
            next_waypoint = len(self.waypoints) -1 # Ende des Spiels erreicht
        self.position = self.waypoints[next_waypoint][:2]
        self.rotation = self.waypoints[next_waypoint][2]
        self.current_waypoint = next_waypoint


    def change_money(self, amount):
        self.money = self.money + amount

    def payday(self):
        self.money = self.money + self.income