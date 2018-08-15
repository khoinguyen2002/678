from game_object import GameObject
from frame_counter import FrameCounter
from enemy.enemy import Enemy
import game_object


class EnemySpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0)
        self.counter = FrameCounter(100)

    def update(self):
        self.counter.run()
        if self.counter.expired:
            enemy = Enemy(100, 0)
            game_object.add(enemy)
            self.counter.reset()
