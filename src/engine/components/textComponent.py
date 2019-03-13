from .component import Component
from pygame.font import Font, SysFont

class TextComponent(Component):
    def __init__(self, container, text="", fontType="", x=0, y=0, textSize=0, color=(255,255,255)):
        self.text = text
        self.textSize = textSize
        self.color = color
        self.font = SysFont(fontType, self.textSize)
        self.size = self.font.size(self.text)
        self.surface = self.font.render(self.text, True, self.color)
        super().__init__(container, x, y, self.size, surface=self.surface)

    def setColor(self, color):
        color = [a if a < 255 else 255 for a in color]
        color = [a if a > 0 else 0 for a in color]
        self.color = color
        self.update()

    def setText(self, text):
        self.text = text
        self.update()

    def update(self):
        self.surface = self.font.render(self.text, True, self.color)

    def select(self):
        self.setColor((150,120,120))

    def unSelect(self):
        self.setColor((0,0,0))
