from PIL import Image as PIL_Image
from .image import Image
from .component import Component
from pynegin.conf import HOME
import pathlib

class Sprite(Component):
    def __init__(self, container, source, size=(32, 32), padding=0, per_row=1, amount=1, animated=False, animation_speed=1.0):
        """container -> Component: parent Component of Sprite
           source -> str: path to the map (base=assets/)
           size -> tuple(int): size of single sprite
           padding -> int: padding between two sprites
           per_row -> int: amount of sprites per row
           amount -> int: total amount of sprites
           animated -> bool: do animation by default (e.g. fire)
           animation_speed -> float: seconds between animation
        """

        self.container = container
        self.source = source
        self.size = size
        self.padding = padding
        self.per_row = per_row
        self.amount = amount
        self.animated = animated
        self.animation_speed = animation_speed
        self.current = 0

        path = pathlib.Path(HOME)
        ass_path = path.joinpath("assets/")
        path = str(ass_path.joinpath(source))

        spriteMap = PIL_Image.open(path)
        self.sprites = []

        rows = round(amount / per_row)
        total_height = (rows + padding) * size[1]
        total_width = (per_row + padding) * size[0]
        for row in range(padding, total_height-size[1], padding+size[1]):
            for sp in range(padding, total_width-size[0], padding+size[0]):
                    sprite = spriteMap.crop( (sp, row, sp+size[0], row+size[1]) )
                    self.sprites.append( Image(container, None, fromString=True, PIL_img=sprite) )

        self.surface = self.sprites[0].surface
        self.rect = self.sprites[0].rect

        super().__init__(container, size=size, surface=self.surface)


    def show(self, surf):
        self._update()
        self.sprites[self.current].show(surf)

    def _update(self):
        self.rect = self.sprites[self.current].rect

    def center(self):
        self.centerHorizontal()
        self.centerVertical()

    def centerHorizontal(self):
        for sprite in self.sprites:
            sprite.centerHorizontal()

    def centerVertical(self):
        for sprite in self.sprites:
            sprite.centerVertical()

    def moveHorizontal(self, distance):
        for sprite in self.sprites:
            sprite.moveHorizontal(distance)

    def moveVertical(self, distance):
        for sprite in self.sprites:
            sprite.moveVertical(distance)

    def fitToScreen(self, window):
        for sprite in self.sprites:
            sprite.fitToScreen(window)

    def resize(self, size):
        for sprite in self.sprites:
            sprite.resize(size)

    def next(self):
        self.current = (self.current + 1) % len(self.sprites)

    def select(self, s):
        self.current = s % len(self.sprites)
