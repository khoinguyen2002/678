from game_object import GameObject
from frame_counter import FrameCounter
from enemy.enemy import Enemy
import game_object
from random import randint

class EnemySpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.counter = FrameCounter(100)
        self.count = 0

    def update(self):
        self.counter.run()
        self.count += 1
        if self.counter.expired:
            enemy = Enemy(randint(30, 670), randint(0, 50))
            game_object.add(enemy)
            
            self.counter.reset()
        if self.count > 2000:
            if self.counter.count == 50:
                    enemy = Enemy(randint(30, 670), randint(0, 50))
                    game_object.add(enemy)