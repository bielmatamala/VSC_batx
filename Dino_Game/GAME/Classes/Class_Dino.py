import pygame as PG
from GAME.Variables_Globals import RUNNING, JUMPING, DOWNING

# Classe que representa el dinosaure del jugador
class Dinosaur:
    # Constants de posició
    X_POS = 100
    Y_POS = 430
    Y_POS_DUCK = 460
    JUMP_VEL = 8.5

    def __init__(self):
        # Imatges de cada moviment
        self.duck_img = DOWNING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        # Booleanes que controlen l'estat
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0 # Índex per a l'animació del dinosaure
        self.jump_vel = self.JUMP_VEL  # Velocitat actual del salt
        self.image = self.run_img[0] # Imatge actual en pantalla

        # Rectangle per a col·lisió i posició
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
    
    def update(self, userInput):
        # Fa el moviment actual del dinosaure
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        # Reinicia l'índex d'animació quan arriba al final
        if self.step_index >= 10:
            self.step_index = 0

        # Detecta entrada de l'usuari i canvia l'estat del dinosaure
        if userInput[PG.K_UP] or userInput[PG.K_SPACE] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[PG.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[PG.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def run(self):
        # Animació del dinosaure corrent
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
    
    def jump(self):
        # Animació del salt del dinosaure
        PG.mixer.music.load(r"C:\Users\AppJT\Dinogames\Dino_Game\GAME\Assets\Other\jump.mp3")
        PG.mixer.music.play()
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 # Mou el dinosaure cap a amunt
            self.jump_vel -= 0.8 # Disminueix la velocitat per crear l'efecte de salt
            
        # Quan la velocitat arriba al límit, finalitza el salt
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
    
    def duck(self):
        # Animació del dinosaure abaixant-se
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1
    
    def draw(self, SCREEN):
        # Dibuixa el dinosaure a la pantalla
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
