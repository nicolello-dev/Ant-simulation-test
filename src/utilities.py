#utilities.py

foodsize = 30
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def calculateapproach(x, y, xspeed, yspeed, objx, objy):
    xdist = x - objx
    ydist = y - objy
    if xdist != 0 and ydist != 0:
        summ = xspeed + yspeed
        const = xdist/ydist
        yspeed = summ/(const+1)
        xspeed = yspeed * const
        return xspeed, yspeed
    if xdist == 0:
        return 0, yspeed
    return xspeed, 0
