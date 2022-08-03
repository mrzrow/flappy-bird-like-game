from random import randint
import pygame as pg
from constants import *


class Bird:
    def __init__(self, app):
        self.app = app
        self.vel_y = fall_vel
        self.x = width // 4
        self.y = height // 2
        self.width = self.height = 50

    def draw(self):
        pg.draw.rect(self.app.screen, RED, (self.x, self.y, self.width, self.height), border_radius=10)

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.vel_y > jump_border:
            self.vel_y = jump_vel
        elif self.vel_y != fall_vel:
            self.vel_y += change_vel
        self.y += self.vel_y


class Pillar:
    def __init__(self, app):
        self.app = app
        self.x = width - width // 3
        self.width = width // 6

        self.space_hight = height // 2
        self.max_space_up = 10
        self.max_space_down = height - self.space_hight + 10
        self.space_y = randint(self.max_space_up, self.max_space_down)

        self.vel_x = -5
        self.spacing = int(width * 0.8)

    def draw(self):
        pg.draw.rect(self.app.screen, WHITE, (self.x, 0, self.width, self.space_y), border_radius=10)
        pg.draw.rect(self.app.screen, WHITE, (self.x, self.space_y + self.space_hight, self.width, height),
                     border_radius=10)
