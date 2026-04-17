import time

USERS = {
    'admin': '123',
    'familia': '123',
    'convidats': '123',
}

MENU = [
    'descareges',
    'musica',
    'video',
    'imatges',
    'documents',
    'calculadora MRUA',
    'configuracio',
    'viatjar',
    'exit',
]

DESCAREGES = {
    'ghub',
    'steam',
    'arxiu.zip',
    'lightroom',
}
MUSICA_CONTENT = {
    'ja dormire',
    'La Familia',
    '2002',
    'dins del meu cap',
}
VIDEO_CONTENT = {
    'familia 90 anys',
    '27/11/2020',
}
IMATGES = {
    'img 0078.jpg',
    'img 6534.jpg',
    'img 2437.jpg',
}
DOCUMENTS = {
    'document 0078.doc',
    'grammar practice.doc',
    'els mobils i la falta de son',
}
CONFIGURACIO = [
    'afegir usuari',
    'treure usuari',
    'editar usuari',
]

CALCULADORA_MRUA = [
    'a',
    'Av',
    'At',
    'Vf',
    'Xf',
]


def authenticate_user(username, password):
    return USERS.get(username) == password


def prompt_credentials():
    username = input('Introdueix el teu usuari: ')
    password = input('Introdueix la teva contrasenya: ')
    return username, password


def confirm_admin():
    print('Autenticació d\'administrador necessària')
    username, password = prompt_credentials()
    return username == 'admin' and authenticate_user(username, password)


def video(video_content, current_user):
    print(sorted(video_content))
    if current_user in ('admin', 'familia'):
        user_input_video = input('Què vols veure? ')
        if user_input_video in video_content:
            if confirm_admin():
                print('Reproduint...')
                time.sleep(5)
                print(f'Reproduït {user_input_video}')
            else:
                print('Autenticació incorrecta.')
    else:
        print('No tens permisos per veure vídeos.')
    return current_user


def musica(musica_content, current_user):
    print(sorted(musica_content))
    if current_user in ('admin', 'familia'):
        user_input_musica = input('Què vols escoltar? ')
        if user_input_musica in musica_content:
            if confirm_admin():
                print('Reproduint...')
                time.sleep(5)
                print(f'Reproduït {user_input_musica}')
            else:
                print('Autenticació incorrecta.')
    else:
        print('No tens permisos per escoltar música.')
    return current_user


def show_descareges(descareges, current_user):
    print(sorted(descareges))
    if current_user in ('admin', 'familia'):
        user_input_descareges = input('Què vols descarregar? ')
        if user_input_descareges in descareges:
            if confirm_admin():
                print('Descarregant...')
                time.sleep(5)
                print(f'Descarregat {user_input_descareges}')
            else:
                print('Autenticació incorrecta.')
    elif current_user == 'convidats':
        input('Què vols descarregar? ')
        print('No pots descarregar res perquè ets convidat.')
        time.sleep(2)
    else:
        print('No tens permisos per descarregar.')
    return current_user


def show_imatges(imatges, current_user):
    print(sorted(imatges))
    if current_user in ('admin', 'familia'):
        user_input_imatges = input('Quina imatge vols veure? ')
        if user_input_imatges in imatges:
            if confirm_admin():
                print('Mostrant...')
                time.sleep(2)
                print(f'Mostrat {user_input_imatges}')
            else:
                print('Autenticació incorrecta.')
    else:
        print('No tens permisos per veure imatges.')
    return current_user


def docs(documents, current_user):
    print(sorted(documents))
    if current_user in ('admin', 'familia'):
        user_input_documents = input('Quin document vols veure? ')
        if user_input_documents in documents:
            if confirm_admin():
                print('Mostrant...')
                time.sleep(2)
                print(f'Mostrat {user_input_documents}')
            else:
                print('Autenticació incorrecta.')
    else:
        print('No tens permisos per veure documents.')
    return current_user


def MRUA_a():
    Vo = float(input('Introdueix la velocitat inicial: '))
    Vf = float(input('Introdueix la velocitat final: '))
    To = float(input('Introdueix el temps inicial: '))
    Tf = float(input('Introdueix el temps final: '))
    resultat = (Vf - Vo) / (Tf - To)
    print(resultat)
    return resultat


def MRUA_av():
    a = float(input('Introdueix la acceleracio: '))
    To = float(input('Introdueix el temps inicial: '))
    Tf = float(input('Introdueix el temps final: '))
    resultat2 = a * (Tf - To)
    print(resultat2)
    return resultat2


def MRUA_at():
    a = float(input('Introdueix la acceleracio: '))
    Vo = float(input('Introdueix la velocitat inicial: '))
    Vf = float(input('Introdueix la velocitat final: '))
    resultat3 = (Vf - Vo) / a
    print(resultat3)
    return resultat3


def MRUA_vf():
    Vo = float(input('Introdueix la velocitat inicial: '))
    a = float(input('Introdueix la acceleracio: '))
    To = float(input('Introdueix el temps inicial: '))
    Tf = float(input('Introdueix el temps final: '))
    resultat4 = Vo + a * (Tf - To)
    print(resultat4)
    return resultat4


def MRUA_xf():
    Vo = float(input('Introdueix la velocitat inicial: '))
    Xo = float(input('Introdueix la posicio inicial: '))
    a = float(input('Introdueix la acceleracio: '))
    Tf = float(input('Introdueix el temps final: '))
    To = float(input('Introdueix el temps inicial: '))
    resultat5 = Xo + Vo * (Tf - To) + 0.5 * a * (Tf - To)**2
    print(resultat5)
    return resultat5


