
def encontrar_extremos(lista):
    return min(lista), max(lista)

numeros = [9, 2, 3, 4, 8]
minimo, maximo = encontrar_extremos(numeros)
print("El número más pequeño es:", minimo)
print("El número más grande es:", maximo)