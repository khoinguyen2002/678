import pygame
from player.player import Player
import game_object
from enemy.enemy import Enemy
from enemy.enemy_spawner import EnemySpawner
from input.input_manager import InputManager
import random
from threading import Thread
from player import face_detection
from score import ScoreBoard
Game_Global = True
scoreboard = ScoreBoard(400, 10, 0)
x_old = 0
y_old = 0

BG = (255, 255, 0)

pygame.init()
pygame.display.set_caption('shoot')
clock = pygame.time.Clock()
SIZE = (800, 640)
canvas = pygame.display.set_mode(SIZE)


def play_audio():
    global Game_Global
    pygame.mixer.music.load("nhac/nhac.mp3")
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy() and Game_Global:
        pygame.event.poll()
        clock.tick(10)


thread_audio = Thread(target=play_audio)
thread_audio.start()


def Check_move(x_new, y_new):
    print("x_new:", x_new, y_new)
    global x_old
    global y_old
    if x_old == 0 and y_old == 0:
        x_old = x_new
        y_old = y_new
        return 0  # ko di chuyển
    if (x_new - x_old) > 5:
        x_old = x_new
        return 1  
    if (x_new - x_old) < -5:
        x_old = x_new
        return 2
    if (5 < x_new - x_old < 5):
        return 0


webcam = face_detection.Webcam()
webcam.update()

loop = True

input_manager = InputManager()

player = Player(600, 500, input_manager)

game_object.add(player)
game_object.add(EnemySpawner())
img = pygame.image.load('image/heart.png')

while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            xnew, ynew = webcam.getpos
            print(xnew,ynew)
            print(x_old, y_old)
            flagmove = Check_move(xnew, ynew)
            # input_manager.update(event)
            input_manager.update2(flagmove)

    hp_count = 0

    for obj in game_object.game_objects:
        if type(obj) == Enemy:
            if obj.is_active == False and obj.y > 627:
                hp_count += 1
    player.hp = 10
    player.hp -= hp_count

    if player.hp <= 0:
        player.is_active = False
    game_object.update()

    if player.is_active == False:
        Game_Global = False
        thread_audio.join()
        canvas.fill((0, 0, 0))
        text = str("Game Over")
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(text, True, (255, 255, 255))
        text_width = text.get_width()
        text_height = text.get_height()
        canvas.blit(text, (400 - text_width / 2, 320 - text_height / 2))
    else:
        BG = pygame.image.load("image/background.123.jpg")
        canvas.blit(BG, (0, 0))
        # canvas.fill(BG)
        game_object.render(canvas)
        scoreboard.display(canvas)
        img = pygame.transform.scale(img, (30, 30))
        for i in range(player.hp):
            canvas.blit(img, (10 + i * 30, 10))
    pygame.display.flip()
    clock.tick(60)