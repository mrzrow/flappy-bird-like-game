import pygame as pg
from constants import *


class Bird:
    def __init__(self, app):
        self.app = app
        self.vel_y = fall_vel
        self.x = width // 4
        self.y = height // 2
        self.width = self.height = 50

    def draw_bird(self):
        pg.draw.rect(app.screen, RED, (self.x, self.y, self.width, self.height), border_radius=10)

    def move_bird(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.vel_y > jump_border:
            self.vel_y = jump_vel
        elif self.vel_y != fall_vel:
            self.vel_y += change_vel
        self.y += self.vel_y


class App:
    def __init__(self):
        self.bird = Bird(self)
        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        pg.display.set_caption('Example')

    def draw(self):
        self.screen.fill(bg_color)
        self.bird.draw_bird()
        pg.display.flip()

    def run(self):
        while True:
            self.draw()
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()

            # aciton of entities
            self.bird.move_bird()

            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
