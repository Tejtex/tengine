from abc import abstractmethod
from tengine.core.entity import Entity
from tengine.core.worldinfo import WorldInfo

class System:
    """
    System is an abstract base class that defines the interface for all systems in the simulation.
    Each system is responsible for updating a specific aspect of the entities in the world.
    Attributes:
        entities (list): A list of entities that the system will update.
    """
    @abstractmethod
    def update(self, entities: list[Entity], world_info: WorldInfo):
        """
        Updates the system with the given entities and world information.
        Args:
            entities (list[Entity]): A list of entities to be updated.
            world_info (WorldInfo): Information about the current state of the world.
        """
        pass