from tires.model.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wear_readings):
        super().__init__()
        self.tire_wear_readings = tire_wear_readings

    def needs_service(self):
        return any(x for x in self.tire_wear_readings if x >= 0.9)