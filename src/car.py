import numpy as np

class Car:
    distance = 0

    def __init__(self, minVelocity, maxVelocity):
        import random
        self.color = random.randint(0,200)
        self.velocity = random.randint(minVelocity,maxVelocity)
    
    def increaseVelocity(self,maxVelocity):
        self.velocity = min(maxVelocity, self.velocity+1)
        return
    
    def setVelocity(self, newVelocity,maxVelocity):
        if newVelocity <= maxVelocity:
            self.velocity = newVelocity
        
    def randomizeVelocity(self, probability):
        if self.velocity < 1:
            return
        
        score = np.random.choice([1,0], p=[probability, 1-probability])
        
        self.velocity = max(1,self.velocity-score)
        
        return
                
    def getColor(self):
        return self.color
    
    def isEmpty(self):
        return false
    
    def setDistance(self,distance):
        self.distance = distance