import pygame as pg

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
        pass

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