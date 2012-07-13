import pygame
from pygame.locals import *
from math import sin, cos, radians
def cCurve(screen, x1, y1, x2, y2, level):
    if level == 0:
        pygame.draw.line(screen, (128,128,128), (x1, y1), (x2, y2), 1)
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    pygame.quit()
            if evt.type == QUIT:
                pygame.quit()
    else:
        xm = (x1 + x2 + y1 - y2) / 2.0
        ym = (y2 + x2 + y1 - x1) / 2.0
        cCurve(screen, x1, y1, xm, ym, level-1)
        cCurve(screen, xm, ym, x2, y2, level-1)
        if level > 7:
            pygame.display.flip()

if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    w, h = screen.get_width(), screen.get_height()
    for level in range (30):
        screen.fill((0,0,0))
        cCurve(screen, *map(int, [w/2, (h/4), w/2, 3*(h/4), level]))
        pygame.display.flip()
        pygame.time.Clock().tick()
        q = False
        while not q:
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    if evt.key == K_ESCAPE:
                        pygame.quit()
                    else:
                        q = True
                if evt.type == QUIT:
                    pygame.quit()
    while not q:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                q = True