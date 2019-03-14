import pygame
from pygame.locals import *
from .container import Container

class Window(Container):
    def __init__(self, size, title, backgroundColor=(0,0,0)):
        super().__init__(0, 0, *size)
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(title)
        self.size = size
        self.backgroundColor = backgroundColor
        self.events = []
        self._shouldStop = False


    def create(self):
        self.display = pygame.display.set_mode(self.size)


    def update(self):
        self.events = pygame.event.get()


    def shouldStop(self):
        types = [e.type for e in self.events]
        if self._shouldStop or QUIT in types:
            pygame.display.quit()
            return True


    def isKeyPressed(self, key):
        return pygame.key.get_pressed()[key] == 1


    def isKeyNotPressed(self, key):
        return not self.isKeyPressed(key)


    def isKeyDown(self, key):
        """Check for KEYDOWN event for key"""
        events = [e for e in self.events if e.type == KEYDOWN]
        ekeys = [e.key for e in events]
        return key in ekeys


    def isKeyUp(self, key):
        """Check for KEYUP event for key"""
        events = [e for e in self.events if e.type == KEYUP]
        ekeys = [e.key for e in events]
        return key in ekeys


    def isMouseButtonPressed(self, mouseButton):
        return pygame.mouse.get_pressed()[mouseButton]


    def getMousePos(self):
        return pygame.mouse.get_pos()


    def getEvents(self):
        return self.events


    def render(self):
        """Show all the blitted elements and immediately clear
        the display so old elements won't stay
        """
        pygame.display.update()
        self.display.fill(self.backgroundColor)

    def quit(self):
        self._shouldStop = True
