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

def collision(a:Collider, b:Collider):
    return a.rect.colliderect(b.rect)

def get_overlap(a: Collider, b: Collider):
    r1 = a.rect
    r2 = b.rect

    dx = min(r1.right - r2.left, r2.right - r1.left)
    dy = min(r1.bottom - r2.top, r2.bottom - r1.top)

    return dx, dy

def resolve_collision(bodyA, bodyB):
    colA = bodyA.collider
    colB = bodyB.collider

    if not collision(colA, colB):
        return

    dx, dy = get_overlap(colA, colB)

    if dx < dy:
        if bodyA.transform.pos.x < bodyB.transform.pos.x:
            bodyA.transform.pos.x -= dx
        else:
            bodyA.transform.pos.x += dx

        bodyA.transform.vel.x = 0
        bodyA.transform.acc.x = 0

    else:
        if bodyA.transform.pos.y < bodyB.transform.pos.y:
            bodyA.transform.pos.y -= dy
        else:
            bodyA.transform.pos.y += dy

        bodyA.transform.vel.y = 0
        bodyA.transform.acc.y = 0
