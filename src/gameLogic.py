from engine.components import textComponent, menuComponent
from engine.constants.colors import COLORS
import pygame

class GameLogic:
    def __init__(self, window):
        self.window = window

        self.menu = menuComponent.MenuComponent(window, size=(500, window.getHeight()), backgroundColor=COLORS.BLUE)
        myText = textComponent.TextComponent(self.menu, text="Hello World!", textSize=50, color=COLORS.BLACK)
        myText2 = textComponent.TextComponent(self.menu, text="FooBar", y=40, textSize=50, color=COLORS.BLACK)
        myText3 = textComponent.TextComponent(self.menu, text="BazQux", y=80, textSize=50, color=COLORS.BLACK)
        myText.centerHorizontal()
        myText2.centerHorizontal()
        myText3.centerHorizontal()
        myText.activate = lambda: print("1")
        myText2.activate = lambda: print("2")
        myText3.activate = lambda: print("3")
        self.menu.addChildren(myText, myText2, myText3)
        self.menu.K_NEXT = pygame.K_s
        self.menu.K_PREV = pygame.K_w
        self.menu.centerHorizontal()

    def update(self):
        self.window.update()

    def input(self):
        self.menu.handleSelection(self.window)
        self.menu.handleActivation(self.window)

    def render(self):
        self.menu.show(self.window.display)
        self.window.render()
