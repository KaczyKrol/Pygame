from rigid_body import Transform
import pygame as pg

class Animator:
    def __init__(self,w,h, transform: Transform, screen: pg.Surface):
        self.pos = transform.pos
        self.dim = w,h
        self.screen = screen
    def update(self):
        pg.draw.rect(self.screen,(255,255,255),(self.pos.x, self.pos.y, self.dim[0], self.dim[1]))
class Animation:
    pass
class PlayerAnimator(Animator):
    pass
class NPCAnimator(Animator):
    pass
class GroundAnimator(Animator):
    pass
class BackgroundAnimator(Animator):
    pass
class ForegroundAnimator(Animator):
    pass
