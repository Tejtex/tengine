from tengine.common.time import Time
from tengine.core.plugin import Plugin
from tengine.common.time import TimeSystem
from tengine.renderer.window import Window
from tengine.renderer.renderer import RenderSystem


class DefaultPlugins(Plugin):
    """
    Default plugins for Tengine.
    """

    def __init__(self, width=800, height=600, title="Tengine"):
        """
        Initialize the default plugins.
        
        Args:
            width (int): The width of the window.
            height (int): The height of the window.
            title (str): The title of the window.
        """
        self.width = width
        self.height = height
        self.title = title
        

    def load(self, world):
        world.add_resource(Time())
        world.add_system(TimeSystem())
        world.add_resource(Window(self.width, self.height, self.title))
        world.add_system(RenderSystem())