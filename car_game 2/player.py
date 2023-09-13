import pygame
from car import Car


class Player(Car):
    def __init__(self, x, y, color):
        width_of_car_assets = 99
        initial_position_x = (x % width_of_car_assets) / 2
        initial_position_y = (y / 2)
        super().__init__(initial_position_x, initial_position_y, color)

    def movement(self, event):
        if event.key == pygame.K_a:
            super().move_left()

        elif event.key == pygame.K_d:
            super().move_right()
