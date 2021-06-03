import random
print("Bienvenido 2.0")
print("\nEsto es una prueba")

#vamos a crear una lista con 10 números al azar
numeros = [0 for x in range (1, 11)]
for i in range (len(numeros)):
    numeros[i] = random.randint(1, 100)

print("\nlista con 10 numeros aleatorios")
print(numeros)

#sumatoria
suma = 0
for i in range(len(numeros)):
    suma += numeros[i]
print("\nsumatoria")
print(suma)

#promedio
promedio = suma/len(numeros)
print("\nEl promedio es",promedio)
