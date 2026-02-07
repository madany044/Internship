from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key ignition")


class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with self-start button")


class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started with heavy ignition system")


car1 = Car()
bike1 = Bike()
bus1 = Bus()

car1.start_engine()
bike1.start_engine()
bus1.start_engine()
