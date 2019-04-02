from .component import Component
import pygame
import pathlib

class Image(Component):
    def __init__(self, container, source, x=0, y=0, size=(0,0), isVisible=True,
                 surface=None, border=None, onActivate=None, basePath=None):

        if not basePath:
            path = pathlib.Path(__file__).parent.parent.parent.absolute()
            path = path.joinpath("assets/")
            path = str(path.joinpath(source))

        surface = pygame.image.load(path)
        super().__init__(container, x=x, y=y, size=size, isVisible=isVisible, surface=surface, border=border, onActivate=onActivate)


    def fitToScreen(self, window):
        toSize = window.size
        self.surface = pygame.transform.scale(self.surface, toSize)
        self._update_rect()

    def resize(self, size):
        self.surface = pygame.transform.scale(self.surface, size)
        self._update_rect()
