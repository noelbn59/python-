from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def fuel_type(self):
        print("Most vehicle need fuel.")

class car(vehicle):
    def start(self):
        print("Car engine started with a key.")

class bike(vehicle):
    def start(self):
      print("Bike engine start with button.")

car = car()
bike = bike()

car.start()
bike.start()
car.fuel_type()