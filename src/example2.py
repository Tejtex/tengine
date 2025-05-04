import pyglet
from tengine.common.time import Time, TimeSystem
from tengine.core.component import Bundle, Component
from tengine.core.system import System
from tengine.core.world import World
from tengine.common.transform import Transform
from tengine.input.input import Input
from tengine.renderer.renderer import RenderSystem
from tengine.renderer.sprite import Sprite, SpriteBundle
from tengine.renderer.window import Window
import math
from tengine.common.defaultplugins import DefaultPlugins
from pyglet.window import key

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
                input = resources.get_resource(Input)
                time = resources.get_resource(Time)
                if input.is_key_pressed(key.SPACE):
                    velocity.dx += math.cos(transform.rotation) * time.dt
                    velocity.dy += math.sin(transform.rotation) * time.dt
                transform.position = (transform.position[0] + velocity.dx, transform.position[1] + velocity.dy)
                if input.is_key_pressed(key.A):
                    transform.rotation += time.dt * 30
                if input.is_key_pressed(key.D):
                    transform.rotation -= time.dt * 30
                transform.scale = (abs(math.sin(resources.get_resource(Time).time)) , abs(math.sin(resources.get_resource(Time).time)))
        return False
world = World()
world.spawn_entity(Velocity(.1, .1), SpriteBundle(pyglet.image.create(100, 100, pyglet.image.CheckerImagePattern())))
world.add_plugin(DefaultPlugins(1920, 1080))
world.add_system(VelocitySystem())
world.mainloop()



