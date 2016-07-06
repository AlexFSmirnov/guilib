import pygame 


# This function returns a pygame.Surface object 
# with a given text drawn on it.
def textSurface(text,
                size,
                font_path       = "fonts/en.png",
                background_color= (255, 255, 255),
                outline_color   = (100, 100, 100),
                outline_width   = 2):
    text = text.split('\n')
    text_w = max([len(line) for line in text])
    text_h = len(text)
    
    text_surf = pygame.Surface((size *  text_w + 2 * outline_width,
                                            size * text_h + 2 * outline_width))
    text_surf.fill(outline_color)
    pygame.draw.rect(text_surf, background_color, 
                     (outline_width, outline_width, 
                              size * text_w, size * text_h))
    
    for line_idx, line in enumerate(text):
        for sym_idx, sym in enumerate(line):
            Basics.drawSym(text_surf,
                           sym,
                           outline_width + sym_idx * size,
                           outline_width + line_idx * size,
                           size,
                           font_path)
    return text_surf
    
    




class Basics:
    def drawSym(surface, sym, x, y, size=16, font_path="fonts/en.png"):
        font = pygame.image.load(font_path)
        alph = ("abcdefghijklmnopqrstuvwxyz-0123456789" + 
                                   "ABCDEFGHIJKLMNOPQRSTUVWXYZ_)!@#$%^&*(.,/ ")
        if sym not in alph: sym = " "
        
        idx = alph.index(sym)
        # Scaling the font file to size
        font = pygame.transform.scale(font, (len(alph) * size, size)) 
        # Slicing the font file, so that only one symbol is left        
        surface.blit(font, (x, y), (size * idx, 0, size, size)) 
