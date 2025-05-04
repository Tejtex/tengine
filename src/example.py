from tengine.core.component import Bundle, Component
from tengine.core.system import System
from tengine.core.world import World

class Position(Component):
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Velocity(Component):
    def __init__(self, dx, dy):
        self.dx =dx
        self.dy = dy

class VelocitySystem(System):
    
    def update(self, entities, world_info):
        
        for entity in entities:
            if entity.has_component(Position) and entity.has_component(Velocity):
                entity.get_component(Position).x += entity.get_component(Velocity).dx * world_info.dt
                entity.get_component(Position).y += entity.get_component(Velocity).dy * world_info.dt
class PrintSystem(System):
    def update(self, entities, world_info):
        for entity in entities:
            if entity.has_component(Position):
                pos = entity.get_component(Position)
                print(pos.x, pos.y)


world = World()
world.spawn_entity(Velocity(1, 1), Position(0, 0))
world.add_system(VelocitySystem())
world.add_system(PrintSystem())
world.mainloop()



