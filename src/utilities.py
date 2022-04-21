#utilities.py

foodsize = 30
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)
AREA = 30

def compreso(num, low, high):
    """
    checks whether or not a number is between low and high
    """
    return num>=low and num<=high


if __name__ == '__main__':
    startx = 20
    starty = 40
    finishx = finishy = 60
    slope = (startx-finishx)/(starty-finishy)
    print(slope)
