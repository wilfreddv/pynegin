import pygame
from gameLogic import GameLogic

class Engine:
    def __init__(self, gameLogic, window, max_fps):
        self.gameLogic = gameLogic
        self.window = window
        self.max_fps = max_fps

    def run(self):
        self.window.create()
        self.gameloop()

    def gameloop(self):
        clock = pygame.time.Clock()

        while not self.window.shouldStop():
            self.gameLogic.input()
            self.gameLogic.update()
            self.gameLogic.render()

            clock.tick(self.max_fps)
