
class CarGame:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"The car is accelerating. Current speed: {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0
        print(f"The car is braking. Current speed: {self.speed} km/h")

car1 = CarGame("Toyota", "Corolla", 2022)
car1.accelerate()
car1.brake()
