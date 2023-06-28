import pygame as pg
from sys import exit

pg.init()
W, H = 400, 500
running = True
color = pg.Color
screen = pg.display.set_mode((W, H))
pg.display.set_caption("FlappyBird")
clock = pg.Clock()


class Bird:
    def __init__(self, pos):
        self.pos = pos
        self.vel = 1
        self.a = 0

    def update(self):
        if self.pos[1] < H-5:
            self.vel += self.a
            self.pos[1] += self.vel
        pg.draw.circle(screen, "red", self.pos, 5)


player = Bird([W//2, H//2])
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            player.pos[1] += -30

    screen.fill('black')
    player.update()
    
    pg.display.update()
    clock.tick(60)
