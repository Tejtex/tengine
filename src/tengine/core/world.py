from tengine.core.component import Component
from tengine.core.entity import Entity
from tengine.core.system import System

import time

from tengine.core.worldinfo import WorldInfo



class World:
    def __init__(self):
        self.entities: list[Entity] = []
        self.systems: list[System] = []
    def add_system(self, system: System):
        self.systems.append(system)
    def spawn_entity(self, *components: Component):
        entity = Entity(components)
        self.entities.append(entity)
        return entity.id
    
    def update(self,world_info: WorldInfo):
        for system in self.systems:
            system.update(self.entities, world_info)
    
    def mainloop(self):
        t: float = time.time()
        while True:
            dt = time.time() - t
            t = time.time()
            world_info = WorldInfo(dt)
            self.update(world_info)