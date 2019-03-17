from engine.components import textComponent, menuComponent, imageComponent
from engine.constants.colors import COLORS
import pygame


class MainMenu(menuComponent.MenuComponent):
    def __init__(self, *args, onQuit=None, onImg=None, bg=None, **kwargs):
        super().__init__(*args, background=bg, **kwargs)

        self.addChild(textComponent.TextComponent(self, text="Hello World!", textSize=50, color=COLORS.BLACK, onActivate=lambda: print("Hello")))
        self.addChild(textComponent.TextComponent(self, text="FooBar", y=40, textSize=50, color=COLORS.BLACK, onActivate=onImg))
        self.addChild(textComponent.TextComponent(self, text="QUIT", y=120, textSize=50, color=COLORS.BLACK, onActivate=onQuit))

        for child in self.children:
            child.centerHorizontal()

        self.K_NEXT = pygame.K_s
        self.K_PREV = pygame.K_w
        self.centerHorizontal()


class GameLogic:
    def __init__(self, window):
        self.window = window

        self.img  = imageComponent.ImageComponent(window, "python.png")
        self.img.fitToScreen(window)
        self.menu = MainMenu(window, size=window.size, backgroundColor=COLORS.BLUE, onQuit=self.quit, onImg=self.onImg, bg=self.img)

        self.context = self.menu


    def input(self):
        if self.context == self.img:
            if self.window.isKeyPressed(pygame.K_ESCAPE):
                self.context = self.menu
        else:
            self.menu.handleSelection(self.window)
            self.menu.handleActivation(self.window)


    def update(self):
        self.window.update()


    def render(self):
        self.context.show(self.window.display)
        self.window.render()

    def onImg(self):
        self.context = self.img

    def quit(self):
        # Gently shut down
        print("Shutting down")
        self.window.quit()
