from mesa import Agent
import numpy as np
import random
import config

from cars.family_car import FamilyCar
from cars.sports_car import SportsCar
from cars.truck import Truck


class Entrance(Agent):
    spawn_probability = config.ENTRY_SPAWN_PROBABILITY

    def __init__(self, unique_id, model, road_length):
        super().__init__(unique_id, model)
        self.road_length = road_length

    def step(self):
        self.create_random_car()

    def create_random_car(self):
        score = np.random.choice([1, 0], p=[self.spawn_probability, 1 - self.spawn_probability])
        if score and self.model.grid.is_cell_empty((self.pos[0] + 1, self.pos[1])):
            car_id = random.randint(1, 1000)
            car = self.add_unique_car(car_id)
            y = self.random.randrange(self.model.grid.height)
            self.model.grid.place_agent(car, (self.pos[0], y))

    def add_unique_car(self, i):
        try:
            car = self.create_car(i)
            self.model.schedule.add(car)
        except Exception:
            self.add_unique_car(i + 1)
        return car

    def create_car(self, i):
        car_type = self.random.randrange(20)
        score = np.random.choice([1, 0], p=[self.spawn_probability, 1 - self.spawn_probability])
        if score:
            if car_type % 2 == 0:  # 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
                return FamilyCar(i, self.model, self.road_length)
            elif car_type == 0:  # 3, 9, 15
                return Truck(i, self.model, self.road_length)
            else: # 1, 5, 7, 11, 13, 17, 19
                return SportsCar(i, self.model, self.road_length)
