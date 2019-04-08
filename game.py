from src.components import text, menu, image, sprite
from src.constants.colors import COLORS
from src.gameLogic import GameLogic
import pygame


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
        self.img  = image.Image(window, "python.png")
        self.img.resize((10,10))
        self.menu = MainMenu(window, size=window.size, backgroundColor=COLORS.BLUE, onQuit=self.quit)

        self.sprite = sprite.Sprite(window, "test2.png", size=(16,16), padding=1, per_row=2, amount=3)
        self.sprite.resize((200,200))
        self.sprite.center()

        super().__init__(window, self.sprite)


    def input(self):
        if self.window.isKeyPressed(pygame.K_RIGHT):
            self.sprite.select(1)
            self.sprite.moveHorizontal(5)
        elif self.window.isKeyPressed(pygame.K_LEFT):
            self.sprite.select(2)
            self.sprite.moveHorizontal(-5)
        else:
            self.sprite.select(0)
