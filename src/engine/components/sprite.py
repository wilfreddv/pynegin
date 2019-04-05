from PIL import Image as PIL_Image
import pathlib

class Sprite:
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

        path = pathlib.Path(__file__).parent.parent.parent.absolute()
        ass_path = path.joinpath("assets/")
        path = str(ass_path.joinpath(source))

        spriteMap = PIL_Image.open(path)
        sprites = []

        rows = round(amount / per_row)
        total_height = (rows + padding) * size[1]
        total_width = (per_row + padding) * size[0]
        for row in range(padding, total_height-size[1], size[1]):
            for sp in range(padding, total_width-size[0], size[0]):
                    sprites.append(spriteMap.crop( (sp, row, sp+size[0], row+size[1]) ))

        for idx, sprite in enumerate(sprites):
            sprite.save(ass_path.joinpath(f"{idx}.png"))
