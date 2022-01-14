from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from road.construction import Construction
from road.entrance import Entrance
from road.exit import Exit

from simulation import Simulation
from cars.sports_car import SportsCar
from cars.family_car import FamilyCar
from cars.truck import Truck

from visualization.HighwayModule import HighwayModule


def agent_portrayal(agent):
    if isinstance(agent, FamilyCar):
        return {"Shape": "rect",
                "Filled": "true",
                "Layer": 0,
                "Color": "blue",
                "w": 0.8,
                "h": 0.1}
    elif isinstance(agent, Truck):
        return {"Shape": "rect",
                "Filled": "true",
                "Layer": 0,
                "Color": "green",
                "w": 1,
                "h": 0.1}
    elif isinstance(agent, SportsCar):
        return {"Shape": "rect",
                "Filled": "true",
                "Layer": 0,
                "Color": "red",
                "w": 0.5,
                "h": 0.1}
    elif isinstance(agent, Construction):
        return {"Shape": "rect",
                "Filled": "true",
                "Layer": 1,
                "Color": "black",
                "w": 0.8,
                "h": 0.8}
    elif isinstance(agent, Entrance):
        return {"Shape": "rect",
                "Filled": "true",
                "Layer": 1,
                "Color": "yellow",
                "w": 0.8,
                "h": 0.8}
    elif isinstance(agent, Exit):
        return {"Shape": "rect",
                "Filled": "true",
                "Layer": 1,
                "Color": "orange",
                "w": 0.8,
                "h": 0.8}


if __name__ == '__main__':
    # grid = CanvasGrid(agent_portrayal, 100, 2, 500, 30)
    highway = HighwayModule(list(range(1)), 100, 1000)

    server = ModularServer(Simulation,
                           [highway],
                           "Traffic simulation",
                           {"width": 100, "height": 2})
    server.port = 8521
    server.launch()

