import pygame
from player.player import Player
import game_object
from enemy.enemy_spawner import EnemySpawner
from input.input_manager import InputManager
import random
BG = (255, 255, 0)

pygame.init()


SIZE = (800,640)
canvas = pygame.display.set_mode(SIZE)


clock = pygame.time.Clock()

loop = True

input_manager =InputManager()

player = Player(600, 650, input_manager)

game_object.add(player)
game_object.add(EnemySpawner())

while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    game_object.update()

    canvas.fill(BG)
    game_object.render(canvas)
    pygame.display.set_caption('shoot')
    pygame.display.flip()
    clock.tick(60)