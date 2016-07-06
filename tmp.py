import pygame 
from pygame import *

import guilib
import sys


pygame.init()

screen = pygame.display.set_mode((500, 500), HWSURFACE|DOUBLEBUF|RESIZABLE)
display_surface = Surface((500, 500))


while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if e.type==VIDEORESIZE:
            screen=pygame.display.set_mode(e.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)            
            pygame.display.update()        
        
        if e.type == KEYDOWN:
            if e.key == K_q:
                surf = guilib.textSurface("LoooKKK, \n  TEXT SURFACE", 30)
                display_surface.blit(surf, (30, 30))
        
        screen.blit(pygame.transform.scale(display_surface, 
                                           (pygame.display.Info().current_w,
                                            pygame.display.Info().current_h)), 
                    (0, 0))
        pygame.display.update()
        
        