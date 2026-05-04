import pygame as PG
from GAME.Styles.Style import SCREEN_WIDTH
from GAME.Classes.Class_Dino import Dinosaur
from GAME.Variables_Globals import RUNNING

# Classe base per a tots els obstacles
class Obstacle:
    def __init__(self, image, type):
        # Emmagatzema la imatge i el tipus de l'obstacle
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect() # Crea el rectangle de col·lisió a partir de la imatge
        self.rect.x = SCREEN_WIDTH # Posiciona l'obstacle a la dreta de la pantalla
        ground_y = Dinosaur.Y_POS + RUNNING[0].get_height()
        self.rect.y = ground_y - self.rect.height

    def update(self, game_speed):
        self.rect.x -= game_speed # Mou l'obstacle cap a l'esquerra depenent la velocitat del joc
        if self.rect.x < -self.rect.width: 
            return False # Retorna False si l'obstacle surt de la pantalla (per a eliminar-lo)
        return True

    def draw(self, SCREEN):
        # Dibuixa l'obstacle a la pantalla
        SCREEN.blit(self.image[self.type], self.rect)