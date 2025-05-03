from tengine.core.world import World




class Plugin:
    """
    Base class for plugins that can be loaded into the world.
    Plugins can modify the world by adding systems, components, or other functionality.
    """
    def load(self, world: World) -> World:
        """
        Load the plugin into the world.

        Args:
            world (World): The world instance to load the plugin into.

        Returns:
            World: The modified world instance.
        """
        return world