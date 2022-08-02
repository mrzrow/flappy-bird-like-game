import pygame as pg
from constants import *


def scene_manage_draw(scene_index, scenes):
    scenes[scene_index].draw()


def scene_manage_move(scene_index, scenes):
    scenes[scene_index].move()
    if scenes[scene_index].end():
        scene_index += 1
    return scene_index


class StartScene:
    def __init__(self, app):
        self.app = app

    def draw(self):
        pg.draw.rect(app.screen, WHITE, (0, 0, width, height), width=20, border_radius=10)

    def move(self):
        pass

    def end(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            return True
        return False


class Bird:
    def __init__(self, app):
        self.app = app
        self.vel_y = fall_vel
        self.x = width // 4
        self.y = height // 2
        self.width = self.height = 50

    def draw(self):
        pg.draw.rect(app.screen, RED, (self.x, self.y, self.width, self.height), border_radius=10)

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.vel_y > jump_border:
            self.vel_y = jump_vel
        elif self.vel_y != fall_vel:
            self.vel_y += change_vel
        self.y += self.vel_y

    def end(self):
        pass


class App:
    def __init__(self):
        self.scene_index = 0
        self.scenes = (StartScene(self), Bird(self))

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

            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
