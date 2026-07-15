import pygame as pg

class DeltaTime:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.dt = 0.0

    def update(self):
        self.dt = self.clock.tick(60) / 1000.0

    def __mul__(self, other):
        return self.dt * other

    def __rmul__(self, other):
        return other * self.dt

dt = DeltaTime()