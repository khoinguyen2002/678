import pygame
width = 800
height = 640
display_surf = pygame.display.set_mode((width, height))
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