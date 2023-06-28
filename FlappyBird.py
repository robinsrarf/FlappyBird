import pygame as pg

pg.init()
W,H = 400, 500
running  = True
color = pg.Color
screen = pg.display.set_mode((W, H))



while (running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    screen.fill(color("black"))
pg.quit()