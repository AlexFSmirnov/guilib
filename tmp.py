import pygame 
from pygame import *

import guilib
import sys


pygame.init()

screen = pygame.display.set_mode((500, 500))


while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit(0)
        
        if e.type == KEYDOWN:
            if e.key == K_q:
                surf = guilib.textSurface("LoooKKK, \n  THIS IS A TEXT SURFACE!!!", 16)
                
                screen.blit(surf, (100, 100))
                pygame.display.update()