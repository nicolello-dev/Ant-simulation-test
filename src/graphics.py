#graphics.py

from ant import ant 
from utilities import SCREEN_HEIGHT, SCREEN_WIDTH, RED, BLUE, foodsize, BACKGROUND_COLOR
import pygame
import random

ants = [] #list that will be accessed to control every ant
for _ in range(1000):
    a = ant()
    ants.append(a)

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
food = False

def foodcoor(size):
    """
    returns two random food x and y coordinates
    """
    return random.randint(0+size, SCREEN_WIDTH-size), random.randint(0+size, SCREEN_HEIGHT-size), True, 20

def compreso(num, low, high):
    """
    checks whether or not a number is between low and high
    """
    return num>=low and num<=high

while True:

    pherormones = []

    SCREEN.fill(BACKGROUND_COLOR) #background color, can be changed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if not food: #creates a new food if the food is not present (useful in the future )
        foodx, foody, food, foodlife = foodcoor(foodsize)
    
    pygame.draw.circle(SCREEN, (0, 255, 0), (foodx, foody), foodsize) #food

        
    pygame.draw.circle(SCREEN, (100, 100, 255), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 20) #nest

    for ant in ants:
        if ant.returningtobase:
            pherormones.append((ant.x, ant.y))
        else:
            for item in pherormones:
                if compreso(ant.x, item[0]-5, item[0]+5) and compreso(ant.y, item[1]-5, item[1]+5):
                    ant.nextstep(foodx, foody, foodsize, tofood=True) 
        pygame.draw.circle(SCREEN, {False:RED, True:BLUE}[ant.returningtobase], (ant.x, ant.y), 3) #draws the ant
        ant.nextstep(foodx, foody, foodsize) #changes the ant's x and y coordinates depending on their x and y speed. it also changes the x and y speeds by a little randomly
        
    pygame.display.update()