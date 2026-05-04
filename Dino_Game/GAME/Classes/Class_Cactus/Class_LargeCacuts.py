from GAME.Classes.Class_Obstacle import Obstacle
import pygame as PG
import random
import os
from GAME.Styles.Style import SCREEN
from GAME.Variables_Globals import LARGE_CACTUS

# Classe del cactus gran que hereta de Obstacle
class LargeCactus(Obstacle):
    def __init__(self, image):
        # Selecciona aleatòriament una de les tres variants del cactus
        self.type = random.randint(0, 2)
        # Crida el constructor del pare (Obstacle)
        super().__init__(image, self.type)
