from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from simulation import Simulation


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": agent.color,
                 "r": 0.7}
    return portrayal


if __name__ == '__main__':
    grid = CanvasGrid(agent_portrayal, 100, 2, 500, 100)
    server = ModularServer(Simulation,
                           [grid],
                           "Traffic simulation",
                           {"width": 100, "height": 2})
    server.port = 8521
    server.launch()

