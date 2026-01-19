#----------------------------------3 en ratlla-------------------------------------------------------------------º
Taulell = {
    "A1": " ", "A2": " ", "A3": " ",
    "B1": " ", "B2": " ", "B3": " ",
    "C1": " ", "C2": " ", "C3": " "
} 

def imprimir_taulell(Taulell):
    print("   1   2   3")
    print(f"A  {Taulell['A1']} | {Taulell['A2']} | {Taulell['A3']}")
    print("  ---+---+---")
    print(f"B  {Taulell['B1']} | {Taulell['B2']} | {Taulell['B3']}")
    print("  ---+---+---")
    print(f"C  {Taulell['C1']} | {Taulell['C2']} | {Taulell['C3']}")
    
    
def comprovacio_victoria():
    combinacions = [
        ["A1", "A2", "A3"],
        ["B1", "B2", "B3"],
        ["C1", "C2", "C3"],
        ["A1", "B1", "C1"],
        ["A2", "B2", "C2"],
        ["A3", "B3", "C3"],
        ["A1", "B2", "C3"],
        ["A3", "B2", "C1"]
    ]
    for combo in combinacions:
        valors = [Taulell[pos] for pos in combo]
        if valors == ["X", "X", "X"]:
            return "X"
        elif valors == ["O", "O", "O"]:
            return "O"
    # comprovar empat
    if all(v != " " for v in Taulell.values()):
        return "Empat"

def reiniciar_taulell():
    for key in Taulell.keys():
        Taulell[key] = " "

def jugar_partida():
    global jugador_1, contador_j1, contador_j2, forma_jugaador_1, forma_jugaador_2, Taulell, jugador_1
    reiniciar_taulell()
    print(imprimir_taulell(Taulell))
    while True:
        if jugador_1:
            posicio = input("Jugador 1, introdueix la teva posició: ").upper()
            if Taulell.get(posicio) == " ":
                Taulell[posicio] = forma_jugaador_1
                jugador_1 = False
            else:
                print("Posició ocupada, torna-ho a intentar.")
                continue
        else:
            posicio = input("Jugador 2, introdueix la teva posició: ").upper()
            if Taulell.get(posicio) == " ":
                Taulell[posicio] = forma_jugaador_2
                jugador_1 = True
            else:
                print("Posició ocupada, torna-ho a intentar.")
                continue

        # update displays
        print(imprimir_taulell(Taulell))
        guanyador = comprovacio_victoria()
        if guanyador == "X":
            print("Jugador 1 ha guanyat!")
            contador_j1 += 3
            break
        elif guanyador == "O":
            print("Jugador 2 ha guanyat!")
            contador_j2 += 3
            break
        elif guanyador == "Empat":
            print("La partida ha acabat en empat!")
            contador_j1 += 1
            contador_j2 += 1
            break

"""def jugar_partida_root():
    global jugador_1, contador_j1, contador_j2
    reiniciar_taulell()
    # create a GUI label using a monospace font for proper alignment
    board_var = StringVar()
    label = Label( textvariable=board_var, font=("Courier", 14), justify=LEFT, anchor='w')
    label.pack()
    # show initial board in console and GUI
    print(imprimir_taulell(Taulell))
    board_var.set(imprimir_taulell(Taulell))
    root.update()
    while True:
        if jugador_1:
            posicio = input("Jugador 1, introdueix la teva posició: ").upper()
            if Taulell.get(posicio) == " ":
                Taulell[posicio] = forma_jugaador_1
                jugador_1 = False
            else:
                print("Posició ocupada, torna-ho a intentar.")
                continue
        else:
            posicio = input("Jugador 2, introdueix la teva posició: ").upper()
            if Taulell.get(posicio) == " ":
                Taulell[posicio] = forma_jugaador_2
                jugador_1 = True
            else:
                print("Posició ocupada, torna-ho a intentar.")
                continue

        # update displays
        print(imprimir_taulell(Taulell))
        board_var.set(imprimir_taulell(Taulell))
        root.update()
        guanyador = comprovacio_victoria()
        if guanyador == "X":
            print("Jugador 1 ha guanyat!")
            contador_j1 += 3
            break
        elif guanyador == "O":
            print("Jugador 2 ha guanyat!")
            contador_j2 += 3
            break
        elif guanyador == "Empat":
            print("La partida ha acabat en empat!")
            contador_j1 += 1
            contador_j2 += 1
            break"""
#----------------------------------GUI-------------------------------------------------------------------
#-----------------------------Variables Globals----------------------------------------------------------
forma_jugaador_1 = "X"
forma_jugaador_2 = "O"
jugador_1 = True
contador_j1 = 0
contador_j2 = 0



num_partides = int(input("Quantes partides vols fer? "))
for i in range(num_partides):
    print(f"\n--- Partida {i+1} ---")
    jugar_partida()

print("\nPuntuació Final:")
print(f"Jugador 1: {contador_j1}")
print(f"Jugador 2: {contador_j2}")
