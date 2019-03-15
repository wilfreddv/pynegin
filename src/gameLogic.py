from engine.components import textComponent, menuComponent, imageComponent
from engine.constants.colors import COLORS
import pygame


class MainMenu(menuComponent.MenuComponent):
    def __init__(self, *args, onQuit=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.addChild(textComponent.TextComponent(self, text="Hello World!", textSize=50, color=COLORS.BLACK, onActivate=lambda: print("Hello")))
        self.addChild(textComponent.TextComponent(self, text="FooBar", y=40, textSize=50, color=COLORS.BLACK, onActivate=lambda: print("FooBar")))
        self.addChild(textComponent.TextComponent(self, text="QUIT", y=120, textSize=50, color=COLORS.BLACK, onActivate=onQuit))

        for child in self.children:
            child.centerHorizontal()

        self.K_NEXT = pygame.K_s
        self.K_PREV = pygame.K_w
        self.centerHorizontal()


class GameLogic:
    def __init__(self, window):
        self.window = window

        self.menu = MainMenu(window, size=window.size, backgroundColor=COLORS.BLUE, onQuit=self.quit)
        self.img  = imageComponent.ImageComponent(window, "python.png")
        self.img.fitToScreen(window)


    def input(self):
        self.menu.handleSelection(self.window)
        self.menu.handleActivation(self.window)


    def update(self):
        self.window.update()


    def render(self):
        #self.menu.show(self.window.display)
        self.img.show(self.window.display)
        self.window.render()


    def quit(self):
        # Gently shut down
        print("Shutting down")
        self.window.quit()
