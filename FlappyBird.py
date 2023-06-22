import pygame as pg
W,H = 400, 500
running  = True
screen = pg.display.set_mode((W, H))



while (running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
