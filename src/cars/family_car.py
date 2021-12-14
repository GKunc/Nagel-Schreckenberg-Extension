from cars.car import Car
import random


class FamilyCar(Car):
    def __init__(self, unique_id, model, road_length):
        Car.__init__(self, unique_id, model, road_length)
        self.color = "red"
        self.min_velocity = 0
        self.max_velocity = 8
        self.velocity = random.randint(self.min_velocity, self.max_velocity)


