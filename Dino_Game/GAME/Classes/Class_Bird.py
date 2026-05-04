from GAME.Classes.Class_Obstacle import Obstacle
import pygame as PG
import os
from GAME.Styles.Style import SCREEN
from GAME.Variables_Globals import BIRD

# Classe de l'ocell que hereta de Obstacle
class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0 # Tipus 0 significa que és un ocell
        super().__init__(image, self.type)

        compencacio_vol = 80
        self.rect.y -= compencacio_vol
        self.index = 0 #Índex per a l'animació de l'ocell

    def draw(self, SCREEN):
        # Anima l'ocell canviant entre les dues imatges
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)  # Dibuixa la imatge corresponent a l'animació
        self.index += 1 # Incrementa l'índex per a la següent frame d'animació
