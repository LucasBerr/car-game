import pygame
from pygame.locals import QUIT
from pygame import display
from player import Player
from map import Map

class carGame:
    def __init__(self, player:Player, enemys=None, x=600, y=500, map:Map = None):
        self._player = player
        self._enemys = enemys
        self._is_game_on = True
        self._map = map
        self.screen = display.set_mode((x, y))
        pygame.init() # Inicializing pygames
        self._loop()

    # Getters and setters
    @property
    def is_game_on(self):
        return self._is_game_on

    @is_game_on.setter
    def is_game_on(self, value):
        print("Ty to use turn_on() or turn_of to do this")

    @property
    def enemys(self):
        return self._enemys

    @enemys.setter
    def enemys(self, value):
        self._enemys = value

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        if self._is_game_on == True:
            print("You cannot draw a player wille your game is on")
        else:
            self._player = value

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, value):
        self._screen = value

    # Other functions
    def turn_on(self):
        self._is_game_on = True
        self._loop()

    def turn_off(self):
        self._is_game_on = False

    def _loop(self):
        while self._is_game_on:
            self._draw()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                else:
                    if event.type == pygame.KEYDOWN:
                        self._player.movement(event)

            pygame.display.update()

    def _draw(self):
        self.screen.fill((66, 66, 66))
        self._player.draw(self.screen)
        self._map.draw(self.screen)
