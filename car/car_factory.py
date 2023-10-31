
from abc import ABC
from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from car.serviceable import Serviceable
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory(ABC):

    class Car(Serviceable):
        def __init__(self, engine, battery):
            self.engine = engine
            self.battery = battery

        def needs_service(self):
            return self.engine.needs_service() or self.battery.needs_service()

    @staticmethod
    def create_calliope(current_mileage, last_service_mileage, current_date, last_service_date):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return CarFactory.Car(engine, battery)
    
    @staticmethod
    def create_glissade(current_mileage, last_service_mileage, current_date, last_service_date):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return CarFactory.Car(engine, battery)
    
    @staticmethod
    def create_palindrome(warning_light_on, current_date, last_service_date):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        return CarFactory.Car(engine, battery)
    
    @staticmethod
    def create_rorschach(current_mileage, last_service_mileage, current_date, last_service_date):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return CarFactory.Car(engine, battery)
    
    @staticmethod
    def create_thovex(current_mileage, last_service_mileage, current_date, last_service_date):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return CarFactory.Car(engine, battery)