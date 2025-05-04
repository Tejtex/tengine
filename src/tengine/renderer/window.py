from tengine.core.resource import Resource


class Window(Resource):
    """
    The Window class represents a window in the rendering system.
    It is responsible for creating and managing the window where the graphics are displayed.
    """
    def __init__(self, width: int, height: int, title: str):
        """
        Initializes a Window instance with the given width, height, and title.

        Args:
            width (int): The width of the window.
            height (int): The height of the window.
            title (str): The title of the window.
        """
        self.width = width
        self.height = height
        self.title = title
        from pyglet.window import Window as PygletWindow
        self.window = PygletWindow(self.width, self.height, self.title)
        self.window.set_visible(True)
        @self.window.event
        def on_draw():
            pass