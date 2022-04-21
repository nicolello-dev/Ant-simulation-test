#ant.py

from utilities import SCREEN_WIDTH, SCREEN_HEIGHT, compreso
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
    
    def nextstep(self, foodx, foody, size, tofood=False):
        """
        changes ant.x and ant.y
        """

        def inratio(num1, num2, highest):
            high = max(num1, num2)
            low = min(num2, num1)
            ratio = high/highest
            high = highest
            low = low * ratio
            if num1 > num2:
                return high, low
            return low, high


        if (compreso(self.x, foodx-size, foodx+size) and compreso(self.y, foody-size, foody+size)) or self.returningtobase or tofood: # if the ant is returning to base or has just eaten the food
            if (not tofood): self.returningtobase = True
            if compreso(self.x, (SCREEN_WIDTH/2)-20, (SCREEN_WIDTH/2)+20) and compreso(self.y, (SCREEN_HEIGHT/2)-20, (SCREEN_HEIGHT/2)+20): #if the ant has arrived to the base
                self.returningtobase = False
                #give a new movement speed to wander again
                self.xmovement = random.randrange(10, 100) / 100
                self.xmovement = {0:self.xmovement, 1:-self.xmovement}[random.randint(0, 1)]
                self.ymovement = random.randrange(10, 100) / 100
                self.ymovement = {0:self.ymovement, 1:-self.ymovement}[random.randint(0, 1)]
                
            elif not tofood: #if the ant is returning to base
                self.xmovement, self.ymovement = self.calculateapproach(self.x, self.y, self.xmovement, self.ymovement) #make it go in the direction of the nest
            else:
                self.xmovement, self.ymovement = self.calculateapproach(self.x, self.y, self.xmovement, self.ymovement, foodx, foody) #make it go in the direction of the nest
        #modify randomly the movement speed
        self.xmovement += (random.randrange(0, 30) / 300) - 0.05
        self.ymovement += (random.randrange(0, 30) / 300) - 0.05

        if self.xmovement > 2 or self.ymovement > 2:
            self.xmovement, self.ymovement = inratio(self.xmovement, self.ymovement, 2)

        if self.x >= SCREEN_WIDTH or self.x <= 0: #make it bounce
            self.xmovement = -self.xmovement
        if self.y >= SCREEN_HEIGHT or self.y <= 0: #make it bounce
            self.ymovement = -self.ymovement

        self.x += self.xmovement #change the position
        self.y += self.ymovement #change the position

        tofood=False

    def calculateapproach(self, x, y, xspeed, yspeed, objx=SCREEN_WIDTH/2, objy=SCREEN_HEIGHT/2):
        """
        calculates the speed in the x and y axis and gives the ant a reasonable speed
        """
        xdist = x - objx
        ydist = y - objy
        if xdist == 0:
            return 0, yspeed
        if ydist != 0:
            summ = xspeed + yspeed
            const = xdist/ydist
            yspeed = summ/(const+1)
            xspeed = yspeed * const
            yspeed = -abs(yspeed) if y > objy else abs(yspeed)
            xspeed = -abs(xspeed) if x > objx else abs(xspeed)
            if abs(xspeed) < 0.25 or abs(yspeed) < 0.25:
                xspeed, yspeed = xspeed * 4, yspeed * 4
            return xspeed, yspeed
        return xspeed, 0

        
        