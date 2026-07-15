import pygame as pg

class Trigger:
    def __init__(self, body, x, y, h, w):
        self.body = body
        self.x = x
        self.y = y
        self.h = h
        self.w = w

    @property
    def rect(self):
        x = self.body.transform.pos.x
        y = self.body.transform.pos.y

        return pg.Rect(x + self.x, y + self.y, self.w, self.h)

def trigger(a:Trigger, b):
    return a.rect.colliderect(b.rect)