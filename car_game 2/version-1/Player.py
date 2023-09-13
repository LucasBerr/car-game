import pygame
from mapaa import Map

class Car:
    def __init__(self, x, y, map:Map, display):
        # Spawn do carro
        self.x = x
        self.y = y
        self.position = {"x":20,"y":y/2}
        self.road = map.get_road()
        self.walls = Walls(x, y, display)

        self.car_asset = pygame.transform.scale(pygame.image.load('../assets/Car.png'), (50, 95))


    def car_draw(self, display):
        display.blit(self.car_asset, (self.position["x"], self.position["y"]))

    def on_event(self, event):

        if event.key == pygame.K_a:
            if not self.colisao(self.position["x"] - 30):
                self.position["x"] -= 30


        elif event.key == pygame.K_d:
            # prevenindo parede direita
            if not self.colisao(self.position["x"] + 30):
                self.position["x"] += 30



    def colisao(self, posicao_futura):
        if self.walls.bateu_parede(posicao_futura):
            print(self.position)
            return True
        #if bate_carro():

    #def walls(self):


# # Creating enemies
# class Enemy:
#     def __init__(self):
#         ...

# Creating walls
class Walls:
    def __init__(self, x, y, display):
        self.x = x
        self.y = y
        self.color_parede = (92,64,51)
        self.parede_esquerda = (0, 0, 20, self.y)
        self.parede_direita = (self.x-20, 0, self.x, self.y)
        self.construir_parede(display)


    def construir_parede(self, display):
        # Desenhando parede esquerda
        pygame.draw.rect(display, self.color_parede, self.parede_esquerda)
        # Desenhando parede direita
        pygame.draw.rect(display, self.color_parede, self.parede_direita)

    def bateu_parede(self, posicao_futura):
        if posicao_futura <= self.parede_esquerda[2]:
            return True
        if posicao_futura >= self.parede_direita[0] - 50:
            return True
        else:
            return False