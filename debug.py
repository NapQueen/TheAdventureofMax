#this debug doesnt actually influence our game. its a debug tool
#can be ignored entierly
#for ex if we go to the main file and run debug and it will print any
#information the coder thinks is important
import pygame
font = pygame.font.Font(None, 30)

def debug(info, y = 10, x = 10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)
