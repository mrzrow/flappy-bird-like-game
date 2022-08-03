import pygame as pg
from constants import *
from entities import *


def scene_manage_move(scene_index, scenes):
    scenes[scene_index].move()
    if scenes[scene_index].end():
        scene_index += 1
    return scene_index


class StartScene:
    def __init__(self, app):
        self.app = app

    def draw(self):
        pg.draw.rect(self.app.screen, WHITE, (0, 0, width, height), width=20, border_radius=10)

    def move(self):
        pass

    def end(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            return True
        return False


class MainScene:
    def __init__(self, app):
        self.app = app
        self.bird = Bird(self.app)
        self.score = Score(self.app)
        self.pillars = []
        for i in range(5):  # spawning pillars
            self.pillars.append(Pillar(self.app))
            self.pillars[-1].x += i * self.pillars[-1].spacing

    def draw(self):
        self.bird.draw()
        for pillar in self.pillars:
            pillar.draw()
        self.score.draw()

    def move(self):
        self.bird.move()
        for pillar in self.pillars:
            pillar.x += pillar.vel_x
            if (pillar.x < self.bird.x - pillar.width) and (not pillar.added_to_score):
                self.score.current_score += 1
                pillar.added_to_score = True

        if self.pillars[0].x < - self.pillars[0].width + 20:  # delet unshowed pillars
            self.pillars.pop(0)
            self.pillars.append(Pillar(self.app))
            self.pillars[-1].x = self.pillars[-2].x + self.pillars[-1].spacing

    def end(self):
        for pillar in self.pillars:  # collisions
            if (pillar.x <= self.bird.x <= pillar.x + pillar.width) or (
                    pillar.x <= self.bird.x + self.bird.width <= pillar.x + pillar.width):
                if (self.bird.y < pillar.space_y) or (
                        self.bird.y + self.bird.width > pillar.space_y + pillar.space_hight):
                    return True
        if self.bird.y + self.bird.width >= height:
            return True
        return False


class EndScene:
    def __init__(self, app):
        self.app = app

    def draw(self):
        pg.draw.circle(self.app.screen, WHITE, (width // 2, height // 2), width // 4)

    def move(self):
        pass

    def end(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            return True
        return False


class App:
    def __init__(self):
        self.scene_index = 0
        self.scenes = (StartScene(self), MainScene(self), EndScene(self))

        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        pg.display.set_caption('Example')

    def draw(self):
        self.screen.fill(bg_color)
        self.scenes[self.scene_index].draw()
        pg.display.flip()

    def run(self):
        while True:
            self.draw()
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()

            self.scene_index = scene_manage_move(self.scene_index, self.scenes)
            if self.scene_index == len(self.scenes):
                self.scene_index = 0
                self.scenes = (StartScene(self), MainScene(self), EndScene(self))
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
