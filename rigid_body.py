import pygame as pg
import delta_time as Dt
import collider as coll
import vector as v

class Transform:
    def __init__(self, x, y, dt: Dt.DeltaTime):
        self.pos = v.Vector(x, y)
        self.vel = v.Vector()
        self.acc = v.Vector()
        self.dt = dt

    def update(self):
        self.vel += self.acc * self.dt
        self.pos += self.vel * self.dt

class RigidBody:
    def __init__(self,x,y,w,h,m, dt: Dt.DeltaTime):
        self.transform = Transform(x,y, dt)
        self.dim = v.Vector(w,h)

        self.mass = m
        self.inv_mass = 1/self.mass if self.mass != 0 else 0

        self.coll = coll.Collider(self)

    def apply_force(self,force):
        self.transform.acc += force * self.inv_mass

    def apply_instant_vel(self,vel):
        self.transform.vel += vel

    def update(self):
        self.transform.update()