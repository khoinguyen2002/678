import pygame
from game_object import GameObject
from physics.box_collider import Boxcollider

class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("image/ENEMY.png")
        self.box_collider = Boxcollider(75,60)
    def update(self):
        GameObject.update(self)
        self.y += 3
