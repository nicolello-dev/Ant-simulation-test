#utilities.py

foodsize = 30
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)
AREA = 30

def calculateapproach(x, y, xspeed, yspeed, objx=SCREEN_WIDTH/2, objy=SCREEN_HEIGHT/2):
    """
    calculates the speed in the x and y axis and gives the ant a reasonable speed
    """
    xdist = x - objx
    ydist = y - objy
    if xdist != 0 and ydist != 0:
        summ = xspeed + yspeed
        const = xdist/ydist
        yspeed = summ/(const+1)
        xspeed = yspeed * const
        yspeed = -abs(yspeed) if y > objy else abs(yspeed)
        xspeed = -abs(xspeed) if x > objx else abs(xspeed)
        if abs(xspeed) < 0.25 or abs(yspeed) < 0.25:
            xspeed, yspeed = xspeed * 4, yspeed * 4
        return xspeed, yspeed
    if xdist == 0:
        return 0, yspeed
    return xspeed, 0


if __name__ == '__main__':
    startx = 20
    starty = 40
    finishx = finishy = 60
    slope = (startx-finishx)/(starty-finishy)
    print(slope)
