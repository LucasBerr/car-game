import time
import pygame
import keyboard


class Map:
    def __init__(self):
        self.streetLeft = "\t\t\tx"
        self.streetMiddle = "|"
        self.streetRight = "x"
        self.blanckSpaces = "  "

        self.interact = [["  ", "🚗", "🚙"], ["  ", "🚗", "🚙"], ["  ", "🚗", "🚙"], ["  ", "🚗", "🚙"]]
        self.isPlayerHere = 0

        # x       |   🚗  x

        self.window = 20

    def construct_street(self):
        for i in range(self.window):
            print(
                self.streetLeft + self.interact[0][0] + self.interact[1][0] + self.streetMiddle + self.interact[2][0] +
                self.interact[3][0] + self.streetRight)

    # I need to find a way to don't use so many ifs inside here
    def construct_street_with_player(self):

        for i in range(self.window):
            if i != (self.window / 2):
                print(
                    self.streetLeft + self.interact[0][0] + self.interact[1][0] + self.streetMiddle + self.interact[2][
                        0] + self.interact[3][0] + self.streetRight)
            else:
                if self.isPlayerHere == 0:
                    print(
                        self.streetLeft + self.interact[0][1] + self.interact[1][0] + self.streetMiddle +
                        self.interact[2][
                            0] + self.interact[3][0] + self.streetRight)
                elif self.isPlayerHere == 1:
                    print(
                        self.streetLeft + self.interact[0][0] + self.interact[1][1] + self.streetMiddle +
                        self.interact[2][
                            0] + self.interact[3][0] + self.streetRight)
                elif self.isPlayerHere == 2:
                    print(
                        self.streetLeft + self.interact[0][0] + self.interact[1][0] + self.streetMiddle +
                        self.interact[2][
                            1] + self.interact[3][0] + self.streetRight)
                elif self.isPlayerHere == 3:
                    print(
                        self.streetLeft + self.interact[0][0] + self.interact[1][0] + self.streetMiddle +
                        self.interact[2][
                            0] + self.interact[3][1] + self.streetRight)

    def move_right(self):
        if not self.isPlayerHere >= 3:
            self.isPlayerHere += 1

    def move_left(self):
        if not self.isPlayerHere <= 0:
            self.isPlayerHere -= 1

class Game:

    def start_game(self, map: Map):
        while not keyboard.is_pressed("esc"):
            map.construct_street_with_player()
            time.sleep(0.036)

if __name__ == "__main__":
    mapa = Map()
    car_game = Game()

    keyboard.add_hotkey("d", mapa.move_right())
    keyboard.add_hotkey("a", mapa.move_left())
    car_game.start_game(mapa)
