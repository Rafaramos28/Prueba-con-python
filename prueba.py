import random
print("Hola mundo")
print("\nEsto es una prueba")

#vamos a crear una lista con 10 números al azar
numeros = [0 for x in range (1, 11)]

for i in range (len(numeros)):
    numeros[i] = random.randint(1, 100)

print("\nlista con 10 numeros aleatorios")
print(numeros)

