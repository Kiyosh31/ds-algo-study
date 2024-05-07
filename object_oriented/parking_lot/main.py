"""
Parking lot

- Floors
- Vehicles
- Payment
"""


import datetime
import math


class Vehicle:
    """Vehicle"""

    def __init__(self, size) -> None:
        self._size = size

    def get_spot_size(self):
        """get size"""
        return self._size


class Car(Vehicle):
    """car"""

    def __init__(self) -> None:
        super().__init__(1)


class Limo(Vehicle):
    """limo"""

    def __init__(self) -> None:
        super().__init__(2)


class SemiTruck(Vehicle):
    """semi truck"""

    def __init__(self) -> None:
        super().__init__(3)


class Driver:
    """Driver"""

    def __init__(self, car_id, vehicle) -> None:
        self._id = car_id
        self._vehicle = vehicle
        self._payment_due = 0

    def get_vehicle(self):
        """getter"""
        return self._vehicle

    def get_id(self):
        """getter"""
        return self._id

    def charge(self, amount):
        """modificator"""
        self._payment_due += amount


class ParkingFlor:
    """Parking floor"""

    def __init__(self, spot_count) -> None:
        self._spots = [0]*spot_count
        self._vehicle_map = {}

    def park_vehicle(self, vehicle):
        """park vehicle"""
        size = vehicle.get_spot_size()
        l, r = 0, 0
        while r < len(self._spots):
            if self._spots[r] != 0:
                l = r + 1
            if r - l + 1 == size:
                # we found enough spots, park the vehicle
                for k in range(l, r+1):
                    self._spots[k] = 1
                self._vehicle_map[vehicle] = [l, r]
                return True
            r += 1
        return False

    def remove_vehicle(self, vehicle):
        """remove"""
        start, end = self._vehicle_map[vehicle]
        for i in range(start, end + 1):
            self._spots[i] = 0
        del self._vehicle_map[vehicle]

    def get_parking_spots(self):
        """getter"""
        return self._spots

    def get_vehicle_spots(self, vehicle):
        """vehicle spots"""
        return self._vehicle_map.get(vehicle)


class ParkingGarage:
    """Parking garage"""

    def __init__(self, floor_count, spots_per_floor):
        self._parking_floors = [ParkingFlor(
            spots_per_floor) for _ in range(floor_count)]

    def park_vehicle(self, vehicle):
        """park"""
        for floor in self._parking_floors:
            if floor.park_vehicle(vehicle):
                return True
        return False

    def remove_vehicle(self, vehicle):
        """remove"""
        for floor in self._parking_floors:
            if floor.get_vehicle_spots(vehicle):
                floor.remove_vehicle(vehicle)
                return True
        return False


class ParkingSystem:
    """Parking system"""

    def __init__(self, parking_garage, hourly_rate):
        self._parking_garage = parking_garage
        self._hourly_rate = hourly_rate
        self._time_parked = {}  # map driverId to time that they parked

    def park_vehicle(self, driver):
        """Park"""
        current_hour = datetime.datetime.now().hour
        is_parked = self._parking_garage.park_vehicle(driver.get_vehicle())
        if is_parked:
            self._time_parked[driver.get_id()] = current_hour
        return is_parked

    def remove_vehicle(self, driver):
        """remove"""
        if driver.get_id() not in self._time_parked:
            return False
        current_hour = datetime.datetime.now().hour
        time_parked = math.ceil(
            current_hour - self._time_parked[driver.get_id()])
        driver.charge(time_parked * self._hourly_rate)

        del self._time_parked[driver.get_id()]
        return self._parking_garage.remove_vehicle(driver.get_vehicle())


parkingGarage = ParkingGarage(3, 2)
parkingSystem = ParkingSystem(parkingGarage, 5)

driver1 = Driver(1, Car())
driver2 = Driver(2, Limo())
driver3 = Driver(3, SemiTruck())

print(parkingSystem.park_vehicle(driver1))      # true
print(parkingSystem.park_vehicle(driver2))      # true
print(parkingSystem.park_vehicle(driver3))      # false

print(parkingSystem.remove_vehicle(driver1))    # true
print(parkingSystem.remove_vehicle(driver2))    # true
print(parkingSystem.remove_vehicle(driver3))    # false
