import pygame
from pygame.locals import *
from math import sin, cos, radians
from random import randint
def cCurve(screen, color, x1, y1, x2, y2, level):
    if level == 0:
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 1)
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    pygame.quit()
                if evt.key == K_s:
                    i = randint(1,10000)
                    pygame.image.save(screen,'%d.png'%(i))
            if evt.type == QUIT:
                pygame.quit()
    else:
    	color = map(lambda x:min(255,x+9),color)
        xm = (x1 + x2 + y1 - y2) / 2.0
        ym = (y2 + x2 + y1 - x1) / 2.0
        cCurve(screen, color, x1, y1, xm, ym, level-1)
        cCurve(screen, color, xm, ym, x2, y2, level-1)
        if level > 10:
            pass#pygame.display.flip()

if __name__=='__main__':
    pygame.display.init()
    screen = pygame.display.set_mode((1024,768),FULLSCREEN)
    w, h = screen.get_width(), screen.get_height()
    for i in range (30):
        screen.fill((0,0,0))
        cCurve(screen, [0,128,255], *map(int, [.25*w, .25*h, .75*w, .25*h, i]))
        #pygame.image.save(screen,'./cCurve/img%d.png'%(i))
        pygame.display.flip()
        #pygame.time.Clock().tick()
        q = False
        while not q:
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    if evt.key == K_ESCAPE:
                        pygame.quit()
                    else:
                        q = True
                    if evt.key == K_s:
                	i = randint(1,10000)
                	pygame.image.save(screen,'%d.png'%(i))
                if evt.type == QUIT:
                    pygame.quit()
    while not q:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                q = True
