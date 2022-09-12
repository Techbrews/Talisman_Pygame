# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 10:40:03 2022

@author: TechBrews
"""

import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from ui import UI


class Level:
    
    def __init__(self):
        
        #nos traemos la pantalla
        self.running = False
        self.display_surface = pygame.display.get_surface()
        
        #hacemos grupos de sprites
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        
        self.current_attack = None
        
        #creamos los sprites
        self.create_map()
        
        self.ui = UI()
        
    
    def create_map(self):
        layouts = {
            'grass': import_csv_layout("../map/Mapa_grass.csv"),     
            'rock': import_csv_layout("../map/Mapa_rock.csv"), 
            }
        graphics = {
            "grass": import_folder("../graphics/plains/grass"),
            "rock": import_folder("../graphics/plains/rock"),
            
            }
        
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        # if style == "grass":
                        #     random_grass_image=choice(graphics['grass'])
                        #     Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)
                        if style == "grass":
                            grass_image=graphics['grass'][int(col)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'grass', grass_image)     
                        if style == "rock":
                            rock_image=graphics['rock'][int(col)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'rock', rock_image)                            
        
        
        self.player = Player(
            (200,200),
            [self.visible_sprites], 
            self.obstacle_sprites, 
            self.create_attack, 
            self.destroy_attack,
            self.create_magic) 
     
        
     
    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])
        
    
    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None
        
    def create_magic(self, style, strength, cost):
        print(style)
        print(strength)
        print(cost)
    
    def run(self):
        self.running = True
        #actualizamos el juego
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        #debug(self.player.status)
        self.ui.display(self.player)
        
        
class YSortCameraGroup(pygame.sprite.Group):
    
    def __init__(self):
        
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2 
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        
        #creamos el suelo
        self.floor_surf = pygame.image.load("../graphics/plains/Plains.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0,0))
        
        
        
        
    def custom_draw(self, player):
        
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        
        
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
        
    
    
    
    
    