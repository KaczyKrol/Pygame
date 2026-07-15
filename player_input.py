import pygame as pg


class PlayerInput:
    def __init__(self):
        self.keys_down = set()
        self.keys_up = set()
        self.keys_held = pg.key.get_pressed()

    def update(self):
        self.keys_down.clear()
        self.keys_up.clear()
        self.keys_held = pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.KEYDOWN:
                self.keys_down.add(event.key)

            if event.type == pg.KEYUP:
                self.keys_up.add(event.key)

    def down(self, key):
        return key in self.keys_down

    def up(self, key):
        return key in self.keys_up

    def held(self, key):
        return self.keys_held[key]