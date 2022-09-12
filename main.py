from CuentaBancaria import CuentaBancaria
from Usuarios import Usuarios

""" cuenta1 = CuentaBancaria(0.01, 0)
cuenta2 = CuentaBancaria(0.01, 0)

cuenta1.depositar(300).depositar(120).depositar(31).retiro(76).generar_interes().mostrar_info_cuenta()


cuenta2.depositar(287).depositar(95).retiro(19).retiro(30).retiro(34).retiro(10).generar_interes().mostrar_info_cuenta()


CuentaBancaria.imprimir_instancias() """

elena =  Usuarios("Elena", "De Troya")

elena.depositar(200)
elena.mostrar_balance_usuario()

elena.retiro(56)
elena.mostrar_balance_usuario()
