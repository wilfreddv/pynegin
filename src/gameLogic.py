from engine import textComponent, menuComponent
import pygame


class GameLogic:
    def __init__(self, window):
        self.window = window
        self.menu = menuComponent.MenuComponent(window, size=(500,500))
        myText = textComponent.TextComponent(self.menu, text="Hello World!", textSize=50, color=(255,50,50))
        myText2 = textComponent.TextComponent(self.menu, text="FooBar", textSize=50, color=(25,50,255))
        myText.center()
        myText2.center()
        myText.select()
        myText2.unSelect()
        myText2.activate = lambda: print("cool")
        myText2.moveVertical(50)
        self.menu.addChild(myText)
        self.menu.addChild(myText2)
        self.menu.center()

    def update(self):
        self.window.update()

    def input(self):
        if self.window.isKeyDown(pygame.K_s):
            self.menu.selectNext()

        if self.window.isKeyDown(pygame.K_w):
            self.menu.selectPrevious()

        if self.window.isKeyDown(pygame.K_RETURN):
            self.menu.activateItem()

    def render(self):
        self.menu.show(self.window.display)
        self.window.render()
