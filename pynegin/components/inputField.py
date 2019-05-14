from .text import Text
from ..constants.keys import Keys
from ..constants.colors import COLORS

class InputField(Text):
    def __init__(self, container, text="", fontType="", x=0, y=0, textSize=0, color=COLORS.WHITE, onActivate=None):
        self.ready = False # User has hit return
        super().__init__(container, text, fontType, x, y, textSize, color, onActivate)

    def updateInput(self, pressedKeys):
        self.rect = self.surface.get_rect()

        text = self.getText()

        for key in pressedKeys:
            if not key in Keys:
                continue

            if '\b' == Keys[key]:
                text = text[:-1]
            elif '\r' == Keys[key]:
                self.ready = True
            else:
                text += Keys[key]

        self.text = text
        self.surface = self.font.render(self.text, True, self.color)
