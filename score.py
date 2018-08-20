import pygame
class ScoreBoard:
    def __init__(self, score):
        self.score = score

    def display(self):
        pygame.display.set_caption("Shoot. Score: " + str(self.score))
    def draw_arena(self):
        self.scoreboard.display()