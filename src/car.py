from mesa import Agent
import numpy as np
import random


class Car(Agent):
    rand_probability = 0.5
    spawn_probability = 0.2

    def __init__(self, unique_id, model, road_length):
        super().__init__(unique_id, model)
        self.road_length = road_length
        self.color = "%06x" % random.randint(0, 0xFFFFFF);
        self.min_velocity = 0
        self.max_velocity = 5
        self.velocity = random.randint(self.min_velocity, self.max_velocity)

    def step(self):
        # 1.Acceleration
        self.increase_velocity()

        # 2. Slow down not to hit car ahead
        self.slow_down()

        # 3. Randomization
        self.randomize_velocity(self.rand_probability)

        # 4. Car motion
        self.move_or_remove_car()

    def increase_velocity(self):
        self.velocity = min(self.max_velocity, self.velocity+1)
        return

    def slow_down(self):
        car_ahead = self.get_car_ahead(self.pos)
        if car_ahead is not None:
            distance = self.calculate_distance(car_ahead)
            self.velocity = min(self.velocity, distance)
        return

    def randomize_velocity(self, probability):
        if self.velocity < 1:
            return
        score = np.random.choice([1, 0], p=[probability, 1-probability])
        self.velocity = max(1, self.velocity-score)
        return

    def get_car_ahead(self, position):
        car_ahead = None
        for i in range(position[0] + 1, self.road_length):
            if not(self.model.grid.is_cell_empty((i, position[1]))):
                car_ahead = (i, position[1])
                break
        return car_ahead

    def calculate_distance(self, car_ahead):
        current_position = self.pos[0]
        car_ahead_position = car_ahead[0]
        return ((car_ahead_position - current_position + self.road_length) % self.road_length)-1

    def move_or_remove_car(self):
        new_position = self.pos[0] + self.velocity
        if new_position > self.road_length:
            print("KLL")
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
        else:
            self.model.grid.move_agent(self, (new_position, self.pos[1]))