from typing import Type
from tengine.core.component import Component


class Entity:
    def __init__(self, components: list[Component]):
        self.id = id(self)
        self.components = components
    def has_component(self, type: Type[Component]) -> bool:
        return any(isinstance(component, type) for component in self.components)
    def get_component(self, type: Type[Component]) -> Component | None:
        for component in self.components:
            if isinstance(component, type):
                return component
        return None 