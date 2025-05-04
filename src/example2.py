import pyglet
from tengine.common.time import Time, TimeSystem
from tengine.core.component import Bundle, Component
from tengine.core.system import System
from tengine.core.world import World
from tengine.common.transform import Transform
from tengine.renderer.renderer import RenderSystem
from tengine.renderer.sprite import Sprite, SpriteBundle
from tengine.renderer.window import Window
import math
from tengine.common.defaultplugins import DefaultPlugins

class Velocity(Component):
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
class VelocitySystem(System):
    def update(self, entities, resources) -> bool:
        for entity in entities:
            if entity.has_component(Velocity) and entity.has_component(Transform):
                velocity = entity.get_component(Velocity)
                transform = entity.get_component(Transform)
                transform.position = (transform.position[0] + velocity.dx, transform.position[1] + velocity.dy)
                transform.rotation += 1
                transform.scale = (math.sin(resources.get_resource(Time).time) , math.sin(resources.get_resource(Time).time))
        return False
world = World()
world.spawn_entity(Velocity(.1, .1), SpriteBundle(pyglet.image.create(100, 100, pyglet.image.CheckerImagePattern())))
world.add_plugin(DefaultPlugins())
world.add_system(VelocitySystem())
world.mainloop()



