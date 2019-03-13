from .component import Component
import pygame

class MenuComponent(Component):
    def __init__(self, container, x=0, y=0, size=None, isVisible=True, surface=None, backgroundColor=(255,255,255)):
        self.size = size if size else (container.width, container.height)
        self.container = container
        self.isVisible = isVisible
        self.surface = pygame.Surface(self.size)
        self.backgroundColor = backgroundColor
        self.children = []
        self.selected = 0
        super().__init__(container, x, y, self.size, surface=self.surface)

    def addChild(self, child):
        self.children.append(child)

    def show(self, surf):
        if self.isVisible:
            self.surface.fill(self.backgroundColor)
            for child in self.children:
                child.show(self.surface)

            surf.blit(self.surface, self.rect)

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
