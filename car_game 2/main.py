from game import carGame
from car import Car
from player import Player
from map import Map


def main():
    width = 1280
    height = 720

    map = Map(width, height)
    player = Player(width, height, color="orange")
    game = carGame(x=width, y=height, player=player, map=map)


if __name__ == "__main__":
    main()