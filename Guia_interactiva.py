"""Ejercicio 1: Suma de números del 1 al 10
Usa un ciclo for para calcular la suma de los números del 1 al 10.
"""

suma = 0

for i in range(1,11):
    suma +=i 
print(suma)


"""
 Ejercicio 2: Tablas de multiplicar
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).

 """
 
 
for i in range(1, 11):
     print(5 * i)
     
for i in range(1, 11):  # Del 1 al 10
    print(f"5 x {i} = {5 * i}")
    
    
"""
Ejercicio 3: Contar vocales en una palabra
Pide al usuario una palabra y cuenta cuántas vocales tiene.
"""

palabra = input("Escribe una palabra: ").lower()
vocales = "aeiou"
contador = 0
for letra in palabra:
    if letra in vocales:  # Comprueba si es vocal
        contador += 1
print(f"Vocales: {contador}")