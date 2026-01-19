import time

username = {
    'admin': '123',
    'familia': '123',
    'convidats': '123',
}

# Menú d'opcions
menu = {
    'descareges',
    'musica',
    'video',
    'imatges',
    'documents',
    'calculadora MRUA',
    'configuracio',
    'viatjar',
    'exit',
}

# Continguts
descareges = {
    'ghub',
    'steam',
    'arxiu.zip',
    'lightroom',
}
musica = {
    'ja dormire',
    'houdini',
    '2002',
    'dins del meu cap',
}
video = {
    'familia 90 anys',
    '27/11/2020',
}
imatges = {
    'img 0078.jpg',
    'img 6534.jpg',
    'img 2437.jpg',
}
documents = {
    'document 0078.doc',
    'grammar practice.doc',
    'els mobils i la falta de son',
}
configuracio = {
    'afegir usuari',
    'treure usuari',
    'editar usuari',
}
punt = "."
calcualdora_mrua = {
    'a',
    'Av',
    'At',
    'Vf',
    'Xf',
}

# Inici del programa
print("Usuari i contrasenya")
user_input_username = input("Introdueix el teu usuari: ")
user_input_password = input("Introdueix la teva contrasenya: ")

if user_input_username in username and username[
        user_input_username] == user_input_password:
    print("Benvingut")
    while True:
        print("Què vols fer?")
        user_input_menu = input(f"Tria una opció: {', '.join(sorted(menu))} ")
        if user_input_menu in menu:
            print(f"Has escollit {user_input_menu}")

            if user_input_menu == 'descareges':
                print(sorted(descareges))
                if user_input_username == 'admin' or user_input_username == 'familia':
                    user_input_descareges = input("Què vols descarregar? ")
                    if user_input_descareges in descareges:
                        print("Usuari i contrasenya")
                        user_input_username = input(
                            "Introdueix el teu usuari: ")
                        user_input_password = input(
                            "Introdueix la teva contrasenya: ")
                        if user_input_username == 'admin' and user_input_password == '123':
                            print("Descarregant...")
                        time.sleep(5)
                        print(f"Descarregat {user_input_descareges}")
                elif user_input_username == 'convidats':
                    user_input_descareges = input("Què vols descarregar? ")
                    print("no pots descarregar res perquè ets convidat")
                    time.sleep(5)
            elif user_input_menu == 'musica':
                print(sorted(musica))
                if user_input_username == 'admin' or user_input_username == 'familia':
                    user_input_musica = input("Què vols escoltar? ")
                    if user_input_musica in musica:
                        print("Usuari i contrasenya")
                        user_input_username = input(
                            "Introdueix el teu usuari: ")
                        user_input_password = input(
                            "Introdueix la teva contrasenya: ")
                        if user_input_username == 'admin' and user_input_password == '123':
                            print("Reproduint...")
                            time.sleep(5)
                            print(f"Reproduït {user_input_musica}")
                            time.sleep(1)
            elif user_input_menu == 'video':
                print(sorted(video))
                if user_input_username == 'admin' or user_input_username == 'familia':
                    user_input_video = input("Què vols veure? ")
                    if user_input_video in video:
                        print("Usuari i contrasenya")
                        user_input_username = input(
                            "Introdueix el teu usuari: ")
                        user_input_password = input(
                            "Introdueix la teva contrasenya: ")
                        if user_input_username == 'admin' and user_input_password == '123':
                            print("Reproduint...")
                        time.sleep(5)
                        print(f"Reproduït {user_input_video}")

            elif user_input_menu == 'imatges':
                print(sorted(imatges))
                if user_input_username == 'admin' or user_input_username == 'familia':
                    user_input_imatges = input("Quina imatge vols veure? ")
                    if user_input_imatges in imatges:
                        print("Usuari i contrasenya")
                        user_input_username = input(
                            "Introdueix el teu usuari: ")
                        user_input_password = input(
                            "Introdueix la teva contrasenya: ")
                        if user_input_username == 'admin' and user_input_password == '123':
                            print("Mostrant...")
                        time.sleep(5)
                        print(f"Mostrat {user_input_imatges}")

            elif user_input_menu == 'documents':
                print(documents)
                if user_input_username == 'admin' or user_input_username == 'familia':
                    user_input_documents = input("Quin document vols veure? ")
                    if user_input_documents in documents:
                        print("Usuari i contrasenya")
                        user_input_username = input(
                            "Introdueix el teu usuari: ")
                        user_input_password = input(
                            "Introdueix la teva contrasenya: ")
                        if user_input_username == 'admin' and user_input_password == '123':
                            print("Mostrant...")
                        time.sleep(5)
                        print(f"Mostrat {user_input_documents}")
            elif user_input_menu == 'calculadora MRUA':
                print(calcualdora_mrua)
                opcio = input("tria la incognita que vols trobar: ")
                if opcio == "a":
                    Vo = float(input("introdueix la velocitat inicial: "))
                    Vf = float(input("introdueix la velocitat final: "))
                    To = float(input("introdueix el temps inicial: "))
                    Tf = float(input("introdueix el temps final: "))
                    resultat = (Vf - Vo) / (Tf - To)
                    print(resultat)

                elif opcio == "Av":
                    a = float(input("introdeix la acceleracio: "))
                    To = float(input("introdueix el temps inicial: "))
                    Tf = float(input("introdueix el temps final: "))
                    resultat2 = a * (Tf - To)
                    print(resultat2)

                elif opcio == "At":
                    a = float(input("introdeix la acceleracio: "))
                    Vo = float(input("introdueix la velocitat inicial: "))
                    Vf = float(input("introdueix la velocitat final: "))
                    resultat3 = (Vf - Vo) / a
                    print(resultat3)

                elif opcio == "Vf":
                    Vo = float(input("introdueix la velocitat inicial: "))
                    a = float(input("introdueix la acceleracio: "))
                    To = float(input("introdueix el temps inicial: "))
                    Tf = float(input("introdueix el temps final: "))
                    resultat4 = Vo + a * (Tf - To)
                    print(resultat4)

                elif opcio == "Xf":
                    Vo = float(input("introdueix la velocitat inicial: "))
                    Xo = float(input("introdueix la posicio inicial: "))
                    a = float(input("introdueix la acceleracio: "))
                    Tf = float(input("introdueix el temps final: "))
                    To = float(input("introdueix el temps inicial: "))
                    resultat5 = Xo + Vo * (Tf - To) + 0.5 * a * (Tf - To)**2
                    print(resultat5)

                arrodonir = input("vols arrodonir el resultat? ")
                if arrodonir == "si":
                    decimals = int(input("quants decimals vols arrodonir? "))
                    if opcio == "a":
                        print(round(resultat, decimals))
                    elif opcio == "Av":
                        print(round(resultat2, decimals))
                    elif opcio == "At":
                        print(round(resultat3, decimals))
                    elif opcio == "Vf":
                        print(round(resultat4, decimals))
                    elif opcio == "Xf":
                        print(round(resultat5, decimals))

                resposta = input("Vols canviar les unitats a m/s? (si/no): ")

                if resposta == "si":

                    canvi = input(
                        "A quines unitats vols canviar (km/h o m/s)?: ")

                    if canvi == "km/h":
                        nombre = input("Introdueix el valor en km/h: ")
                        resultatkm = float(nombre) * 1000 / 3600
                        print(f"{resultatkm} m/s")

                    elif canvi == "km/s":
                        nombre = input("Introdueix el valor en m/s: ")
                        resultatms = float(nombre) * 1000 * 3600
                        print(f"{resultatms} m/s")

                elif resposta == "no":
                    print("No es farà el canvi d'unitats.")
            elif user_input_menu == 'configuracio':
                print(configuracio)
                if user_input_username == 'admin':
                    print("afegir usuari, treure usuari, editar usuari")
                    user_input_configuracio = input("Què vols fer? ")
                    if user_input_configuracio == 'afegir usuari':
                        user_input_username = input(
                            "Introdueix el teu usuari: ")
                        user_input_password = input(
                            "Introdueix la teva contrasenya: ")
                        if user_input_username == 'admin' and user_input_password == '123':
                            time.sleep(2)
                        usuari_nou = input(
                            "Introdueix el nom del nou usuari : i la contrasenya"
                        )
                        username.append(usuari_nou)
                        # username["usari_nou"] = usuari_nou
                        # print(f"S'ha afegit l'usuari {usuari_nou}")
                    elif user_input_configuracio == 'treure usuari':
                        user_input_username = input(
                            "Introdueix el teu usuari: ")
                        user_input_password = input(
                            "Introdueix la teva contrasenya: ")
                        if user_input_username == 'admin' and user_input_password == '123':
                            time.sleep(2)
                        usuari_nou = input(
                            "Introdueix el nom del usuari que vols treure: ")
                        del username[usuari_nou]
                        print(f"S'ha tret l'usuari {usuari_nou}")
                else:
                    print(
                        "No pots fer aquesta acció perquè no ets administrador"
                    )

            elif user_input_menu == 'viatjar':
                print(
                    "https://landbot.online/v3/H-2775206-6P3AOFD16UGVM00S/index.html"
                )

            elif user_input_menu == 'exit':
                print("Apagant programa.")
                time.sleep(0.1)
                print("Apagant programa..")
                time.sleep(0.1)
                print("Apagant programa...")
                time.sleep(0.1)
                print("Apagant programa..")
                time.sleep(0.1)
                print("Apagant programa.")
                time.sleep(0.1)
                break


            elif user_input_menu == "back":
                print(menu)

            else:
                print("No tens permisos per veure aquest document")
        else:
            print("Opció no vàlida.")
else:
    print("Usuari o contrasenya incorrectes")
