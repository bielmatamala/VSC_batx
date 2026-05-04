#pantalla principal abans de començar el joc, on es mostra els contols i el nonms del joc
import pygame as PG
from GAME.Styles.Style import SCREEN, WHITE, font
import GAME.Assets.Dino
from Main_Screen_final.main import punts
def main_screen():
    PG.init()
    PG.display.set_caption("Dino Game")
    run = False
    if not run:
        SCREEN.fill(WHITE)
        imatge, imatge_rect = image()
        text, text_rect = text_1(imatge_rect)
        text2, text_rect2 = text_2(text_rect)
        SCREEN.blit(imatge, imatge_rect)
        SCREEN.blit(text, text_rect)
        SCREEN.blit(text2, text_rect2)
        PG.display.update()
        if PG.key.get_pressed()[PG.K_ESCAPE]: # Si el jugador prem la tecla ESC, es tanca el joc
            return False
        else:
            while not run:
                for event in PG.event.get():
                    if event.type == PG.QUIT:
                        run = True
                    if event.type == PG.KEYDOWN:
                        run = True
      
    
    else: 
        run = False

def text_2(text_rect):
    text2 = font.render("o Esc per acabar", True, (0, 0, 0))
    text_rect2 = text2.get_rect(center=(SCREEN.get_width() // 2, text_rect.bottom + 40))
    return text2,text_rect2

def text_1(imatge_rect):
    text = font.render("Prem una tecla per començar", True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN.get_width() // 2, imatge_rect.bottom + 40))
    return text,text_rect

def image():
    imatge = PG.image.load(r"C:\Users\AppJT\Dinogames\Dino_Game\GAME\Assets\Dino\DinoStart.png")
    imatge_size = (250, 250)
    imatge = PG.transform.scale(imatge, imatge_size)
    imatge_rect = imatge.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 180))
    return imatge,imatge_rect