from abc import ABC

class FireDepartment:
    def __init__(self,name,cord_x,cord_y):
        self._name = name
        self._cords = [cord_x,cord_y]
        self._fire_trucks = []
        for i in range(5):
            truck = Truck()
            truck.state = FreeTruck()
            self._fire_trucks.append(truck)

    @property
    def cords(self):
        return self._cords

    @property
    def fire_trucks(self):
        return self._fire_trucks

    def number_of_fire_trucks(self):
        num = 0
        for truck in self._fire_trucks:
            if truck.free() == True:
                num += 1
            else:
                pass
        return num

class Truck:
    def __init__(self):
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self,value):
        self._state = value

class FireTruck(ABC):
    def __init__(self):
        pass

    def busy(self):
        pass

    def free(self):
        pass

    def going_to(self):
        pass

    def going_from(self):
        pass

    @property
    def department(self):
        return self._department

class FreeTruck(FireTruck):
    def busy(self):
        return False

    def free(self):
        return True

    def going_to(self):
        return False

    def going_from(self):
        return False

class BusyTruck(FireTruck):
    def busy(self):
        return True

    def free(self):
        return False

    def going_to(self):
        return False

    def going_from(self):
        return False

class TruckGoingTo(FireTruck):
    def busy(self):
        return False

    def free(self):
        return False

    def going_to(self):
        return True

    def going_from(self):
        return False

class TruckGoingFrom(FireTruck):
    def busy(self):
        return False

    def free(self):
        return False

    def going_to(self):
        return False

    def going_from(self):
        return True