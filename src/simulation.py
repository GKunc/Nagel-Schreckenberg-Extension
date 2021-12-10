import matplotlib.pyplot as plt
import numpy as np


from car import Car
from road import Road

class Simulation:
    # Parameters
    roadLength = 50
    minVelocity = 0
    maxVelocity = 5
    grid = [Road()] * roadLength

    rand_probability = 0.5
    spawn_probability = 0.2

    def __init__(self, roadLength):
        # Initialize grid 
        self.grid[0] = Car(self.minVelocity, self.maxVelocity) 
        self.grid[1] = Car(self.minVelocity, self.maxVelocity) 
        self.grid[2] = Car(self.minVelocity, self.maxVelocity) 
        self.grid[3] = Car(self.minVelocity, self.maxVelocity) 
        self.grid[8] = Car(self.minVelocity, self.maxVelocity) 
        self.grid[9] = Car(self.minVelocity, self.maxVelocity) 

    def show(self, im):
        im.set_data(np.array(list(map(lambda x : x.getColor(), self.grid))).reshape(1, self.roadLength))


    def update(self, frameNum, im):
        if(frameNum == 0):
            self.show(im)
        else:
            carPositions = [(i, self.grid[i]) for i in range(len(self.grid)) if type(self.grid[i]) is Car]
    # 1.Acceleration
            for (p, car) in carPositions:            
                car.increaseVelocity(self.maxVelocity)

    # 2. Slow down                    
            pairs = list(zip(carPositions, carPositions[1:]))
            pairs.append((carPositions[-1], carPositions[0]))
            for p in pairs:
                ((p1, carA), (p2, carB)) = p
                distance = ((p2 - p1 + self.roadLength) % self.roadLength) - 1
                newVelocity = min(carA.velocity, distance)
                carA.setVelocity(newVelocity, self.maxVelocity)

            # 3. Randomization
            for i in self.grid:
                if type(i) is Car:
                    i.randomizeVelocity(self.rand_probability)


    # 4. Car motion
            newGrid = [Road()] * self.roadLength        
            for (p, car) in carPositions:
                newGrid[(p+car.velocity)%self.roadLength] = car

            self.grid[:] = newGrid[:] 

            score = np.random.choice([1,0], p=[self.spawn_probability, 1-self.spawn_probability])
            if score and type(self.grid[0]) is not Car:
                self.grid[0] = Car(self.minVelocity, self.maxVelocity)

            self.show(im)
        return im

