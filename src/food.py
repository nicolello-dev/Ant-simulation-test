#food.py

from utilities import SCREEN_HEIGHT, SCREEN_WIDTH, foodsize
import pygame

class Food():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = foodsize
        self.hp = 1000
    
    def __repr__(self):
        return f"x: {self.x}, y: {self.y}, hp:{self.hp}"

    def newrandomcoor(self, size):
        """
        returns two random food x and y coordinates
        """
        import random
        self.x = random.randint(0+size, SCREEN_WIDTH-size)
        self.y = random.randint(0+size, SCREEN_HEIGHT-size)
        self.hp = 1000
    
    def draw(self, SCREEN:pygame.display):
        pygame.draw.circle(SCREEN, (0, 255, 0), (self.x, self.y), self.size)