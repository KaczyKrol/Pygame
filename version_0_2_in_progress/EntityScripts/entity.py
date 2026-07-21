import rigid_body as rb
import version_0_2_in_progress.elementary.vector as v
import constants as c

class Entity:
    def __init__(self,delta_time,w,h):
        self.body = rb.RigidBody(self)
        self.dt = delta_time
        self.size = v.Vector(w, h)

        self.is_grounded = False

    def gravity(self):
        self.body.apply_acc(v.Vector(0,-c.GRAV))

    def resistance(self):
        acc = - self.body.vel * abs(self.body.vel) * c.RESISTANCE
        self.body.apply_acc(acc)

    def walking(self,direction: float):
