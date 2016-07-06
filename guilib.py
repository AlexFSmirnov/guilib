import pygame 


# This class creates an in
#
#class inputField:
    #def __init__(x, y,
                 #textlen,
                 #size,
                 #font_path               = "fonts/en.png",
                 #background_color        = (255, 255, 255),
                 #background_color_active = (255, 255, 255),
                 #outline_color           = (100, 100, 100),
                 #outline_color_acive     = (255, 0, 0),
                 #outline_width           = 2):
        #pass

#def inputField(surface,
               #x, y,
               #textlen, 
               #sym_size,
               #resizable        = True,
               #font_path        = "fonts/en.png",
               #background_color = (255, 255, 255),
               #outline_color    = (100, 100, 100),
               #outline_width    = 2): 
    #is_on = True
    #while is_on:
        #for e in pygame.event.get():
            #if e.type == pygame.QUIT:
                #pygame.quit()
                #quit(0)
            
               


# This function returns a pygame.Surface object 
# with a given text drawn on it.
def textSurface(text,
                sym_size,
                font_path        = "fonts/en.png",
                background_color = (255, 255, 255),
                outline_color    = (100, 100, 100),
                outline_width    = 2):
    text = text.split('\n')
    text_w = max([len(line) for line in text])
    text_h = len(text)
    
    text_surf = pygame.Surface((sym_size *  text_w + 2 * outline_width,
                                            sym_size * text_h + 2 * outline_width))
    text_surf.fill(outline_color)
    pygame.draw.rect(text_surf, background_color, 
                     (outline_width, outline_width, 
                              sym_size * text_w, sym_size * text_h))
    
    for line_idx, line in enumerate(text):
        for sym_idx, sym in enumerate(line):
            Basics.drawSym(text_surf,
                           sym,
                           outline_width + sym_idx * sym_size,
                           outline_width + line_idx * sym_size,
                           sym_size,
                           font_path)
    return text_surf
    
    




class Basics:
    def drawSym(surface, sym, x, y, sym_size=16, font_path="fonts/en.png"):
        font = pygame.image.load(font_path)
        alph = ("abcdefghijklmnopqrstuvwxyz-0123456789" + 
                                   "ABCDEFGHIJKLMNOPQRSTUVWXYZ_)!@#$%^&*(.,/ ")
        if sym not in alph: sym = " "
        
        idx = alph.index(sym)
        # Scaling the font file to size
        font = pygame.transform.scale(font, (len(alph) * sym_size, sym_size)) 
        # Slicing the font file, so that only one symbol is left        
        surface.blit(font, (x, y), (sym_size * idx, 0, sym_size, sym_size)) 
