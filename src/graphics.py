#graphics.py

from ant import ant 
from utilities import SCREEN_HEIGHT, SCREEN_WIDTH, RED, BLUE, foodsize
import pygame
import random

ants = []
for _ in range(2):
    a = ant(100)
    ants.append(a)

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
food = False

def foodcoor(size):
    return random.randint(0+size, SCREEN_WIDTH-size), random.randint(0+size, SCREEN_HEIGHT-size), True

while True:
    SCREEN.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if not food:
        foodx, foody, food = foodcoor(foodsize)
    
    pygame.draw.circle(SCREEN, (0, 255, 0), (foodx, foody), 5)

        
    pygame.draw.circle(SCREEN, (100, 100, 255), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 20) #nest

    for ant in ants:
        pygame.draw.circle(SCREEN, {False:RED, True:BLUE}[ant.returningtobase], (ant.x, ant.y), 3)
        ant.nextstep(foodx, foody, foodsize)
        
    pygame.display.update()