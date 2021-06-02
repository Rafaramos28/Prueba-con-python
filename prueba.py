print("Hola mundo")
print("\nEsto es una prueba")

#vamos a crear una lista con los números del 1 al 10
numeros = [0 for x in range (1, 11)]
for i in range (len(numeros)):
    numeros[i] = i+1
print("\nNumeros del 1 al 10")
print(numeros)

#sumatoria
suma = 0
for i in range(len(numeros)):
    suma += numeros[i]
print("\nsumatoria")
print(suma)
