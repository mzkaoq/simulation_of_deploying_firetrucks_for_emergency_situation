import random
from time import sleep

from observer import Observer
from data import fire_departments
from fire_units import FireDepartment, FireTruck, FreeTruck, BusyTruck
from event import Event, MZ, PZ
from iterator import  Iterator
from strategies import DefaultStrategies, StrategyMZ, StrategyPZ

class Manager:
    def __init__(self):
        self._fire_stations = []
        self._observer = Observer()
        self._sorted_list = []
        for department in fire_departments:
            station = FireDepartment(department[0],department[1],department[2])
            self._fire_stations.append(station)

        while True:
            sleep(1)
            self._sorted_list = []
            cord_x = random.uniform(49.95855025648944, 50.154564013341734)
            cord_y = random.uniform(19.688292482742394, 20.02470275868903)
            if random.uniform(0, 1) < 0.7:
                event = MZ(cord_x, cord_y)
                print("nowa akcja MZ")
            else:
                event = PZ(cord_x, cord_y)
                print("nowa akcja PZ")
            self._sorted_list = self._observer.collect_info(self._fire_stations, event)
            print("dostepne wozy",len(self._sorted_list))
            iterator = iter(Iterator(self._sorted_list))
            """
            for i in self._sorted_list:
                print(i)
            """
            if isinstance(event, MZ) == True:
                StrategyMZ(event, iterator)
            else:
                StrategyPZ(event, iterator)




