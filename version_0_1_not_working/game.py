import delta_time as dt
import player
import player_input as pi
import ground
import pygame as pg
screen = pg.display.set_mode((500, 500))
dt = dt.DeltaTime()
pi = pi.PlayerInput()
player = player.Player(pi, dt, screen)
ground = ground.Ground(0, 0, 10, 200, dt, screen)

while True:
    screen.fill((0, 0, 0))

    dt.update()
    pi.update()
    player.update()
    player.rb.resolve_collision(ground.rb)
    player.trigger(ground)
    player.update_a()

    ground.update()
    pg.display.flip()



