from engine.components import textComponent, menuComponent
from engine.constants.colors import COLORS
import pygame

class GameLogic:
    def __init__(self, window):
        self.window = window

        self.menu = menuComponent.MenuComponent(window, size=(500, window.getHeight()), backgroundColor=COLORS.BLUE)
        myText = textComponent.TextComponent(self.menu, text="Hello World!", textSize=50, color=COLORS.BLACK)
        myText2 = textComponent.TextComponent(self.menu, text="FooBar", y=50, textSize=50, color=COLORS.BLACK)
        myText.centerHorizontal()
        myText2.centerHorizontal()
        self.menu.addChildren(myText, myText2)
        self.menu.K_NEXT = pygame.K_s
        self.menu.K_PREV = pygame.K_w
        self.menu.centerHorizontal()

    def update(self):
        self.window.update()

    def input(self):
        self.menu.updateSelected(self.window)

        if self.window.isKeyDown(pygame.K_RETURN):
            self.menu.activateItem()


    def render(self):
        self.menu.show(self.window.display)
        self.window.render()
