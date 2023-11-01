from tires.model.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear_readings):
        super().__init__()
        self.tire_wear_readings = tire_wear_readings

    def needs_service(self):
        return sum(self.tire_wear_readings) >= 3