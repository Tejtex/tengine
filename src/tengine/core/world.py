from tengine.core.component import Bundle, Component
from tengine.core.entity import Entity
from tengine.core.plugin import Plugin
from tengine.core.system import System

import time

from tengine.core.worldinfo import WorldInfo



class World:
    """
    World represents the simulation environment containing entities and systems.
    
    Attributes:
        entities (list): A list of entities in the world.
        systems (list): A list of systems that are responsible for updating entities.
    """

    def __init__(self):
        """
        Initializes an empty world with no entities or systems.
        """
        self.entities: list[Entity] = []
        self.systems: list[System] = []
    def add_system(self, system: System):
        """
        Adds a system to the world.

        Args:
            system (System): A system to be added to the world.
        """
        self.systems.append(system)
        
    def add_plugin(self, plugin: Plugin):
        """
        Adds a plugin to the world.

        Args:
            plugin (Plugin): A plugin to be added to the world.
        """
        self = plugin.load(self)
    def spawn_entity(self, *components: Component | Bundle):
        """
        Spawns a new entity with the given components.

        Args:
            components (Component): Components to associate with the entity.

        Returns:
            int: The ID of the spawned entity.
        """
        end_components = []
        for component in components:
            if isinstance(component, Bundle):
                end_components.extend(component.components)
            else:
                end_components.append(component)
        entity = Entity(end_components)
        self.entities.append(entity)
        return entity.id
    
    def update(self,world_info: WorldInfo):
        """
        Runs all the systems in the world, updating the entities.
        Args:
            world_info (WorldInfo): Information about the current state of the world.
        """
        for system in self.systems:
            system.update(self.entities, world_info)
    
    def mainloop(self):
        """
        Main loop of the world. This method runs indefinitely, updating the world at each iteration.
        It calculates the time delta (dt) between each iteration and passes it to the systems.
        """
        t: float = time.time()
        while True:
            dt = time.time() - t
            t = time.time()
            world_info = WorldInfo(dt)
            self.update(world_info)