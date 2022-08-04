import pygame as pg
from constants import *
from entities import *
from scenes import *

pg.font.init()


def scene_manage_move(scene_index, scenes):
    scenes[scene_index].move()
    if scenes[scene_index].end():
        scene_index += 1
    return scene_index


class App:
    def __init__(self):
        self.scene_index = 0
        self.scenes = (StartScene(self), MainScene(self), EndScene(self))

        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        pg.display.set_caption('Example')

        self.bg_image = pg.image.load(os.path.join('images', 'bg_image.png'))

    def draw(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.scenes[self.scene_index].draw()
        pg.draw.rect(self.screen, BLACK, (0, 0, width, height), width=10)
        pg.display.flip()

        pg.display.set_caption(str(self.clock.get_fps()))

    def run(self):
        while True:
            self.draw()
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    exit()

            # scene managment
            self.scene_index = scene_manage_move(self.scene_index, self.scenes)
            if self.scene_index == len(self.scenes):
                self.scene_index = 0
                self.scenes = (StartScene(self), MainScene(self), EndScene(self))
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
