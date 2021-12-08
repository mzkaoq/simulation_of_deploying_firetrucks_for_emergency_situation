from abc import ABC
import threading
import random
import time
from fire_units import BusyTruck,FreeTruck,TruckGoingFrom,TruckGoingTo,FireTruck

class DefaultStrategies(ABC):
    def __init__(self, event, iterator):
        self._event = event
        self._iterator = iterator
        self._go_to = random.uniform(0, 3)
        self._action = random.uniform(5, 25)
        self._back = random.uniform(0, 3)

    def doing_stuff(self, truck, total_time):
        x = threading.Thread(target=self.taking_some_time_to_done, args=(total_time,truck,))
        x.start()

    def taking_some_time_to_done(self,total_time,truck):
        #print("zaczeła sie akcja", total_time)
        truck.state = BusyTruck()
        time.sleep(total_time)
        truck.state = FreeTruck()
        #print("koniec",total_time)

class StrategyMZ(DefaultStrategies):
    def __init__(self, event, iterator):
        super().__init__(event, iterator)
        self._truck_needed = event.truck_needed
        for i in range(self._truck_needed):
            fire_truck = next(self._iterator)
            if event.is_fake == True:
                time_needed = self._go_to + self._back
                self.doing_stuff(fire_truck,time_needed)
            else:
                time_needed = self._go_to + self._back + self._action
                self.doing_stuff(fire_truck, time_needed)


class StrategyPZ(DefaultStrategies):
    def __init__(self, event, iterator):
        super().__init__(event, iterator)
        self._truck_needed = event.truck_needed
        for i in range(self._truck_needed):
            fire_truck = next(self._iterator)
            if event.is_fake == True:
                time_needed = self._go_to + self._back
                self.doing_stuff(fire_truck,time_needed)
            else:
                time_needed = self._go_to + self._back + self._action
                self.doing_stuff(fire_truck, time_needed)