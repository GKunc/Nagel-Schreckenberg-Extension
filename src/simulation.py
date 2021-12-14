import random
import numpy as np
from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from cars.family_car import FamilyCar
from cars.truck import Truck
from cars.sports_car import SportsCar


class Simulation(Model):
    spawn_probability = 0.2

    # Todo
    # Add second lane
    def __init__(self, width=100, height=1):
        self.road_length = width
        self.num_agents = 20
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # Create agents
        for i in range(self.num_agents):
            car = self.create_car(i)
            self.schedule.add(car)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(car, (x, y))
        self.running = True

    def step(self):
        self.schedule.step()
        self.create_random_car()

    def create_random_car(self):
        score = np.random.choice([1, 0], p=[self.spawn_probability, 1 - self.spawn_probability])
        if score and self.grid.is_cell_empty((0, 0)):
            car_id = random.randint(1, 1000)
            car = self.create_car(car_id)
            self.schedule.add(car)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(car, (0, y))

    def create_car(self, i):
        # Todo
        # Add probability of spawning
        car_type = self.random.randrange(3)
        if car_type == 0:
            return FamilyCar(i, self, self.road_length)
        elif car_type == 1:
            return SportsCar(i, self, self.road_length)
        elif car_type == 2:
            return Truck(i, self, self.road_length)