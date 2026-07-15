import pygame as pg
import player_input
pg.init()

screen = pg.display.set_mode((384, 216))
pg.display.set_caption("Moja gra")
pi = player_input.PlayerInput()

running = True
i = 0
while running:
    pi.update()
    screen.fill((0, 0, 0))   # czyści ekran
    if pi.held(pg.K_SPACE):
        screen.blit(pg.image.load(f"test000{i}.png").convert_alpha(), (2, 2))  # rysujesz obraz

    pg.display.flip()  # aktualizujesz ekran
    i = (i + 1)%4