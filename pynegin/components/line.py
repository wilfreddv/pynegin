from .component import Component
from ..constants.colors import COLORS
from pygame.draw import line as drawline
from pygame import Surface

class Line(Component):
    def __init__(self, container, start_pos, end_pos, width, color=COLORS.BLACK):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = width
        self.color = color
        self.size = abs(start_pos[0]-end_pos[0])+width, abs(start_pos[1]-end_pos[1])+width
        self.surface = Surface(self.size)
        super().__init__(container, x=start_pos[0], y=start_pos[1], size=self.size, surface=self.surface)

    def show(self, surf):
        if self.isVisible:
            drawline(surf, self.color, self.start_pos, self.end_pos, self.width)

    def center(self):
        self.centerHorizontal()
        self.centerVertical()

    def centerHorizontal(self):
        container = self.container

        width = self.getWidth()
        y = self.rect.y
        x = (container.getWidth() - width) / 2 + container.getXPos()
        self.rect.center = (x + width/2, y + self.getHeight()/2)
        self._transpose((x-self.start_pos[0], 0))

    def centerVertical(self):
        container = self.container

        height = self.getHeight()
        x = self.rect.x
        y = (container.getHeight() - height) / 2 + container.getYPos()
        self.rect.center = (x + self.getWidth()/2, y + height/2)
        self._transpose((0, y-self.start_pos[1]))

    def moveHorizontal(self, distance):
        self.rect.move_ip(distance, 0)
        self._transpose((distance,0))

    def moveVertical(self, distance):
        self.rect.move_ip(0, distance)
        self._transpose((0,distance))

    def _transpose(self, diff=(0,0)):
        self.start_pos = self.start_pos[0]+diff[0], self.start_pos[1]+diff[1]
        self.end_pos = self.end_pos[0]+diff[0], self.end_pos[1]+diff[1]
