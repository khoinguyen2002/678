import pygame
from game_object import GameObject
from physics.box_collider import Boxcollider
from game_object import collide_with
from enemy.enemy import Enemy
class PlayerBullet(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load('image/bullet.png')
        self.box_collider = Boxcollider(30,95)
    def update(self):
        GameObject.update(self)
        collide_list = collide_with(self.box_collider)
        for game_object in collide_list:
            if type(game_object) == Enemy:
                game_object.deactivate()
                self.deactivate()
        self.move()
        self.deactivate_if_needed()

    def move(self):
        self.y -= 5

    def deactivate_if_needed(self):
        if self.y <= 0:
            self.deactivate()
