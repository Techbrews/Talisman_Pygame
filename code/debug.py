# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 11:22:55 2022

@author: TechBrews
"""

import pygame

pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, y = 10, x=10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, "White")
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface, "Black", debug_rect)
    display_surface.blit(debug_surf, debug_rect)
