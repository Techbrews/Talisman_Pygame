# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 10:30:09 2022

@author: TechBrews
"""

import pygame
import sys
from settings import *
from level import *
from button import *
from pyvidplayer import Video



class Game:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Talisman")
        self.clock = pygame.time.Clock()
        self.game_paused = False
        self.menu_state = "main"
        self.font = pygame.font.SysFont(None, 40)
        self.level = Level()
        self.vid = Video("../graphics/test/Intro.mp4") #video de la intro
        self.vid.set_size((WIDTH,HEIGTH))  
        self.titulo = pygame.image.load("../graphics/test/Titulo.png").convert_alpha()
        self.titulo = pygame.transform.scale(self.titulo, (736, 248))
        
        main_sound = pygame.mixer.Sound('../audio/music/musica.mp3')
        main_sound.set_volume(1)
        main_sound.play(loops = -1)
        
        
        
        self.button1 = Button(self.screen, "Continuar partida", 200,40,(570,270),5)
        self.button2 = Button(self.screen, "Opciones", 200,40,(570,350),5)
        self.button3 = Button(self.screen, "Salir", 200,40,(570,550),5)
        self.button4 = Button(self.screen, "Controles", 200,40,(570,270),5)
        self.button5 = Button(self.screen, "Audio ", 200,40,(570,350),5)
        self.button6 = Button(self.screen, "Volver", 200,40,(570,430),5)
        self.button7 = Button(self.screen, "Si", 200,40,(570,325),5)
        self.button8 = Button(self.screen, "No", 200,40,(570,400),5)
        
        
        
    def draw_text(self, text, font, text_col, x, y ):
        self.screen.blit(font.render(text, True, text_col), (x,y))


  
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.vid.close() #Si me dan a espacio cierro el video
                        self.menu_state = "main"
                        self.game_paused = True
                        
                        
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            #pintamos el fondo
            self.screen.fill(((204,211,168)))
            


            print(self.game_paused)
            print(self.menu_state)
            if self.game_paused == True:
                #sonido

                #comprobamos el menu
                
                self.screen.blit(self.titulo, (300,10))
                
                
                if self.menu_state == "salir":
                    self.draw_text("¿Desea salir de verdad?", self.font, ((255,255,255)), 515,270)
                    self.button7.draw()
                    self.button8.draw()
                    
                    if self.button7.pressed == True:
                        pygame.quit()
                        sys.exit()
                    if self.button8.pressed == True:
                        self.menu_state = "main"       
                        self.button8.pressed = False                
                
                
                
                
                if self.menu_state == "options":
                    
                    self.button4.draw()
                    self.button5.draw()
                    self.button6.draw()
                
                    if self.button4.pressed == True:
                        self.button4.pressed = False #fuerzo el apagado del boton
                        
                    if self.button5.pressed == True:
                        self.button5.pressed = False
                    
                    if self.button6.pressed == True:
                        self.menu_state = "main"       
                        self.button6.pressed = False
                

                
                if self.menu_state == "main":   
                    self.button1.draw()
                    self.button2.draw()
                    self.button3.draw()
        
                    if self.button1.pressed == True:
                        self.menu_state = "run_level"
                        self.game_paused = False
                        self.button1.pressed = False #fuerzo el apagado del boton
                        
                    if self.button2.pressed == True:
                        self.menu_state = "options"
                        self.button2.pressed = False
                        
                    if self.button3.pressed == True:
                        #confirmación de salir
                        self.menu_state = "salir"
                        self.button3.pressed = False
                        

            else:
                
                if self.level.running==False:
                    
                    self.vid.draw(self.screen, (0, 0))
                    self.draw_text("Pulsa ESPACIO para continuar...", self.font, ((255,255,255)), 450,600)

                
                if self.menu_state == "run_level" :
                    
                    self.level.run()
                    

            #self.screen.fill("black")
            #self.screen.fill(((52,78,91)))
            
            #ACTUALIZAMOS EL FONDO
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()

