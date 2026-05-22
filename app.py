print("Sistema DevSecOps iniciado")

usuario = "admin"

if usuario == "admin":
    print("Acesso permitido")

import math

numero = float(input("Digite um numero para calcular a raiz quadrada: "))
print(f"{numero} e maior que 10? {numero > 10}")
print(f"{numero} e menor que 10? {numero < 10}")

if numero < 0:
    print("Nao existe raiz quadrada real para numero negativo.")
else:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} e {raiz}")