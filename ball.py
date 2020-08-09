import pygame
import random
from random import randint
import time 

BLACK = (0, 0, 0)
 
class Ball(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [random.choice([1,-1])*4,randint(-8,8)]
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        sign = self.velocity[0]/abs(self.velocity[0])
        self.velocity[0] = -1 * sign * 7
        self.velocity[1] = randint(-8,8)

    def aPoint(self):
        self.rect.x = 345
        self.rect.y = 195
        self.velocity = [4,randint(-4,4)]
        
    def bPoint(self):
        self.rect.x = 345
        self.rect.y = 195
        self.velocity = [-4,randint(-4,4)]