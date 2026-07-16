import pygame as pg
import constants as c
import rigid_body as rb
import trigger as t

class Player:
    def __init__(self, player_input):
        self.rb = rb.RigidBody()

        self.feet_coll = t.Trigger(self.rb)
        self.right_coll = t.Trigger(self.rb)
        self.left_coll = t.Trigger(self.rb)

        self.pi = player_input

    def movement_control(self):
        pass

    def restrictive_forces(self):
        force = - self.rb.transform.vel * abs(self.rb.transform.vel) * c.RES
        self.rb.apply_force(force)


    def walk(self):
        pass
    def run(self):
        pass
    def jump(self):
        pass
    def dash(self):
        pass

    def update(self):
        pass

# zmienić system kolizji tak, żeby działał na siłach wyrównujących, a nie na zerowaniu