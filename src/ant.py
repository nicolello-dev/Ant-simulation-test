#ant.py

from utilities import SCREEN_WIDTH, SCREEN_HEIGHT, calculateapproach, allpeopleinarea
import random
#0 is right, 90 is up, 180 is left, 270 is down
class ant():
    def __init__(self, multiplier:int=1):
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2
        self.xmovement = random.randrange(10, 100) / 100
        self.xmovement = {0:self.xmovement, 1:-self.xmovement}[random.randint(0, 1)]
        self.ymovement = random.randrange(10, 100) / 100
        self.ymovement = {0:self.ymovement, 1:-self.ymovement}[random.randint(0, 1)]
        self.returningtobase = False
        self.xmovement *= multiplier
        self.ymovement *= multiplier
    def nextstep(self, foodx, foody, size):
        """
        changes ant.x and ant.y
        """

        def compreso(num, low, high):
            """
            checks whether or not a number is between low and high
            """
            return num>=low and num<=high


        if (compreso(self.x, foodx-size, foodx+size) and compreso(self.y, foody-size, foody+size)) or self.returningtobase: # if the ant is returning to base or has just eaten the food
            self.returningtobase = True
            if compreso(self.x, (SCREEN_WIDTH/2)-20, (SCREEN_WIDTH/2)+20) and compreso(self.y, (SCREEN_HEIGHT/2)-20, (SCREEN_HEIGHT/2)+20): #if the ant has arrived to the base
                self.returningtobase = False
                #give a new movement speed to wander again
                self.xmovement = random.randrange(10, 100) / 100
                self.xmovement = {0:self.xmovement, 1:-self.xmovement}[random.randint(0, 1)]
                self.ymovement = random.randrange(10, 100) / 100
                self.ymovement = {0:self.ymovement, 1:-self.ymovement}[random.randint(0, 1)]
                
            else: #if the ant is returning to base
                self.xmovement, self.ymovement = calculateapproach(self.x, self.y, self.xmovement, self.ymovement) #make it go in the direction of the nest
        else: #if the ant is wandering
            if False: #allpeopleinarea(self.x, self.y, foodx, foody, SCREEN_HEIGHT/2, SCREEN_WIDTH/2, 10): #if the ant is in the pherormone area
                self.xmovement, self.ymovement = calculateapproach(self.x, self.y, self.xmovement, self.ymovement)
            else: #if the ant is in any other place in the map
                #modify randomly the movement speed
                self.xmovement += (random.randrange(0, 30) / 300) - 0.05
                self.ymovement += (random.randrange(0, 30) / 300) - 0.05
    
        if self.x >= SCREEN_WIDTH or self.x <= 0: #make it bounce
            self.xmovement = -self.xmovement
        if self.y >= SCREEN_HEIGHT or self.y <= 0: #make it bounce
            self.ymovement = -self.ymovement

        self.x += self.xmovement #change the position
        self.y += self.ymovement #change the position

        
        