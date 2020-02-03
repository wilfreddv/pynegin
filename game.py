from pynegin.components import text, menu, image, sprite, inputField, line, component
from pynegin.constants.colors import COLORS
from pynegin.gameLogic import GameLogic
import pygame
from pygame import Surface


class MainMenu(menu.Menu):
    def __init__(self, *args, onQuit=None, bg=None, **kwargs):
        super().__init__(*args, background=bg, **kwargs)

        self.addChild(text.Text(self, text="Hello World!", textSize=50, color=COLORS.BLACK, onActivate=lambda: print("Hello")))
        self.addChild(text.Text(self, text="FooBar", y=40, textSize=50, color=COLORS.BLACK))
        self.addChild(text.Text(self, text="QUIT", y=120, textSize=50, color=COLORS.BLACK, onActivate=onQuit))

        for child in self.children:
            child.centerHorizontal()

        self.K_NEXT = pygame.K_s
        self.K_PREV = pygame.K_w
        self.centerHorizontal()


class Game(GameLogic):
    def __init__(self, window):
        self.menu = MainMenu(window, size=window.size, backgroundColor=COLORS.BLUE, onQuit=self.quit)

        self.window = window
        self.context = self.menu


    def input(self):
        self.menu.handleSelection(self.window)
        self.menu.handleActivation(self.window)
