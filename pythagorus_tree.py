import pygame
from pygame.locals import *
from math import sin, cos, radians
from random import randint

def rotate_pyt(x1, y1, x2, y2, deg):
    x, y = (x2-x1), (y2-y1)
    return [x2+x*cos(radians(deg))-y*sin(radians(deg)), y2+x*sin(radians(deg))+y*cos(radians(deg))]

def pyt(screen, color, x1, y1, x2, y2, level):
    if level == 0:
        tmp=[]
        tmp.append([x1,y1])
        tmp.append([x2,y2])
        x3, y3 = rotate_pyt(x1,y1,x2,y2,90)
        tmp.append([x3,y3])
        x5, y5 = rotate_pyt(x2,y2,x1,y1,-90)
        x4, y4 = x5, y5
        x4, y4 = (x3 + x5 +y5 -y3)/2.0,(y3 + y5 + x3 - x5)/2.0  # comment this line to make squares instead of pentagons
        tmp.append([x4,y4])        
        tmp.append([x5,y5])
        pygame.draw.polygon(screen, color, tmp)
        #pygame.draw.line(screen, (0,0,128), tmp[0],tmp[3],1)
        #pygame.draw.line(screen, (0,0,128), tmp[1],tmp[2],1)
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    pygame.quit()
                if evt.key == K_s:
                	i = randint(1,10000)
                	pygame.image.save(screen,'%d.png'%(i))
            if evt.type == QUIT:
                pygame.quit()
        #pygame.display.flip()	# comment to prevent animation
    else:
        color = map(lambda x:max(0,(x-13)),color)
        x3, y3 = rotate_pyt(x1,y1,x2,y2,90)
        x5, y5 = rotate_pyt(x2,y2,x1,y1,-90)
        x4, y4 = (x3 + x5 +y5 -y3)/2.0,(y3 + y5 + x3 - x5)/2.0
        pyt(screen, color, x4, y4, x3, y3, level-1)
        pyt(screen, color, x5, y5, x4, y4, level-1)

if __name__=='__main__':
    pygame.display.init()
    screen = pygame.display.set_mode((1366,768))
    w, h = screen.get_width(), screen.get_height()
    level = 30
    for i in range(level):
        pyt(screen,[128,255,255], *map(int, [.57*w, h, .43*w, h, i]))
        pygame.display.flip()
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
    q = False
    while not q:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                q = True
