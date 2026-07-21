import pygame as pg

class Trigger:
    def __init__(self, body, x, y,w,h):
        self.body = body
        self.x = x
        self.y = y
        self.h = h
        self.w = w

        self.is_triggered = False

    def __bool__(self):
        return self.is_triggered

    @property
    def rect(self):
        x = self.body.transform.pos.x
        y = self.body.transform.pos.y

        return pg.Rect(x + self.x, y + self.y, self.w, self.h)

    def trigger(self, floor):
        return self.rect.colliderect(floor.rect)