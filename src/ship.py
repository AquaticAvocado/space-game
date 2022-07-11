import pygame

import constants as c

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load('sprites/ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (c.SHIP_SIZE, c.SHIP_SIZE))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.x = (c.SCREEN_WIDTH/2) - (c.SHIP_SIZE/2)
        self.rect.y = c.SCREEN_HEIGHT - c.SHIP_SIZE
        self.x_vel = 0
        self.y_vel = 0
        self.speed = 10
        
    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel