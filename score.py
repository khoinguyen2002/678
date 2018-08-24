import pygame
color = {
    'white': (255, 255, 255),
    'bright_white': (255, 255, 200),
    'blue': (0, 0, 255),
    'bright_blue': (117, 156, 255),
    'green': (0, 200, 0),
    'black': (0, 0, 0),
    'bright_green': (0, 255, 0),
    'red': (200,0,0),
    'bright_red': (255,0,0),
    'yellow': (200,200,0),
    'bright_yellow': (255,255,0),
}

class ScoreBoard:
    def __init__(self, x, y, score):
        self.x = x
        self.y = y
        self.score = score
        self.high_score = 0
    def display(self, canvas):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        display_high_score = font.render(" Best score " + str(self.high_score), True, (255,255,255))
        display_score = font.render(' Score ' + str(self.score), True, (255,255,255))
        canvas.blit(display_score, (self.x, self.y))
        canvas.blit(display_high_score, (self.x, self.y + 20))
