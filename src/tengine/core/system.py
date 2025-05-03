from abc import abstractmethod
from tengine.core.entity import Entity
from tengine.core.worldinfo import WorldInfo

class System:
    @abstractmethod
    def update(self, entities: list[Entity], world_info: WorldInfo):
        pass