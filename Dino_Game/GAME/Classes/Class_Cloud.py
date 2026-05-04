import pygame as PG
import random
import os
from GAME.Styles.Style import SCREEN
from GAME.Variables_Globals import CLOUD

# Classe del núvol que apareix de fons
class Cloud:
    def __init__(self):
        # Posiciona el núvol aleatòriament a la dreta de la pantalla
        self.x = 1100 + random.randint(800, 1000)
        self.y = random.randint(120, 180)
        self.image = CLOUD
        self.width = self.image.get_width() # Ample de la imatge per a detectar quan surt de la pantalla

    def update(self, game_speed):
        self.x -= game_speed # Mou el núvol cap a l'esquerra segons la velocitat del joc
        # Si el núvol surt de la pantalla, el reposiciona a la dreta
        if self.x < -self.width:
            self.x = 1100 + random.randint(2500, 3000)
            self.y = random.randint(120, 180)

    def draw(self, SCREEN):
        # Dibuixa el núvol a la pantalla
        SCREEN.blit(self.image, (self.x, self.y))