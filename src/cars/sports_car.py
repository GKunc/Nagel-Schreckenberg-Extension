from cars.car import Car
import random


class SportsCar(Car):
    def __init__(self, unique_id, model, road_length):
        Car.__init__(self, unique_id, model, road_length)
        self.min_velocity = 0
        self.max_velocity = 10
        self.velocity = random.randint(self.min_velocity, self.max_velocity)


