from utilities import SCREEN_WIDTH, SCREEN_HEIGHT
import random
#0 is right, 90 is up, 180 is left, 270 is down
class ant():
    def __init__(self):
        self.x = random.randrange(SCREEN_WIDTH)
        self.y = random.randrange(SCREEN_HEIGHT)
        self.xmovement = random.randrange(0, 100) / 100
        self.ymovement = random.randrange(0, 100) / 100
    def nextstep(self):
        self.x += (random.randrange(0, 50) -25) / 25
        if self.x >= SCREEN_WIDTH -2:
            self.xmovement = -self.xmovement
        if self.y >= SCREEN_HEIGHT -2:
            self.ymovement = -self.xmovement
            

a = ant()

for _ in range(50):
    print(a.xmovement, a.ymovement)
    a.nextstep()

        