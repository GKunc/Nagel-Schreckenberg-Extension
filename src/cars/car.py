from mesa import Agent
import numpy as np
import random

import config
from road import entrance
from road import exit


class Car(Agent):
    rand_probability = config.RANDOMIZE_VELOCITY_PROBABILITY
    spawn_probability = config.SPAWN_PROBABILITY

    def __init__(self, unique_id, model, road_length):
        super().__init__(unique_id, model)
        self.road_length = road_length
        self.min_velocity = 0
        self.max_velocity = 5
        self.velocity = random.randint(self.min_velocity, self.max_velocity)

    def step(self):
        lane_changed = self.should_change_lane()

        if lane_changed:
            self.change_lane()
        else:
            # 1.Acceleration
            self.increase_velocity()

            # 2. Slow down not to hit car ahead
            self.slow_down()

            # 3. Randomization
            self.randomize_velocity(self.rand_probability)

        # 4. Car motion
        self.move_or_remove_car()

    def change_lane(self):
        lane_to_change = self.get_lane_to_change()
        self.model.grid.move_agent(self, (self.pos[0], lane_to_change))

    def should_change_lane(self):
        # 1. has car moving slower ahead
        if not self.lane_should_be_changed():
            return False

        # 2. no car ahead on other (opposite) lane
        if not self.has_enough_space_ahead_on_opposite_lane():
            return False

        # 3. no car is moving behind on other (opposite) lane
        if not self.has_enough_space_behind_on_opposite_lane():
            return False

        return True

    def lane_should_be_changed(self):
        lane_to_change = self.get_lane_to_change()
        if lane_to_change == 0:
            return True
        for i in range(self.pos[0] + 1, self.pos[0] + self.max_velocity):
            try:
                if not(self.model.grid.is_cell_empty((i, self.pos[1]))):
                    return True
            except IndexError:
                return False
        return False

    def has_enough_space_ahead_on_opposite_lane(self):
        lane_to_change = self.get_lane_to_change()
        for i in range(self.pos[0] + 1, self.pos[0] + self.velocity):
            try:
                if not (self.model.grid.is_cell_empty((i, lane_to_change))):
                    return False
            except IndexError:
                return False
        return True

    def has_enough_space_behind_on_opposite_lane(self):
        lane_to_change = self.get_lane_to_change()
        for i in range(self.pos[0] - self.velocity, self.pos[0] + 1):
            try:
                if not (self.model.grid.is_cell_empty((i, lane_to_change))):
                    return False
            except IndexError:
                return False
        return True

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
            cell = self.model.grid.get_cell_list_contents([(i, position[1])])
            if len(cell) > 0:
                if not(self.model.grid.is_cell_empty((i, position[1]))) and not(type(cell[0]) == entrance.Entrance) and not(type(cell[0]) == exit.Exit):
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
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
        else:
            self.model.grid.move_agent(self, (new_position, self.pos[1]))

    def get_lane_to_change(self):
        try:
            if self.pos[1] == 0:
                return 1
            return 0
        except:
            return 0
