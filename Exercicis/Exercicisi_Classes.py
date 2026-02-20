import math
#------------------------------------------1--------------------------------
class Punt2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punt2D({self.x}, {self.y})"
    
    def dist_origen(self):
        return (self.x**2 + self.y**2)**0.5
    
    def dist_punt(self, x_altre, y_altre):
        self.x_altre = x_altre
        self.y_altre = y_altre
        return ((self.x - self.x_altre)**2 + (self.y - self.y_altre)**2)**0.5
    
    def mou(self, dx, dy):
        self.x += dx
        self.y += dy
        return (self.x, self.y)
    
Punt2D_1 = Punt2D(3, 4)
print(Punt2D_1)
print("Distancia de l'orgien: ", Punt2D_1.dist_origen())
print("Distancia a un  altre punt (6,9): ", Punt2D_1.dist_punt(6, 9))
print("Moure el punt en (2,3): ", Punt2D_1.mou(2, 3))
t = Punt2D_1.__str__()
print(t)

#------------------------------------------2--------------------------------
Users = {
    1: {"Nom": "User1", "Edat": 25, "Email": "user1@example.com", "saldo": 1000.0},
    2: {"Nom": "User2", "Edat": 30, "Email": "user2@example.com", "saldo": 1500.0},
    3: {"Nom": "User3", "Edat": 35, "Email": "user3@example.com", "saldo": 2000.0}
}
class Compte:
    def __init__(self, titular: str):
        if not isinstance(titular, str):
            raise TypeError("El tipus de dades no és correcte")
        self.titular = titular
        for uid, u in Users.items():
            if u["Nom"] == titular:
                self.user_id = uid
                self.saldo = u["saldo"]
                break 
            
    def ingressar(self, Q):
        self.saldo += Q
        Users[self.user_id]["saldo"] = self.saldo
        return self.saldo
    
    def retirar(self, Ret):
        if Ret > self.saldo:
            raise ValueError("Fons insuficients")
        else:
            self.saldo -= Ret
            Users[self.user_id]["saldo"] = self.saldo
            return self.saldo

    def Transferencia(self, Titular_2, Q_2):
        if Q_2 > self.saldo:
            raise ValueError("Fons insuficients")
        else:
            self.saldo -= Q_2
            Users[self.user_id]["saldo"] -= Q_2
            for uid, u in Users.items():
                if u["Nom"] == Titular_2:
                    Users[uid]["saldo"] += Q_2
                    break

Persona = Compte("User1")
print("Saldo inicial: ", Persona.saldo)
print("Saldo després d'ingressar 500: ", Persona.ingressar(20))
print("Saldo després de retirar 300: ", Persona.retirar(11))
Persona.Transferencia("User2", 200)
print("Saldo després de transferir 200 a User2: ", Persona.saldo)


#------------------------------------------3--------------------------------
class Rectngle:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura)
    
    def perimetre(self):
        return 2*(self.base + self.altura)
    @property
    def diagonal(self):
        return math.sqrt(self.base**2 + self.altura**2)
    
R = Rectngle(20, 15)
print(R.area())
print(R.perimetre())
print(R.diagonal)

#------------------------------------------5--------------------------------
class Veichle:
    def __init__(self, x, y, vx, vy, ax, ay):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
    
    def moure(self, t):
        xf = self.x + (self.vx*t)+(0.5*self.ax*(t**2))
        yf = self.y + (self.vy*t) + (0.5*self.ay*(t**2))
        P = (xf,yf)
        print("Posició final: ", P)
        return xf, yf
    
    def estat(self, t):
        vxf = self.vx + self.ax*t
        vyf = self.vy + self.ay*t
        return (vxf, vyf)
    
    
class Cotxe(Veichle):
    def __init__(self, x, y, vx, vy, ax, ay, capacitat_combustible, combustible, consum_combustible):
        super().__init__(x, y, vx, vy, ax, ay)
        self.capacitat_combustible = capacitat_combustible
        self.combustible = combustible
        self.consum_combustible = consum_combustible

    def repostar(self, litres):
        if self.combustible + litres > self.capacitat_combustible:
            raise ValueError("No es pot repostar més del que la capacitat permet")
        else:
            self.combustible += litres
    
    def comb_gastat(self):
        posicio_inical = [self.x, self.y]
        xf, yf = self.moure(3)
        posicio_final = [xf, yf]
        distancia = math.sqrt((posicio_final[0] - posicio_inical[0])**2 + (posicio_final[1] - posicio_inical[1])**2)
        comb_gastat = distancia * self.consum_combustible
        if comb_gastat > self.combustible:
            raise ValueError("No hi ha suficient combustible per moure's durant 3 segons")
        else:
            self.combustible -= comb_gastat
            return comb_gastat, self.combustible
    
Cotxe_1 = Cotxe(7, 10, 10, 10, 2, 2, 50, 150, 2)
comb_gastat, comb_restant = Cotxe_1.comb_gastat()
print(f"{round(comb_gastat, 2)} litres de combustible gastats després de moure's durant 3 segons")
print(f"Combustible restant: {round(comb_restant, 2)} litres")
