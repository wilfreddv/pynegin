import pygame
from engine import engine, window
from gameLogic import GameLogic

window = window.Window((800,600), "My game")
gameLogic = GameLogic(window)
engine = engine.Engine(gameLogic, window, max_fps=30)
engine.run()
