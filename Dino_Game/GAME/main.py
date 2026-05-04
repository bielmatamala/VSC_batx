import pygame as PG
import random
import os
from GAME.Styles.Style import SCREEN, WHITE
from GAME.Variables_Globals import RUNNING, JUMPING, DOWNING, SMALL_CACTUS, LARGE_CACTUS, BIRD, CLOUD, BG
from GAME.Classes.Class_Dino import Dinosaur
from GAME.Classes.Class_Obstacle import Obstacle
from GAME.Classes.Class_Cloud import Cloud
from GAME.Classes.Class_Bird import Bird
from GAME.Classes.Class_Cactus.Class_SmallCactus import SmallCactus
from GAME.Classes.Class_Cactus.Class_LargeCacuts import LargeCactus


# Inicializar Pygame
PG.init()


#Programa principal
def main():
    run = True
    Dino = Dinosaur()
    clock = PG.time.Clock()
    cloud = Cloud()
    game_speed = 20
    points = 0
    obstacles = []
    font = PG.font.Font('freesansbold.ttf', 20)
    x_pos_bg = 0
    y_pos_bg = 500
    p = 0

    while run:
        PG.mixer.music.load(r"C:\Users\AppJT\Dinogames\Dino_Game\GAME\Assets\Sons\43861138-jurassic-park-210987.mp3")
        PG.mixer.music.play(-1)
        for event in PG.event.get():
            if event.type == PG.QUIT:
                run = False

        SCREEN.fill(WHITE)
        userInput = PG.key.get_pressed()
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg)) # Dibuixa una segona imatge darrere
        
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0 # Torna a començar el bucle d'imatges
        x_pos_bg -= game_speed

        # Cridar calsse del dinosuare
        dino_class_call(Dino, userInput)

        # Cridar calsse del núvol
        cloud_class_call(cloud, game_speed)

        # Crear obstacles aleatòriament
        Create_obstacles(obstacles)

        # Crida a les classes dels obstacles
        for obstacle in obstacles[:]:
            obstacle.draw(SCREEN)
            if not obstacle.update(game_speed):
                obstacles.remove(obstacle)
                continue
            if Dino.dino_rect.colliderect(obstacle.rect):
                PG.mixer.music.stop()
                run = False
                finalscreen(points)
                break

        if userInput[PG.K_ESCAPE]: #Si el jugador prem la tecla ESC el joc, es reinicia
            run = False # S'atura el joc

        if userInput[PG.K_p]: #Si el jugador prem la tecla P, el joc es pausa
            run = False
        
        # Puntuació
        points += 1
        if points % 100 == 0:
         game_speed += 1
        # Ensenyar els punts per pantalla
        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN.get_width() // 2, 40)
        SCREEN.blit(text, textRect)

        if points / 100 == p:
            PG.mixer.music.load(r"C:\Users\AppJT\Dinogames\Dino_Game\GAME\Assets\Other\point.mp3")
            PG.mixer.music.play()
            p += 1
        
        clock.tick(30)
        PG.display.update()

def finalscreen(points):
    if points > 0:
        from Main_Screen_final.main import main_screen_final
        main_screen_final(points)
        PG.time.delay(5)


def punts_compt():
    points += 1
    if points % 100 == 0:
        game_speed += 1
    return points


def Create_obstacles(obstacles):
    if len(obstacles) == 0:
        obstacle_tipus = random.randint(0,2)
        if obstacle_tipus == 0:
            obstacles.append(SmallCactus(SMALL_CACTUS))
        elif obstacle_tipus == 1:
            obstacles.append(LargeCactus(LARGE_CACTUS))
        else:
            obstacles.append(Bird(BIRD))

def cloud_class_call(cloud, game_speed):
    cloud.draw(SCREEN)
    cloud.update(game_speed)

def dino_class_call(Dino, userInput):
    Dino.draw(SCREEN)
    Dino.update(userInput)

if __name__ == "__main__":
    
    main()