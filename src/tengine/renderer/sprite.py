from tengine.core.component import Bundle, Component
import pyglet

from tengine.core.system import System
from tengine.common.transform import Transform
from tengine.renderer.window import Window


class Sprite(Component):
    def __init__(self, sprite: pyglet.sprite.Sprite):
        """
        Initializes a Sprite component with a given sprite.

        Args:
            sprite (pyglet.sprite.Sprite): The sprite to be used for rendering.
        """
        self.sprite = sprite

class SpriteBundle(Bundle):
    def __init__(self, 
                 image: pyglet.image.AbstractImage, 
                 position: tuple[float, float] = (0, 0), 
                 rotation: float = 0.0, 
                 scale: tuple[float, float] = (1.0, 1.0)
                 ):
        super().__init__()
        self.components.append(Transform(position, rotation, scale))
        sprite = pyglet.sprite.Sprite(image, position[0], position[1])
        self.components.append(Sprite(sprite))