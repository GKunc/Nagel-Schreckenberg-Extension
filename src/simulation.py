import random
import numpy as np
from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from car import Car


class Simulation(Model):
    spawn_probability = 0.2

    # for now its just one lane
    def __init__(self, width=100, height=1):
        self.road_length = width
        self.num_agents = 20
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # Create agents
        for i in range(self.num_agents):
            a = Car(i, self, self.road_length)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
        self.running = True

    def step(self):
        self.schedule.step()
        self.create_random_car()

    def create_random_car(self):
        score = np.random.choice([1, 0], p=[self.spawn_probability, 1 - self.spawn_probability])
        if score and self.grid.is_cell_empty((0, 0)):
            car_id = random.randint(1, 1000)
            a = Car(car_id, self, self.road_length)
            self.schedule.add(a)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (0, y))
