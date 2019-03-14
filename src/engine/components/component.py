class Component:
    """Base class for objects that can be rendered to screen
    """

    def __init__(self, container, x=0, y=0, size=(0,0), isVisible=True, surface=None, border=None):
        self.container = container
        self.isVisible = isVisible
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.rect.center = (x + size[0]/2, y + size[1]/2)

    def getPosition(self):
        return (self.rect.x, self.rect.y)

    def getSize(self):
        return (self.width, self.height)

    def center(self):
        self.centerHorizontal()
        self.centerVertical()

    def centerHorizontal(self):
        container = self.container

        width = self.getWidth()
        y = self.rect.y
        x = (container.getWidth() - width) / 2 + container.getXPos()
        self.rect.center = (x + width/2, y + self.getHeight()/2)

    def centerVertical(self):
        container = self.container

        height = self.getHeight()
        x = self.rect.x
        y = (container.getHeight() - height) / 2 + container.getYPos()
        self.rect.center = (x + self.getWidth()/2, y + height/2)

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
        x = self.getXPos() + self.container.getXPos()
        y = self.getYPos() + self.container.getYPos()
        return x < mX < x + self.getWidth() and y < mY < y + self.getHeight()

    def select(self):
        pass

    def unSelect(self):
        pass

    def activate(self):
        pass
