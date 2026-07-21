import pygame as pg
from version_0_2_in_progress.elementary.vector import  *

class Collider:
    def __init__(self, parent, size):
        self.size = size
        self.pos = parent.transform.pos
    @property
    def rect(self):
        return pg.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)

    def collision(self, other):
        return self.rect.colliderect(other.rect)

    def get_overlap(self, other):
        r1 = self.rect
        r2 = other.rect

        dx = min(r1.right - r2.left, r2.right - r1.left)
        dy = min(r1.bottom - r2.top, r2.bottom - r1.top)

        return dx, dy