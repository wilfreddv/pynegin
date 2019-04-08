import pygame
import pynegin
from game import Game

window = pynegin.Window((800,600), "My game")
game = Game(window)
engine = pynegin.Engine(game, window, max_fps=30)
engine.run()
