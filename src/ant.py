#ant.py

from utilities import SCREEN_WIDTH, SCREEN_HEIGHT
import random
#0 is right, 90 is up, 180 is left, 270 is down
class ant():
    def __init__(self, multiplier=1):
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2
        self.xmovement = random.randrange(0, 100) / 100
        self.xmovement = {0:self.xmovement, 1:-self.xmovement}[random.randint(0, 1)]
        self.ymovement = random.randrange(0, 100) / 100
        self.ymovement = {0:self.ymovement, 1:-self.ymovement}[random.randint(0, 1)]
        self.returningtobase = False
        self.xmovement *= multiplier
        self.ymovement *= multiplier
    def nextstep(self, foodx, foody, size):
        """
        changes ant.x and ant.y
        """

        if self.x in range(foodx-size, foodx+size) and self.y in range(foody-size, foody+size):
            self.returningtobase = True
        
        if self.returningtobase:
            pass

        if self.x >= SCREEN_WIDTH or self.x <= 0:
            self.xmovement = -self.xmovement
        if self.y >= SCREEN_HEIGHT or self.y <= 0:
            self.ymovement = -self.ymovement

        self.x -= self.xmovement
        self.y -= self.ymovement

        
        