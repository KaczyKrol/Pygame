import pygame as pg
pg.init()

screen = pg.display.set_mode((200, 60))
pg.display.set_caption("Moja gra")


running = True
i = 0
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0, 0, 0))   # czyści ekran

    screen.blit(pg.image.load(f"test000{i}.png").convert_alpha(), (2, 2))  # rysujesz obraz

    pg.display.flip()  # aktualizujesz ekran
    i = (i + 1)%4