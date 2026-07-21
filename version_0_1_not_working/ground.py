import rigid_body as r
import delta_time as d
import animator as a
class Ground:
    def __init__(self,x,y,h,w,delta_time: d.DeltaTime, screen):
        self.rb = r.RigidBody(x,y,w,h,delta_time)
        self.a = a.Animator(w,h,self.rb.transform,screen)
    def update(self):
        self.a.update()