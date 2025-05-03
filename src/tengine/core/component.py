class Component:
    """
    Base class for all components in the simulation. Components are used to define the properties
    and behaviors of entities. Each component should inherit from this class.
    """
    pass

class Bundle:
    """
    A bundle is a collection of components that can be added to an entity. Bundles are used to
    group related components together for easier management and organization.
    """


    def __init__(self):
        """
        Initialize the bundle with an empty list of components. This is a abstract class and should not be instantiated directly.
        """
        self.components = []
    
