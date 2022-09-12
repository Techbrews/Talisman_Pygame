# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 21:24:14 2022

@author: Mora
"""

import pygame, sys

class Button:
    def __init__(self, screen,  text, width, height, pos, elevation):
        
        self.screen = screen
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        
        gui_font = pygame.font.Font(None, 30)
        
        #top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        
        
        #bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'
        
        #text
        self.text_surf = gui_font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
        
    def draw(self):
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        
        pygame.draw.rect(self.screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.screen, self.top_color, self.top_rect, border_radius = 12)
        self.screen.blit(self.text_surf, self.text_rect)
        self.check_click()
        
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = "#D74B4B"
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    print("Click")
                    self.pressed = False
        else:
          self.dynamic_elevation = self.elevation
          self.top_color = '#475F77'
            
            
            
            
            
        
        