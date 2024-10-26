from random import randint
import pygame as pg
import os
from constants import *


class Bird:
    def __init__(self, app):
        self.app = app
        self.vel_y = fall_vel
        self.x = width // 4
        self.y = height // 2
        self.width = self.height = 50

        self.image_fly = pg.image.load(os.path.join('images', 'plate_fly.png'))
        self.image_jump = pg.image.load(os.path.join('images', 'plate_jump.png'))

    def draw(self):
        if self.vel_y > jump_border:
            self.app.screen.blit(self.image_fly, (self.x, self.y))
        else:
            self.app.screen.blit(self.image_jump, (self.x, self.y))
        # pg.draw.rect(self.app.screen, RED, (self.x, self.y, self.width, self.height), border_radius=10)

    def move(self):
        keys = pg.key.get_pressed()

        # jump
        if (keys[pg.K_SPACE] or pg.mouse.get_pressed()[0]) and self.vel_y > jump_border:
            self.vel_y = jump_vel
        elif self.vel_y != fall_vel:
            self.vel_y += change_vel
        self.y += self.vel_y


class Pillar:
    def __init__(self, app):
        self.app = app
        self.x = width - width // 3
        self.width = width // 6
        self.image_top = pg.image.load(os.path.join('images', 'pillar_top.png'))
        self.image_bot = pg.image.load(os.path.join('images', 'pillar_bot.png'))
        self.images_size = (167, 1000)

        self.space_hight = int(height * 0.4)
        self.max_space_up = min_height_top
        self.max_space_down = min(height - self.space_hight, min_height_bot)
        self.space_y = randint(self.max_space_up, self.max_space_down)

        self.added_to_score = False

        self.vel_x = -5
        self.spacing = int(width * 0.45)

    def draw(self):
        self.app.screen.blit(self.image_top, (self.x, self.space_y - self.images_size[1]))
        self.app.screen.blit(self.image_bot, (self.x, self.space_y + self.space_hight))


class Score:
    def __init__(self, app):
        self.app = app
        self.current_score = 0
        self.score_font = pg.font.SysFont(os.path.join('fonts', 'Debrosee-ALPnL.ttf'), font_size)
        self.rect_coords = (20, 20, 134, 76)
        self.bg_image = pg.image.load(os.path.join('images', 'score_back.png'))

    def draw(self):
        self.app.screen.blit(self.bg_image, (self.rect_coords[:2]))
        score_image = self.score_font.render(str(self.current_score), True, BLACK)
        score_rect = score_image.get_rect(
            center=(self.rect_coords[0] + self.rect_coords[2] // 2, self.rect_coords[1] + self.rect_coords[3] // 2))
        self.app.screen.blit(score_image, score_rect)
