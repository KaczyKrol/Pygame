import player_input
import pygame as pg
import vector as v

pg.init()
pi = player_input.PlayerInput()
# Ustawienie rozmiaru okna
WIDTH = 800
HEIGHT = 600

# Utworzenie okna
screen = pg.display.set_mode((WIDTH, HEIGHT))
while True:
    screen.fill((0,0,0))  # wyczyść ekran
    pi.update()
    if pi.down(pg.K_m):
        break
    ve = v.Vector(pi.held(pg.K_d)-pi.held(pg.K_a),pi.held(pg.K_w) - pi.held(pg.K_s))
    pg.draw.rect(
        screen,  # ekran
        (255, 0, 0),  # kolor (czerwony)
        (100*ve.x +100, -100*ve.y+100, 20, 20)  # x, y, szerokość, wysokość
    )
    pg.display.flip()

pg.quit()