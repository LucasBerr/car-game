import pygame

class Map:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color_parede = (92,64,51)

    def draw_map(self, display):
        # Rua principal
        display.fill((66,66,66))

    def get_road(self):
        return {"x_inicio":self.x/3, "y_inicio": 0, "x_fim":self.x/3, "y_fim":self.y}


