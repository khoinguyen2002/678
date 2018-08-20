from threading import Thread
import pygame

class audio:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load("nhac/nhac.mp3")
        self.clock = pygame.time.Clock()
    def play_audio(self):
        pygame.mixer.music.play(0)
        while pygame.mixer.music.get_busy() :
            pygame.event.poll()
            self.clock.tick(10)
    def update(self):
        Thread(None,self.play_audio).start()
    def stop_audio(self):
        pygame.mixer.music.stop()
        Thread(None, self.play_audio).setDaemon(True)