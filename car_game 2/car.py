import pygame

dic_of_cars = {"orange": "assets/Car.png"}


class Car:
    def __init__(self, x, y, color):
        self.position = {"x": x, "y": y}
        self.speed = 110
        self.car_asset = pygame.image.load(dic_of_cars[color])

    def move_right(self):
        if not self._collision(self.position["x"] + self.speed):
            self.position["x"] += self.speed

    def move_left(self):
        if not self._collision(self.position["x"] - self.speed):
            self.position["x"] -= self.speed

    def _collision(self, future_place):
        return False

    def draw(self, screen: pygame.display):
        screen.blit(self.car_asset, (self.position["x"], self.position["y"]))