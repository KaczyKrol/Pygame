from version_0_2_in_progress.elementary.vector import *
from version_0_2_in_progress.elementary.collider import *

class Transform:
    def __init__(self, delta_time):
        self.pos = Vector()
        self.vel = Vector()
        self.acc = Vector()

        self.dt = delta_time
    def set_pos(self, x, y):
        self.pos.x = Vector(x, y)

    def set_vel(self, x, y):
        self.vel.x = Vector(x, y)

    def set_acc(self, x, y):
        self.acc = Vector(x, y)

    def apply_acc(self,acc):
        self.acc += acc

    def reset_acc(self):
        self.set_acc(0,0)

    def update(self):
        self.vel += self.acc * self.dt
        self.pos += self.vel * self.dt


class RigidBody:
    def __init__(self, entity):
        self.entity = entity

        self.transform = Transform(self.entity.dt)
        self.collider = Collider(self.transform, self.entity.size)

    @property
    def pos(self):
        return self.transform.pos
    @property
    def vel(self):
        return self.transform.vel
    @property
    def acc(self):
        return self.transform.acc

    def apply_acc(self, acc):
        self.transform.apply_acc(acc)


    def resolve_collision(self, other):
        if not self.collider.collision(other.collider):
            self.entity.is_grounded = False
            return

        dx, dy = self.collider.get_overlap(other.coll)

        if dx != 0:
            if self.pos.x < other.pos.x:
                self.pos.x -= dx
            else:
                self.pos.x += dx

            self.vel.x = 0
            self.acc.x = 0

        if dy != 0:
            if self.pos.y < other.pos.y:
                self.pos.y -= dy
                self.entity.is_grounded = True
            else:
                self.pos.y += dy

            self.vel.y = 0
            self.acc.y = 0
