from tengine.core.resource import Resource
from tengine.core.system import System
import time as t


class Time(Resource):
    def __init__(self):
        self.time = 0.0
        self.dt = 0
        self.start_time = t.time()

class TimeSystem(System):
    def __init__(self):
        self.last_time = 0.0

    def update(self, entities, resources) -> bool:
        time = resources.get_resource(Time)
        time.time = t.time() - time.start_time
        current_time = time.time
        time.dt = current_time - self.last_time
        self.last_time = current_time
        return False