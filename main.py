import pygame
from player.player import Player
import game_object
from enemy.enemy import Enemy
from enemy.enemy_spawner import EnemySpawner
from input.input_manager import InputManager
import random
from threading import Thread
from player import face_detection
from player import  play_audio
import  score
from score import ScoreBoard
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,20)

Game_Global = True

x_old = 0
y_old = 0


BG = (255, 255, 0)

pygame.init()
pygame.display.set_caption('shoot')
clock = pygame.time.Clock()
SIZE = (800,640)
canvas = pygame.display.set_mode(SIZE)

def Check_move(x_new,y_new):
    global x_old
    global y_old
    if(x_new > 0 and y_new >0):
        if x_old ==0 and y_old == 0:
            x_old = x_new
            y_old = y_new
            return 0 # ko di chuyển
        if (x_new - x_old) > 5:
            x_old = x_new
            return 1 #1 di chuyển sang phải
        if (x_new - x_old)< -5:
            x_old = x_new
            return 2 # 2 di chuyển sang trái
        if (-5 < (x_new - x_old) <5):
            return 0 #không di chuyển

    else:
        return 0
def Check_move1(x_new,y_new):
    global x_old
    global y_old
    if (x_new > 0 and y_new > 0):
        if x_old == 0 and y_old == 0:
            x_old = x_new
            y_old = y_new
            return 3  # ko di chuyển
        if (x_new - x_old) > 4:
            x_old = x_new
            return 4  # 1 di chuyển lên trên
        if (x_new - x_old) < -4:
            x_old = x_new
            return 5  # 2 di chuyển xuống dưới
        if (-4 < (x_new - x_old) < 4):
            return 6  # không di chuyển


webcam = face_detection.Webcam()
webcam.update()

loop = True
input_manager =InputManager()

player = Player(600, 500, input_manager)
game_object.add(player)
game_object.add(EnemySpawner())
img = pygame.image.load('image/heart.png')

pl = play_audio.audio()
pl.update()
while loop:
    events = pygame.event.get()
    (xnew, ynew) = webcam.getpos
    flagmove = Check_move(xnew, ynew)
    input_manager.update2(flagmove)
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
    hp_count = 0
    for obj in game_object.game_objects:
        if type(obj) == Enemy:
            if obj.is_active == False and obj.y > 627:
                hp_count += 1
    player.hp = 5
    player.hp -= hp_count

    if player.hp <= 0:
        player.is_active = False
    game_object.update()

    if player.is_active == False:
        Game_Global = False
        pl.stop_audio()
        #thread_audio.setDaemon(True)
        canvas.fill((0,0,0))
        text = str("Game Over")
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(text, True, (255,255,255))
        text_width = text.get_width()
        text_height = text.get_height()
        canvas.blit(text, (400 - text_width/2, 320 - text_height/2 ))
    else:
        canvas.fill(BG)
        game_object.render(canvas)
        img = pygame.transform.scale(img, (30, 30))
        for i in range(player.hp):

            canvas.blit(img, (10+ i*30, 10 ))
    pygame.display.flip()
    clock.tick(60)