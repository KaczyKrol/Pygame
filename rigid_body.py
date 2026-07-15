import pygame as pg
import delta_time as dt
import collider as coll

class Transform:
    def __init__(self, x, y, dt: dt.DeltaTime):
        self.pos = pg.Vector2(x, y)
        self.vel = pg.Vector2(0, 0)
        self.acc = pg.Vector2(0, 0)
        self.dt = dt

    def update(self):
        self.vel += self.acc * self.dt
        self.pos += self.vel * self.dt

class RigidBody:
    def __init__(self,x,y,h,w,m, dt: dt.DeltaTime):
        self.transform = Transform(x,y, dt)
        self.dim = pg.Vector2(w,h)

        self.mass = m
        self.inv_mass = 1/self.mass if self.mass != 0 else 0

        self.coll = coll.Collider(self)

    def apply_force(self,force):
        self.transform.acc += force * self.inv_mass

    def apply_instant_vel(self,vel):
        self.transform.vel += vel

    def update(self):
        self.transform.update()