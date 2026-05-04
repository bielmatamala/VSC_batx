import sys
import os

directori_arrel = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(directori_arrel, 'GAME'))

from Main_Screen.main import main_screen
from GAME.main import main

while True:
    main_screen()
    if main_screen() == False:
        break
    else:
        if __name__ == "__main__":
            main()


"""
from Main_Screen_final.main import main_screen_final

if __name__ == "__main__":
    while True:
        # 1. Mostra la pantalla inicial
        resultat = main_screen()
        if resultat == False:
            break

        # 2. Executa la partida
        main()

        # 3. Mostra la pantalla final amb puntuació
        resultat = main_screen_final()
        if resultat == False:
            break"""