from .component import Component
import pygame

class Menu(Component):
    def __init__(self, container, x=0, y=0, size=None, isVisible=True, surface=None, backgroundColor=(255,255,255), background=None):
        self.size = size if size else (container.width, container.height)
        self.container = container
        self.isVisible = isVisible
        self.surface = pygame.Surface(self.size)
        self.backgroundColor = backgroundColor
        self.background = background
        self.children = []
        self.selected = -1
        self.K_NEXT, self.K_PREV = None, None # Keys for selecting next
        super().__init__(container, x, y, self.size, surface=self.surface)


    def addChildren(self, *children):
        for child in children:
            self.addChild(child)


    def addChild(self, child):
        self.children.append(child)


    def show(self, surf):
        if self.isVisible:
            self.surface.fill(self.backgroundColor)
            if self.background: self.surface.blit(self.background.surface, (0,0))
            for child in self.children:
                child.show(self.surface)

            surf.blit(self.surface, self.rect)


    def handleSelection(self, window):
        if self.isHovered(window):
            for i, child in enumerate(self.children):
                if child.isHovered(window):
                    self.children[self.selected].unSelect()
                    self.selected = i
                    self.children[self.selected].select()

        if not None in (self.K_NEXT, self.K_PREV):
            if window.isKeyDown(self.K_NEXT):
                self.selectNext()

            if window.isKeyDown(self.K_PREV):
                self.selectPrevious()


    def handleActivation(self, window):
        if window.isKeyDown(pygame.K_RETURN) or ( window.isMouseButtonPressed(0) and self.children[self.selected].isHovered(window) ):
            self.children[self.selected].activate()


    def selectNext(self):
        if len(self.children)-1 > self.selected:
            self.children[self.selected].unSelect()
            self.selected = self.selected + 1
            self.children[self.selected].select()


    def selectPrevious(self):
        if self.selected > 0:
            self.children[self.selected].unSelect()
            self.selected = self.selected - 1
            self.children[self.selected].select()


    def activateItem(self):
        self.children[self.selected].activate()
