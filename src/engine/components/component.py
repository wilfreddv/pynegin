class Component:
    """Base class for objects that can be rendered to screen
    """

    def __init__(self, container, x, y, size, isVisible=True, surface=None, border=None):
        self.container = container
        self.isVisible = isVisible
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.rect.center = (x + size[0]/2, y + size[1]/2)

    def getPosition(self):
        return (self.xPos, self.yPos)

    def getSize(self):
        return (self.width, self.height)

    def center(self):
        container = self.container

        width, height = self.getWidth(), self.getHeight()

        x = (container.getWidth() - width) / 2 + container.getXPos()
        y = (container.getHeight() - height) / 2 + container.getYPos()
        self.rect.center = (x + width/2, y + height/2)

    def moveHorizontal(self, distance):
        self.rect.move_ip(distance, 0)

    def moveVertical(self, distance):
        self.rect.move_ip(0, distance)

    def setVisible(self, isVisible):
        self.isVisible = isVisible

    def show(self, surf):
        if self.isVisible:
            surf.blit(self.surface, self.rect)

    def getXPos(self):
        return self.rect.x

    def getYPos(self):
        return self.rect.y

    def getWidth(self):
        return self.rect.width

    def getHeight(self):
        return self.rect.height

    def isHovered(self, window):
        mX, mY = window.getMousePos()
        x = self.getXPos()
        y = self.getYPos()
        return x < mX < x + self.getWidth() and y < mY < y + self.getHeight()

    def select(self):
        pass

    def unSelect(self):
        pass

    def activate(self):
        pass
