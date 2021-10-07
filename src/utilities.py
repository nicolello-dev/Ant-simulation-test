#utilities.py

foodsize = 30
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)

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


def allpeopleinarea(x, y, startx, starty, finishx, finishy, height):
    """
    returns whether or not the ant is in a rectangle between the food center and the base with height height
    """

    #first determine the slope of the line connecting the two dots
    #slope of a line is deltax/deltay
    slope = -(startx-finishx)/(starty-finishy)
    #now the equation of the line will be
    #y=slope*x + b
    #let's find b
    b = finishy - (slope*finishx)
    #now let's define a range of b's
    rangeslope = [b-(height/2), b+(height/2)]
    #ok now let's checl whether or not the points are part of said line in said range.
    #if that;s the case then y will be between the results of slope max and min
    ymin = slope * x + rangeslope[0]
    ymax = slope * x + rangeslope[1]
    if y>=ymin and y<=ymax: #if in the boundary
        if y >= min(starty, finishx) and y <= max(starty, finishy): #if between the food and the nest
            return True
    #in any other case
    return False