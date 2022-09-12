from CuentaBancaria import CuentaBancaria

class Usuarios:
    lista_cuentas = []

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.cuenta = CuentaBancaria(tasa_interes=0.02, balance=0)
        Usuarios.lista_cuentas.append(self)

    def depositar(self, amount):
        self.cuenta.depositar(amount)


    def retiro(self, amount):
        self.cuenta.retiro(amount)

    
    def mostrar_balance_usuario(self):
        print(f"{self.name}, su balance de cuenta es: {self.cuenta.balance}")

    def transferir_dinero(self, amount, name_user):
        self.cuenta -= amount
        name_user.cuenta += amount