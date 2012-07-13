'''
Created on 12-Jul-2012

@author: TOSHIBA
'''
#import turtle
import pygame
from pygame.locals import *
from math import sin, cos, radians
from random import randint
def koch(screen, x1, y1, x2, y2, level):
    if level == 0:
        pygame.draw.line(screen, (128,128,128), (x1, y1), (x2, y2), 1)
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
        xm = (x1 + x2) / 2.0 + (y1 - y2) / 3.0
        ym = (y2 + y1) / 2.0 + (x2 - x1) / 3.0
        xv = (x2 - x1) / 3.0
        yv = (y2 - y1) / 3.0
        xl = x1 + xv
        yl = y1 + yv
        xr = x2 - xv
        yr = y2 - yv
        koch(screen, x1, y1, xl, yl, level-1)
        koch(screen, xl, yl, xm, ym, level-1)
        koch(screen, xm, ym, xr, yr, level-1)
        koch(screen, xr, yr, x2, y2, level-1)
        if level > 3:
            pygame.display.flip()
        
if __name__=='__main__':
    pygame.display.init()
    screen = pygame.display.set_mode((1366,768),FULLSCREEN)
    w, h = screen.get_width(), screen.get_height()
    speed = 2;
    q = False
    for i in range(20):
        screen.fill((0,0,0))
        koch(screen, *map(int, [w, 3*(h/4), 0, 3*(h/4), i]))
        pygame.display.flip()
        #pygame.time.Clock().tick(speed)
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
