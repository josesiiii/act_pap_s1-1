suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Ingresa un número (0 para terminar): "))
print("Suma total:", suma)