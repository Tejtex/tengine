from tengine.core.component import Component


class Entity:
    def __init__(self, components: list[Component]):
        self.id = id(self)
        self.components = components