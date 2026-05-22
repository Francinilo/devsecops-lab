print("Sistema DevSecOps iniciado")

usuario = "admin"

if usuario == "admin":
    print("Acesso permitido")

import math

numero = float(input("Digite um numero para calcular a raiz quadrada: "))

if numero < 0:
    print("Nao existe raiz quadrada real para numero negativo.")
else:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} e {raiz}")