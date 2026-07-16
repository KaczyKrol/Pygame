from delta_time import *
acc = 5
v = 0
dt = DeltaTime()

for i in range(100):
    dt.update()
    v += (acc - 0.2*v* abs(v)) * dt
    print(v)