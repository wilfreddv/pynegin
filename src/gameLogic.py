from engine.components import text, menu, image, sprite
from engine.constants.colors import COLORS
import pygame


class MainMenu(menu.Menu):
    def __init__(self, *args, onQuit=None, onImg=None, bg=None, **kwargs):
        super().__init__(*args, background=bg, **kwargs)

        self.addChild(text.Text(self, text="Hello World!", textSize=50, color=COLORS.BLACK, onActivate=lambda: print("Hello")))
        self.addChild(text.Text(self, text="FooBar", y=40, textSize=50, color=COLORS.BLACK, onActivate=onImg))
        self.addChild(text.Text(self, text="QUIT", y=120, textSize=50, color=COLORS.BLACK, onActivate=onQuit))

        for child in self.children:
            child.centerHorizontal()

        self.K_NEXT = pygame.K_s
        self.K_PREV = pygame.K_w
        self.centerHorizontal()


class GameLogic:
    def __init__(self, window):
        self.window = window

        self.img  = image.Image(window, "python.png")
        self.img.resize((10,10))
        self.menu = MainMenu(window, size=window.size, backgroundColor=COLORS.BLUE, onQuit=self.quit, onImg=self.onImg)

        self.sprite = sprite.Sprite(window, "test.png", size=(16,16), padding=1, per_row=2, amount=4)
        self.sprite.fitToScreen(window)
        self.sprite.center()
        self.context = self.sprite


    def input(self):
        if self.window.isKeyDown(pygame.K_q):
            self.sprite.next()


    def update(self):
        self.window.update()


    def render(self):
        self.context.show(self.window.display)
        self.window.render(self.context)

    def onImg(self):
        self.context = self.img

    def quit(self):
        # Gently shut down
        print("Shutting down")
        self.window.quit()
