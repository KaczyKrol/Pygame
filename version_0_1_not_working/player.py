import pygame as pg
import constants as c
import rigid_body as rb
import trigger as t
import vector as v
import player_input as p
import delta_time as d
import animator as a

class Player:
    def __init__(self, player_input: p.PlayerInput,delta_time: d.DeltaTime, screen):
        self.rb = rb.RigidBody(0,100, c.PLAYER_WIDTH,c.PLAYER_HEIGHT,delta_time)
        self.feet_trigg = t.Trigger(self.rb,c.PLAYER_WIDTH/2,0,c.FEET_WIDTH,-c.FEET_HEIGHT)

        self.pi = player_input
        self.dt = delta_time
        self.a = a.Animator(c.PLAYER_WIDTH,c.PLAYER_HEIGHT,self.rb.transform,screen)

        self.extra_jump = False
        self.is_grounded = False
        self.timer = 0

    def trigger(self,coll):
        self.feet_trigg.trigger(coll)

    def gravity(self):
        acc = v.Vector(0,c.GRAV)
        self.rb.apply_force(acc)

    def restrictive_forces(self):
        acc = - self.rb.transform.vel * abs(self.rb.transform.vel) * c.RES
        self.rb.apply_force(acc)

    def side_movement(self,dir):
        acc = v.Vector(dir.x * c.WALK_ACC,0)
        self.rb.apply_force(acc)

    def jump(self):
        if self.is_grounded or self.extra_jump:
            vel = v.Vector(self.rb.transform.vel.x,c.JUMP_SPEED)
            self.rb.apply_instant_vel(vel)
            if not self.is_grounded:
                self.extra_jump = False



    @property
    def direction(self):
        return v.Vector(self.pi.held(pg.K_w) - self.pi.held(pg.K_s),self.pi.held(pg.K_d)-self.pi.held(pg.K_a))

    def movement_control(self):
        dir = self.direction
        if self.pi.down(pg.K_SPACE):
            self.jump()
        self.side_movement(dir)

    def update(self):
        self.timer = min(self.timer + self.dt,6)
        #self.is_dashing = False if self.timer > c.DASH_TIME or (self.feet_trigg and not self.is_grounded) else True

        self.is_grounded = bool(self.feet_trigg)
        self.movement_control()
        self.gravity()
        self.restrictive_forces()

        self.rb.update()

    def update_a(self):
        self.a.update()
