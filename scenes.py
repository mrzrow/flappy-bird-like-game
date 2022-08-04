import pygame as pg
import os
from constants import *
from entities import *


class StartScene:
    def __init__(self, app):
        self.app = app
        self.clock = pg.time.Clock()

        self.button_image_s = pg.image.load(os.path.join('images', 'start_button.png'))
        self.image_rect = self.button_image_s.get_rect(center=(width // 2, height // 2))

        self.font_press = pg.font.SysFont(os.path.join('fonts', 'Debrosee-ALPnL.ttf'), 40)
        self.text_press = self.font_press.render('CLICK or press \'SPACE\' to START', True, BLACK)
        self.text_press_rect = self.text_press.get_rect(center=(width // 2, int(height * 0.6)))

        self.font_start = pg.font.SysFont(os.path.join('fonts', 'Debrosee-ALPnL.ttf'), 250)
        self.text_start = self.font_start.render('START', True, BLACK)
        self.text_rect = self.text_start.get_rect(center=(width // 2, height // 2))

    def draw(self):
        self.app.screen.blit(self.button_image_s, self.image_rect)
        self.app.screen.blit(self.text_start, self.text_rect)
        self.app.screen.blit(self.text_press, self.text_press_rect)

    def move(self):
        pass

    def end(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            return True
        if pg.mouse.get_pressed()[0]:
            xm, ym = pg.mouse.get_pos()
            if self.image_rect.collidepoint(xm, ym):
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

        if self.pillars[0].x < - self.pillars[0].width + 20:  # delete unshowed pillars
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

        self.button_image_s = pg.image.load(os.path.join('images', 'start_button.png'))
        self.image_rect = self.button_image_s.get_rect(center=(width // 2, height // 2))

        self.font_start = pg.font.SysFont(os.path.join('fonts', 'Debrosee-ALPnL.ttf'), 150)
        self.text_start = self.font_start.render('CONTINUE', True, BLACK)
        self.text_rect = self.text_start.get_rect(center=(width // 2, height // 2))

        self.font_press = pg.font.SysFont(os.path.join('fonts', 'Debrosee-ALPnL.ttf'), 40)
        self.text_press = self.font_press.render('press \'C\' to CONTINUE', True, BLACK)
        self.text_press_rect = self.text_press.get_rect(center=(width // 2, int(height * 0.6)))

    def draw(self):
        self.app.screen.blit(self.button_image_s, self.image_rect)
        self.app.screen.blit(self.text_start, self.text_rect)
        self.app.screen.blit(self.text_press, self.text_press_rect)

    def move(self):
        pass

    def end(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_c]:
            return True
        return False
