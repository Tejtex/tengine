from abc import abstractmethod
from tengine.core.entity import Entity
from tengine.core.resource import Resources

class System:
    """
    System is an abstract base class that defines the interface for all systems in the simulation.
    Each system is responsible for updating a specific aspect of the entities in the world.
    """
    @abstractmethod
    def update(self, entities: list[Entity], resources: Resources) -> bool:
        """
        Updates the system with the given entities and world information.
        Args:
            entities (list[Entity]): A list of entities to be updated.
        """
        pass