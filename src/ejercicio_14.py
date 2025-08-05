import random
numero_secreto = random.randint(1, 10)
intento = int(input("Adivina el número (1-10): "))
while intento != numero_secreto:
    intento = int(input("Incorrecto. Intenta de nuevo: "))
print("¡Felicidades! Adivinaste el número.")
