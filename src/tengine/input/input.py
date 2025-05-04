import pyglet
from tengine.core.system import System
from tengine.core.resource import Resource
from tengine.renderer.window import Window

class Input(Resource):
    def __init__(self):
        self.keys = set()
        self.mouse_buttons = set()
        self.mouse_position = (0, 0)

    def is_key_pressed(self, key):
        return key in self.keys

    def is_mouse_button_pressed(self, button):
        return button in self.mouse_buttons

    def get_mouse_position(self):
        return self.mouse_position

class InputSystem(System):

    

    def register_window(self, window):
        window.push_handlers(self)

    def on_key_press(self, symbol, modifiers):
        self.input.keys.add(symbol)

    def on_key_release(self, symbol, modifiers):
        self.input.keys.discard(symbol)

    def on_mouse_motion(self, x, y, dx, dy):
        self.input.mouse_position = (x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        self.input.mouse_buttons.add(button)

    def on_mouse_release(self, x, y, button, modifiers):
        self.input.mouse_buttons.discard(button)
    
    def startup(self, entities, resources):
        if not resources.has_resource(Input) or not resources.has_resource(Window):
            return False
        self.input = resources.get_resource(Input)
        window = resources.get_resource(Window)
        self.register_window(window.window)

        return False
