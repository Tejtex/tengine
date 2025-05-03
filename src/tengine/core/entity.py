from typing import Type
from tengine.core.component import Component


class Entity:
    """
    Entity represents a single object in the simulation world. It can have multiple components
    that define its behavior and properties.
    Attributes:
        id (int): Unique identifier for the entity.
        components (list): A list of components associated with the entity.
    """
    def __init__(self, components: list[Component]):
        """
        Initializes an entity with a unique ID and a list of components.
        Args:
            components (list): A list of components to associate with the entity.
        """
        self.id = id(self)
        self.components = components
    def has_component(self, type: Type[Component]) -> bool:
        """
        Checks if the entity has a component of the specified type.
        Args:
            type (Type[Component]): The type of component to check for.
        Returns:
            bool: True if the entity has the component, False otherwise.
        """
        return any(isinstance(component, type) for component in self.components)
    def get_component(self, type: Type[Component]) -> Component | None:
        """
        Retrieves the component of the specified type from the entity.
        Args:
            type (Type[Component]): The type of component to retrieve.
        Returns:
            Component | None: The component if found, None otherwise."""
        for component in self.components:
            if isinstance(component, type):
                return component
        return None 