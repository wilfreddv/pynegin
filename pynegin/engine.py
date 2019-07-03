import pygame
import os
import time


now = lambda: time.time() * 1000


class Engine:
    def __init__(self, gameLogic, window, max_fps=30, max_tps=300):
        """
        max_fps: max frame blitting rate
        max_tps: max state update rate
        """
        self.gameLogic = gameLogic
        self.window = window
        self.max_fps = max_fps
        self.max_tps = max_tps

    def run(self):
        self.window.create()
        self.gameloop()

    def gameloop(self):
        ms_per_frame = 1000 / self.max_fps
        ms_per_tick = 1000 / self.max_tps
        frame_delay = tick_delay = 0
        last = now()

        while not self.window.shouldStop():
            if tick_delay <= 0:
                tick_delay = ms_per_tick
                self.gameLogic.input()
                self.gameLogic.update()

            if frame_delay <= 0:
                frame_delay = ms_per_frame
                self.gameLogic.render()

            delta = now() - last
            frame_delay -= delta
            tick_delay -= delta
            last = now()
