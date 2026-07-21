import pygame as pg

class Collider:
    def __init__(self, body):
        self.body = body

    @property
    def rect(self):
        x = self.body.transform.pos.x
        y = self.body.transform.pos.y
        w = self.body.dim.x
        h = self.body.dim.y
        return pg.Rect(x, y, w, h)

    def collision(self, other):
        return self.rect.colliderect(other.rect)

    def get_overlap(self, other):
        r1 = self.rect
        r2 = other.rect

        dx = min(r1.right - r2.left, r2.right - r1.left)
        dy = min(r1.bottom - r2.top, r2.bottom - r1.top)

        return dx, dy