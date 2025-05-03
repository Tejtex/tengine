from tengine.core.component import Component


class Transform(Component):
    def __init__(self, position: tuple[float, float] = (0, 0), rotation: float = 0.0, scale: tuple[float, float] = (1.0, 1.0)):
        """
        Initializes a Transform component with position, rotation, and scale.

        Args:
            position (tuple[float, float]): The position of the entity in the world.
            rotation (float): The rotation of the entity in degrees.
            scale (tuple[float, float]): The scale of the entity in the x and y directions.
        """
        self.position = position
        self.rotation = rotation
        self.scale = scale