import pygame
from engine import engine, window
from game import Game

window = window.Window((800,600), "My game")
game = Game(window)
engine = engine.Engine(game, window, max_fps=30)
engine.run()
