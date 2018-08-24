import pygame
import time

class InputManager:
    def __init__(self):
        self.right_pressed = False
        self.left_pressed = False
        self.down_pressed = False
        self.up_pressed = False
        self.x_pressed = True

    def __str__(self):
        return '''right: {0} left: {1} down: {2} up: {3} x: {4}'''.format(
            self.right_pressed,
            self.left_pressed,
            self.down_pressed,
            self.up_pressed,
            self.x_pressed)

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.right_pressed = True
            elif event.key == pygame.K_LEFT:
                self.left_pressed = True
            elif event.key == pygame.K_DOWN:
                self.down_pressed = True
            elif event.key == pygame.K_UP:
                self.up_pressed = True
            elif event.key == pygame.K_x:
                self.x_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right_pressed = False
            elif event.key == pygame.K_LEFT:
                self.left_pressed = False
            elif event.key == pygame.K_DOWN:
                self.down_pressed = False
            elif event.key == pygame.K_UP:
                self.up_pressed = False
            elif event.key == pygame.K_x:
                self.x_pressed = False
    def update2(self, flagMove):

            if flagMove == 1:
                self.right_pressed = True
                time.sleep(0.01)
            if flagMove == 2:
                self.left_pressed = True
                time.sleep(0.01)
            if flagMove == 0:
                self.right_pressed = False
                self.left_pressed = False
            if flagMove == 4:
                self.up_pressed = True
                time.sleep(0.01)
            # if flagMove == 5:
            #     self.down_pressed = True
            #     time.sleep(0.01)
            # if flagMove == 6:
            #     self.up_pressed = False
            #     self.down_pressed = False


                #self.down_pressed = False
                #self.up_pressed = False