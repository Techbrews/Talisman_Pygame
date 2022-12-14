# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 10:34:33 2022

@author: TechBrews
"""

WIDTH   = 1280
HEIGTH  = 720
FPS     = 60
TILESIZE = 64  


#UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../font/Pixeltype.ttf'
UI_FONT_SIZE = 18

#general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

#UI COLOR
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'



# weapons 
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphics':'../graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphics':'../graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphics':'../graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphics':'../graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphics':'../graphics/weapons/sai/full.png'}}

# magic
magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphics':'../graphics/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphics':'../graphics/particles/heal/heal.png'}}