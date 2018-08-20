import pygame
from player.player_bullet import PlayerBullet
import game_object
from game_object import GameObject
from frame_counter import FrameCounter


class Player(GameObject):

    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load('image/player.png')
        self.input_manager = input_manager
        self.shoot_lock = False
        self.counter = FrameCounter(30)
        self.hp = 10

    def update(self):
        GameObject.update(self)

        for i in range(3):
            self.move()
            self.shoot()

    def move(self):
        dx = 0
        dy = 0
        delta = 10
        if self.input_manager.right_pressed:
            if self.x + delta > 775:
                dx = 0
            else:
                dx += delta
        if self.input_manager.left_pressed:
            if self.x - delta < 27:
                dx = 0
            else:
                dx -= delta
        if self.input_manager.down_pressed:
            if self.y + delta > 600:
                dy = 0
            else:
                dy += delta
        if self.input_manager.up_pressed:
            if self.y - delta < 40:
                dy = 0
            else:
                dy -= delta

        self.x += dx
        self.y += dy

    def shoot(self):
        if self.input_manager.x_pressed and not self.shoot_lock:
            game_object.recycle(PlayerBullet, self.x, self.y - 40)
            self.shoot_lock = True

        if self.shoot_lock:
            self.counter.run()
            if self.counter.expired:
                self.shoot_lock = False
                self.counter.reset()