def MRUA_arrondonir(opcio, resultat, resultat2, resultat3, resultat4, resultat5, arrodonir):
    if arrodonir.lower() == 'si':
        decimals = int(input('Quants decimals vols arrodonir? '))
        if opcio == 'a' and resultat is not None:
            print(round(resultat, decimals))
        elif opcio == 'Av' and resultat2 is not None:
            print(round(resultat2, decimals))
        elif opcio == 'At' and resultat3 is not None:
            print(round(resultat3, decimals))
        elif opcio == 'Vf' and resultat4 is not None:
            print(round(resultat4, decimals))
        elif opcio == 'Xf' and resultat5 is not None:
            print(round(resultat5, decimals))
        else:
            print('No hi ha cap resultat per arrodonir.')


def MRUA_canviUnits():
    canvi = input('A quines unitats vols canviar (km/h o m/s)?: ')
    if canvi == 'km/h':
        nombre = float(input('Introdueix el valor en m/s: '))
        resultatkm = nombre * 3600 / 1000
        print(f'{resultatkm} km/h')
    elif canvi == 'm/s':
        nombre = float(input('Introdueix el valor en km/h: '))
        resultatms = nombre * 1000 / 3600
        print(f'{resultatms} m/s')
    else:
        print('Unitat desconeguda. Escriu "km/h" o "m/s".')


def Config(users, current_user):
    print(sorted(CONFIGURACIO))
    if current_user == 'admin':
        user_input_configuracio = input('Què vols fer? ')
        if user_input_configuracio == 'afegir usuari':
            nou_usuari = input('Introdueix el nom del nou usuari: ').strip()
            if not nou_usuari:
                print('Nom d\'usuari invàlid.')
            elif nou_usuari in users:
                print(f'L\'usuari {nou_usuari} ja existeix.')
            else:
                nova_contrasenya = input('Introdueix la contrasenya del nou usuari: ')
                users[nou_usuari] = nova_contrasenya
                print(f'S\'ha afegit l\'usuari {nou_usuari}.')
        elif user_input_configuracio == 'treure usuari':
            usuari_a_treure = input('Introdueix el nom de l\'usuari que vols treure: ').strip()
            if usuari_a_treure == 'admin':
                print('No es pot treure l\'usuari admin.')
            elif usuari_a_treure in users:
                del users[usuari_a_treure]
                print(f'S\'ha tret l\'usuari {usuari_a_treure}.')
            else:
                print(f'L\'usuari {usuari_a_treure} no existeix.')
        elif user_input_configuracio == 'editar usuari':
            usuari_a_editar = input('Introdueix el nom de l\'usuari que vols editar: ').strip()
            if usuari_a_editar in users:
                nova_contrasenya = input('Introdueix la nova contrasenya: ')
                users[usuari_a_editar] = nova_contrasenya
                print(f'S\'ha modificat la contrasenya de {usuari_a_editar}.')
            else:
                print(f'L\'usuari {usuari_a_editar} no existeix.')
        else:
            print('Opció de configuració no vàlida.')
    else:
        print('No pots fer aquesta acció perquè no ets administrador.')
    return current_user


if __name__ == '__main__':
    print('Usuari i contrasenya')
    user_input_username, user_input_password = prompt_credentials()

    if authenticate_user(user_input_username, user_input_password):
        print('Benvingut')
        while True:
            print('Què vols fer?')
            user_input_menu = input(f'Tria una opció: {", ".join(sorted(MENU))} ')
            if user_input_menu in MENU:
                print(f'Has escollit {user_input_menu}')
                if user_input_menu == 'descareges':
                    user_input_username = show_descareges(DESCAREGES, user_input_username)
                elif user_input_menu == 'musica':
                    user_input_username = musica(MUSICA_CONTENT, user_input_username)
                elif user_input_menu == 'video':
                    user_input_username = video(VIDEO_CONTENT, user_input_username)
                elif user_input_menu == 'imatges':
                    user_input_username = show_imatges(IMATGES, user_input_username)
                elif user_input_menu == 'documents':
                    user_input_username = docs(DOCUMENTS, user_input_username)
                elif user_input_menu == 'calculadora MRUA':
                    print(sorted(CALCULADORA_MRUA))
                    opcio = input('Tria la incògnita que vols trobar: ')
                    resultat = None
                    resultat2 = None
                    resultat3 = None
                    resultat4 = None
                    resultat5 = None
                    if opcio == 'a':
                        resultat = MRUA_a()
                    elif opcio == 'Av':
                        resultat2 = MRUA_av()
                    elif opcio == 'At':
                        resultat3 = MRUA_at()
                    elif opcio == 'Vf':
                        resultat4 = MRUA_vf()
                    elif opcio == 'Xf':
                        resultat5 = MRUA_xf()
                    else:
                        print('Opció no vàlida per a la calculadora MRUA.')
                    arrodonir = input('Vols arrodonir el resultat? (si/no): ')
                    MRUA_arrondonir(opcio, resultat, resultat2, resultat3, resultat4, resultat5, arrodonir)
                    resposta = input('Vols canviar les unitats? (si/no): ')
                    if resposta.lower() == 'si':
                        MRUA_canviUnits()
                    else:
                        print('No es farà el canvi d\'unitats.')
                elif user_input_menu == 'configuracio':
                    user_input_username = Config(USERS, user_input_username)
                elif user_input_menu == 'viatjar':
                    print('https://landbot.online/v3/H-2775206-6P3AOFD16UGVM00S/index.html')
                elif user_input_menu == 'exit':
                    print('Apagant programa.')
                    for _ in range(2):
                        time.sleep(0.1)
                        print('Apagant programa..')
                    print('Programa apagat.')
                    break
                else:
                    print('No tens permisos per veure aquest document')
            else:
                print('Opció no vàlida.')
    else:
        print('Usuari o contrasenya incorrectes')
