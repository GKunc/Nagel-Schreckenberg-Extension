import numpy as np
from mesa import Agent
from road import exit

class Exit(Agent):
    exit_probability = 0.1

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        score = np.random.choice([1, 0], p=[self.exit_probability, 1 - self.exit_probability])
        if score:
            for i in range(self.pos[0] - 3, self.pos[0] + 3):
                cell = self.model.grid.get_cell_list_contents([(i, self.pos[1])])
                if len(cell) == 0:
                    continue
                elif len(cell) == 1 and not(type(cell[0]) == exit.Exit):
                    car = cell[0]
                    self.model.grid.remove_agent(car)
                    self.model.schedule.remove(car)
                if (type(cell[0]) == exit.Exit) and len(cell) > 1:
                    car = cell[1]
                    self.model.grid.remove_agent(car)
                    self.model.schedule.remove(car)