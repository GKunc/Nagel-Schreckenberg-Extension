from cars.car import Car
import random


class Truck(Car):
    def __init__(self, unique_id, model, road_length):
        Car.__init__(self, unique_id, model, road_length)
        self.color = "green"
        self.min_velocity = 0
        self.max_velocity = 5
        self.velocity = random.randint(self.min_velocity, self.max_velocity)


