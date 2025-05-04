from tengine.core.plugin import Plugin
from tengine.core.system import System
from tengine.core.world import World
from tengine.common.transform import Transform
from tengine.renderer.sprite import Sprite
from tengine.renderer.window import Window


class RenderSystem(System):
    """
    RenderSystem is responsible for rendering entities with the Image component.
    It uses the pyglet library to create a window and draw images on the screen.
    """
    def update(self, entities, resources) -> bool:
        if (not resources.has_resource(Window)):
            return
        window = resources.get_resource(Window)
        window.window.dispatch_events()
        window.window.clear()
        for entity in entities:
            if entity.has_component(Sprite):
                sprite = entity.get_component(Sprite)
                transform = entity.get_component(Transform)
                sprite.sprite.x = transform.position[0]
                sprite.sprite.y = transform.position[1]
                sprite.sprite.rotation = transform.rotation
                sprite.sprite.scale_x = transform.scale[0]
                sprite.sprite.scale_y = transform.scale[1]
                sprite.sprite.draw()
        window.window.flip()
        if window.window.has_exit:
            return True
        return False