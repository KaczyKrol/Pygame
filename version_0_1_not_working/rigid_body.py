import pygame as pg
import delta_time as Dt
import collider as coll
import vector as v

class Transform:
    def __init__(self, x, y, delta_time: Dt.DeltaTime):
        self.pos = v.Vector(x, y)
        self.vel = v.Vector()
        self.acc = v.Vector()
        self.dt = delta_time

    def update(self):
        self.vel += self.acc * self.dt
        self.pos += self.vel * self.dt

class RigidBody:
    def __init__(self,x,y,w,h, delta_time: Dt.DeltaTime):
        self.transform = Transform(x,y, delta_time)
        self.dim = v.Vector(w,h)

        self.coll = coll.Collider(self)

    def apply_force(self,acc):
        self.transform.acc += acc

    def apply_instant_vel(self,vel):
        self.transform.vel = vel

    def reset_force(self):
        self.transform.acc = v.Vector(0,0)

    def update(self):
        self.transform.update()
        self.reset_force()

    def resolve_collision(self, other):
        if not self.coll.collision(other.coll):
            return

        dx, dy = self.coll.get_overlap(other.coll)

        if dx < dy:
            if self.transform.pos.x < other.transform.pos.x:
                self.transform.pos.x -= dx
            else:
                self.transform.pos.x += dx

            self.transform.vel.x = 0
            self.transform.acc.x = 0


        else:
            if self.transform.pos.y < other.transform.pos.y:
                self.transform.pos.y -= dy
            else:
                self.transform.pos.y += dy

            self.transform.vel.y = 0
            self.transform.acc.y = 0