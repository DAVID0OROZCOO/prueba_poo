def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "") 
    return cadena == cadena[::-1]

texto = input("Ingrese una cadena de texto: ")
if es_palindromo(texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")