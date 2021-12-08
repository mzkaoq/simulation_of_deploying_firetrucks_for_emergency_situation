from abc import ABC
import random


class Event(ABC):
    def __init__(self, cord_x, cord_y):
        self._cord_x = cord_x
        self._cord_y = cord_y
        if random.uniform(0, 1) < 0.05:
            self._is_fake = True
        else:
            self._is_fake = False

    def cords(self):
        return [self._cord_x,self._cord_y]

    @property
    def is_fake(self):
        return self._is_fake

class MZ(Event):
    def __init__(self,cord_x,cord_y):
        super().__init__(cord_x, cord_y)
        self._truck_needed = 2

    @property
    def truck_needed(self):
        return self._truck_needed

class PZ(Event):
    def __init__(self,cord_x,cord_y):
        super().__init__(cord_x, cord_y)
        self._truck_needed = 3

    @property
    def truck_needed(self):
        return self._truck_needed