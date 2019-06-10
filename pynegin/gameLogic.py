class GameLogic:
    def __init__(self, window, context):
        self.window = window
        self.context = context

    def input(self):
        pass

    def update(self):
        self.window.update()

    def render(self):
        self.context.show(self.window.display)
        self.window.render(self.context)

    def quit(self):
        self.window.quit()
