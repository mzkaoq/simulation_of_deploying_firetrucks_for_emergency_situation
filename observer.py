from fire_units import FireDepartment
from event import Event, MZ, PZ


class Observer:
    def __init__(self):
        pass

    def collect_info(self, fire_stations, event):
        list_of_stations = []
        cord_x, cord_y = event.cords()
        for station in fire_stations:
            list_of_stations.append(station)
        sorted_list = self.sort_stations(list_of_stations, cord_x, cord_y)
        return sorted_list

    def sort_stations(self, list_of_stations, cord_x, cord_y):
        sorted_dict = {}
        fire_trucks_sorted = []
        for station in list_of_stations:
            dist = ((station.cords[0] - cord_x) ** 2 + (station.cords[1] - cord_y) ** 2) ** 0.5
            sorted_dict.update({dist: station})
            new_dict = sorted(sorted_dict.items())
        for value in new_dict:
            fire_dep = value[1]
            for fire_truck in fire_dep.fire_trucks:
                if fire_truck.state.free() == True:
                    #fire_trucks_sorted.append([fire_truck,value[0]])
                    fire_trucks_sorted.append(fire_truck)
        return fire_trucks_sorted
