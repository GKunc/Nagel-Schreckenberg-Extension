from mesa.visualization.ModularVisualization import VisualizationElement

import cars.truck
import road.construction
from cars.family_car import FamilyCar
from cars.sports_car import SportsCar
from cars.truck import Truck


class HighwayModule(VisualizationElement):
    package_includes = ["Chart.min.js"]
    local_includes = ["visualization/HighwayModule.js"]

    def __init__(self, canvas_height, canvas_width):
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        new_element = "new HighwayModule({}, {})"
        new_element = new_element.format(
                                         canvas_width,
                                         canvas_height)
        self.js_code = "elements.push(" + new_element + ");"

    def render(self, model):
        car_agents = []
        for agent in model.schedule.agents:
            if agent.pos is not None:
                if type(agent) == cars.truck.Truck:
                    car_agents.append({"type": "Truck", "x": int(agent.pos[0]), "y": int(agent.pos[1])})
                elif type(agent) == cars.family_car.FamilyCar:
                    car_agents.append({"type": "FamilyCar", "x": int(agent.pos[0]), "y": int(agent.pos[1])})
                elif type(agent) == cars.sports_car.SportsCar:
                    car_agents.append({"type": "SportsCar", "x": int(agent.pos[0]), "y": int(agent.pos[1])})
                elif type(agent) == road.construction.Construction:
                    car_agents.append({"type": "Construction", "x": int(agent.pos[0]), "y": int(agent.pos[1])})
                elif type(agent) == road.exit.Exit:
                    car_agents.append({"type": "Exit", "x": int(agent.pos[0]), "y": int(agent.pos[1])})
                elif type(agent) == road.entrance.Entrance:
                    car_agents.append({"type": "Entrance", "x": int(agent.pos[0]), "y": int(agent.pos[1])})

        return car_agents
