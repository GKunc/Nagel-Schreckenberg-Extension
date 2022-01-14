from mesa.visualization.ModularVisualization import VisualizationElement
import numpy as np

import cars.truck
from cars.family_car import FamilyCar
from cars.sports_car import SportsCar
from cars.truck import Truck


class HighwayModule(VisualizationElement):
    package_includes = ["Chart.min.js"]
    local_includes = ["visualization/HighwayModule.js"]

    def __init__(self, bins, canvas_height, canvas_width):
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        self.bins = bins
        new_element = "new HighwayModule({}, {}, {})"
        new_element = new_element.format(bins,
                                         canvas_width,
                                         canvas_height)
        self.js_code = "elements.push(" + new_element + ");"

    def render(self, model):
        car_agents = []
        for agent in model.schedule.agents:
            if type(agent) == cars.truck.Truck:
                print(agent.pos)
                car_agents.append({"type": "Truck", "pos": agent.pos})
            elif type(agent) == cars.family_car.FamilyCar:
                print(agent.pos)
                car_agents.append({"type": "FamilyCar", "pos": agent.pos})
            elif type(agent) == cars.sports_car.SportsCar:
                print(agent.pos)
                car_agents.append({"type": "SportsCar", "pos": agent.pos})

        return car_agents
