from typing import Type, TypeVar


class Resource:
    """
    Resource is a global object that represents a single resource in the simulation world. It can be used to store and manage data that is shared across multiple entities or systems.
    """
    def __init__(self, name: str, data: object):
        """
        Initializes a resource with a name and data.
        Args:
            name (str): The name of the resource.
            data (object): The data associated with the resource.
        """
        self.name = name
        self.data = data


T = TypeVar("T", bound="Resource")


class Resources:
    """
    Resources is a collection of resources that can be used to store and manage data that is shared across multiple entities or systems.
    """
    def __init__(self):
        """
        Initializes an empty collection of resources.
        """
        self.resources: list[Resource] = []
    
    def add_resource(self, resource: Resource):
        """
        Adds a resource to the collection.
        Args:
            resource (Resource): The resource to add.
        """
        self.resources.append(resource)
    
    def get_resource(self, type: Type[T]) -> T | None:
        """
        Retrieves the resource of the specified type from the collection.
        Args:
            type (Type[Resource]): The type of resource to retrieve.
        Returns:
            Resource | None: The resource if found, None otherwise.
        """
        for resource in self.resources:
            if isinstance(resource, type):
                return resource
        return None
    def has_resource(self, type: Type[T]) -> bool:
        """
        Checks if the collection has a resource of the specified type.
        Args:
            type (Type[Resource]): The type of resource to check for.
        Returns:
            bool: True if the collection has the resource, False otherwise.
        """
        return any(isinstance(resource, type) for resource in self.resources)