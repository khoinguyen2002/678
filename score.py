import pygame
width = 800
height = 640
display_surf = pygame.display.set_mode((width, height))
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
    def __init__(self, x, y, score, size):
        self.x = x
        self.y = y
        self.score = score
        self.size = size
        self.font = pygame.font.Font(None, self.size)
        self.high_score = 0
    def display(self):
        display_high_score = self.font.render(" Best score " + str(self.high_score), True, color['white'])
        display_score = self.font.render(' Score ' + str(self.score), True, color['white'])
        display_surf.blit(display_score, (self.x, self.y))
        display_surf.blit(display_high_score, (self.x, self.y + 20))