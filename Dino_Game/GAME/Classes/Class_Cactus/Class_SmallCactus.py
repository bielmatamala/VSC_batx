from GAME.Classes.Class_Obstacle import Obstacle
import pygame as PG
import random
import os
from GAME.Styles.Style import SCREEN
from GAME.Variables_Globals import SMALL_CACTUS

# Classe del cactus petit que hereta de Obstacle
class SmallCactus(Obstacle):
    def __init__(self, image):
        # Selecciona aleatòriament una de les tres variants del cactus
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
