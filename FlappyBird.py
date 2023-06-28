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
    def __init__(self, pos, img):
        self.pos = pos
        self.vel = 1
        self.a = 0
        self.sprite = pg.image.load(img)
        self.img_size = self.sprite.get_size()

    def update(self):
        if self.pos[1] < H:
            self.vel += self.a
            self.pos[1] += self.vel
        screen.blit(
            self.sprite, (self.pos[0]-self.img_size[0]//2, self.pos[1]-self.img_size[1]//2))


player = Bird(
    [W//2, H//2], "C:\\Users\\robin\\Desktop\\FlappyBird\\sprites\\bird.png")
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
