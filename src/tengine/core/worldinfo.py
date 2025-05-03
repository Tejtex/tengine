
class WorldInfo:
    """
    WorldInfo contains information about the current state of the world.
    Attributes:
        dt (float): The time delta since the last update.
    """
    def __init__(self, dt):
        """
        Initializes WorldInfo with the given time delta.
        Args:
            dt (float): The time delta since the last update.
        """
        self.dt = dt