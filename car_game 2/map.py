import pygame

class Map:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width_of_car_assets = 110
        self.wall_color = (92, 64, 51)
        self.wall_width = (self.x % self.width_of_car_assets)/ 2
        self.line_color = (40, 40, 123)
        self.line_width = 10

    def draw(self, screen):
        self.draw_road(screen)
        self.draw_side_streets(screen)

    def draw_side_streets(self, screen):

        # Drawing on screen
        pygame.draw.rect(screen, self.wall_color, (0, 0, self.wall_width, self.y))
        pygame.draw.rect(screen, self.wall_color, (self.x-self.wall_width, 0, self.wall_width, self.y))


    def draw_road(self, screen):
        amount_of_roads = self.x // self.width_of_car_assets
        first_line_position = self.width_of_car_assets + self.wall_width
        line = 1

        while line <= amount_of_roads - 2:
            pygame.draw.rect(screen, self.line_color, (first_line_position * (line), 0, self.line_width, self.y))
            line += 1

        # Draw the lines of the roads
        # for road, index in enumerate(range(amount_of_roads)):
        #     print(index)
        #     pygame.draw.rect(screen, self.line_color, (first_line_position * (index + 1), 0, self.line_width, self.y))
