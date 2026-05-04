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


