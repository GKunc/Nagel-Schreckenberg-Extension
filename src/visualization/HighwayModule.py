from mesa.visualization.ModularVisualization import VisualizationElement

import cars.truck
import road.construction
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
            print(type(agent))
            print(type(agent.pos))
            if type(agent) == cars.truck.Truck:
                car_agents.append({"type": "Truck", "pos": agent.pos})
            elif type(agent) == cars.family_car.FamilyCar:
                car_agents.append({"type": "FamilyCar", "pos": agent.pos})
            elif type(agent) == cars.sports_car.SportsCar:
                car_agents.append({"type": "SportsCar", "pos": agent.pos})
            elif type(agent) == road.construction.Construction:
                car_agents.append({"type": "Construction", "pos": agent.pos})

        return car_agents
