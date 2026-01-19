N = 20
llista_joc = list(range(0, N))

def decisio_jugarr():
    user_input = input("Vols jugar una partida? (s/n): ").strip().lower()
    if user_input == "s":
        return True
    else:
        return False

def demana_index():
    user_input_index = input(f"Introdueix un index entre 0 i {N-1}: ").strip()
    return int(user_input_index)

def demana_string():
    user_input_string = input("Introdueix una cadena de text: ").strip().lower()
    return user_input_string

def substitucio_index(user_input_index, user_input_string):
    llista_joc[user_input_index] = user_input_string

def mostra_llista():
    print("Llista actualitzada:", llista_joc)

while decisio_jugarr() == True:
    user_demana = demana_index()
    user_string = demana_string()
    substitucio_index(user_demana, user_string)
    mostra_llista()
    break

print("---------------------------------------------------------------------------------------------------")

