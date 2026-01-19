import time
users = {
            1: {"name": "Maria Lopez", 
                "password": "abcd",
                "saldo": 1000                
                },
            2: {"name": "Pere Martinez", 
                "password": "pass123",
                "saldo": 500},
            3: {"name": "Anna Garcia", 
                "password": "qwerty",
                "saldo": 750}
}
while True:
    user_input = int(input("1.iniciar sessió \n2.Tancar el caixer \nTria una opció: "))
   

    if user_input == 2:
        print("Tancant el caixer...")
        time.sleep(0.52)
        print("Caixer tancat.")
        break
    
    else:
        user_input_NC = input("Introdueix el nom i el cognom: ")
        user_input_password = input("Introdueix la contrasenya: ")
        user_input_password2 = input("Introdueix un altre cop la contrasenya: ")

        if user_input_NC not in [user["name"] for user in users.values()]:
            print("Usuari no registrat.")
            usuarisacio = input("Vols registrar-te? (sí/no): ")
            if usuarisacio.lower() == "si" or usuarisacio.lower() == "sí":
                length = len(users) + 1
                new_id = users[length] = {"name": user_input_NC, "password": user_input_password, "saldo": 0}

            elif usuarisacio.lower() == "no":
                print("Fins aviat!")
                break

        elif user_input_password != user_input_password2 or user_input_password == "" or user_input_password2 == "" or user_input_password not in [users[user]["password"] for user in users]:
            print("Contrasenya incorrecta.")
        
        else:
            for user_id in users:
                if users[user_id]["name"] == user_input_NC and users[user_id]["password"] == user_input_password:
                    current_user_id = user_id
                    continue
            
            print("Iniciant sessió...")
            time.sleep(2)
            print(f"Sessió iniciada. Benvingut/da, {user_input_NC}!")
            print("1. Dipositar diners\n2. Extreure diners\n3. Modificar contrasenya\n4. Transferecnies\n5.Sortir")
            user_input_action = int(input("Tria una opció: "))
            if user_input_action == 1:
                user_input_deposit = float(input("Introdueix l'import a dipositar: "))
                users[current_user_id]["saldo"] += user_input_deposit
                print(f"S'han dipositat {user_input_deposit}€. Nou saldo: {users[current_user_id]['saldo']}€")
            elif user_input_action == 2:
                user_input_extreure = float(input("Introdueix l'import a extreure: "))
                if user_input_extreure > users[current_user_id]["saldo"]:
                    print("Fons insuficients.")
                else:
                    users[current_user_id]["saldo"] -= user_input_extreure
                    print(f"S'han extret {user_input_extreure}€. Nou saldo: {users[current_user_id]['saldo']}€")
            
            elif user_input_action == 3:
                user_input_password_antiga = input("Introdueix la contrasenya: ")
                user_input_password_antiga2 = input("Introdueix un altre cop la contrasenya: ")
                user_input_new_password = input("Introdueix la nova contrasenya: ")
                user_input_new_password2 = input("Introdueix un altre cop la contrasenya: ")
                if user_input_password_antiga == user_input_password_antiga2 and user_input_new_password == user_input_new_password2 and user_input_password_antiga == users[current_user_id]["password"]:
                    users[current_user_id]["password"] = user_input_new_password
                    print("Contrasenya modificada correctament.")
            elif user_input_action == 5:
                print("Tancant sessió...")
                time.sleep(2)
                print("Sessió tancada.")
                break
            elif user_input_action == 4:
                user_input_trans = input("Aqui vols fer una transferencia:")
                if user_input_trans not in [users[user]["name"] for user in users]:
                    print("Usuari no existeix")
                else:
                    user_input_trans_import = input("Quants diners vols enviar:")
                    if [users[user_input_trans]["saldo"]] < user_input_trans_import or [users[current_user_id]["saldo"]] < user_input_trans_import:
                        print("saldo insuficinet")
                    else:
                        trasn = current_user_id - user_input_trans_import
                        trans2 = user_input_trans + user_input_trans_import
                        print([users[current_user_id]["saldo"]])
                        print([users[user_input_trans]["saldo"]])

