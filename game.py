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

class Lines(component.Component):
    def __init__(self, container):
        self.lines = []
        self.lines.append(line.Line(container, (10,10), (container.getWidth()-10, 10), 10, COLORS.GREEN))
        self.lines.append(line.Line(container, (container.getWidth()-10,10), (container.getWidth()-10, container.getHeight()-10), 10, COLORS.WHITE))
        self.lines.append(line.Line(container, (10,10), (10, container.getHeight()-10), 10, COLORS.BLUE))
        self.lines.append(line.Line(container, (10,container.getHeight()-10), (container.getWidth()-10, container.getHeight()-10), 10, COLORS.RED))
        size = container.getWidth(), container.getHeight()
        surface = Surface(size)
        super().__init__(container, surface=surface, size=size)

    def show(self, surf):
        for line in self.lines:
            line.show(surf)


class Game(GameLogic):
    def __init__(self, window):

        self.textField = inputField.InputField(window, textSize=30, color=COLORS.WHITE)
        self.t = text.Text(window, text="Hello!", textSize=50, color=COLORS.WHITE)
        ctx = Lines(window)

        super().__init__(window, ctx)


    def input(self):
        #self.textField.updateInput(self.window.getPressedKeys())

        ...
