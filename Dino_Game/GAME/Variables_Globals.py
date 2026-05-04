import pygame as PG
import os

DIRECTORI_BASE = os.path.dirname(os.path.abspath(__file__))

RUNNING_porva = [PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Dino - copia", r"R_1.png")),
           PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Dino - copia", r"R_2.png"))]

RUNNING = [PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Dino", r"DinoRun1.png")),
           PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Dino", r"DinoRun2.png"))]

JUMPING = PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Dino", r"DinoJump.png"))

DOWNING = [PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Dino", r"Dinoajupit1.png")),
           PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Dino", r"Dinoajupit2.png"))]

SMALL_CACTUS = [PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Cactus", r"SmallCactus1.png")),
                PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Cactus", r"SmallCactus2.png")),
                PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Cactus", r"SmallCactus3.png"))]

LARGE_CACTUS = [PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Cactus", r"LargeCactus1.png")),
                PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Cactus", r"LargeCactus2.png")),
                PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Cactus", r"LargeCactus3.png"))]

BIRD = [PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Bird", r"Bird1.png")),
        PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Bird", r"Bird2.png"))]

CLOUD = PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Other", r"Cloud.png"))

BG = PG.image.load(os.path.join(DIRECTORI_BASE, r"Assets\Other", r"Track.png"))