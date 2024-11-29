
"""
Ejercicio: Simulación de Inventario de una Librería
Objetivo: Este ejercicio está diseñado para mejorar tus habilidades en el manejo de diccionarios en Python, así como tu capacidad para implementar lógica compleja en la manipulación de estructuras de datos. Utilizarás un diccionario para simular y gestionar el inventario de una librería.
Descripción del ejercicio:
Desarrolla un programa en Python que permita gestionar el inventario de libros en una librería utilizando un diccionario. El programa debe permitir la adición, actualización, eliminación y consulta de libros, así como el seguimiento de la cantidad de cada título disponible.
Especificaciones del problema:
Estructura del Inventario:
Cada libro en el inventario debe ser representado como una clave en el diccionario, donde la clave es el título del libro.
El valor asociado a cada clave (título del libro) será otro diccionario que contenga al menos la cantidad de copias disponibles y el precio del libro.
Funcionalidades Requeridas:
Agregar un libro nuevo al inventario: El usuario debe poder ingresar el título del libro, el precio y la cantidad inicial de copias.
Actualizar la información de un libro: El usuario debe poder modificar tanto la cantidad de copias como el precio de cualquier libro.
Eliminar un libro del inventario: Si un libro ya no está disponible o ha sido discontinuado, el usuario debe poder eliminarlo del inventario.
Consultar la información de un libro: El usuario debe poder consultar la cantidad disponible y el precio de cualquier libro ingresando su título.
Listar el inventario completo: Debe haber una opción para mostrar todos los libros disponibles en el inventario, junto con su precio y cantidad.


Que se debe hacer ?
me piden crear un programa que gestione libros 
agregar un libro
actualizar informacion de un libro
eliminar un libro
consultar la informacion de un libro 
listar el inventario completo
"""

print("¿Qué quieres hacer? Selecciona una opción:")
print("1. Agregar un libro")
print("2. Actualizar libro")
print("3. eliminar libro")
print("4. Consultar libro")
print("5. Ver inventario completo")

opcion = input("Introduce el número de tu elección: ")

libros = {
    1: {"titulo": "Cien años de soledad", "precio": 15000, "cantidad": 5},
    2: {"titulo": "1984", "precio": 12000, "cantidad": 3},
    3: {"titulo": "El principito", "precio": 8000, "cantidad": 10},
    4: {"titulo": "Don Quijote de la Mancha", "precio": 20000, "cantidad": 2},
    5: {"titulo": "Orgullo y prejuicio", "precio": 14000, "cantidad": 4},
    6: {"titulo": "El señor de los anillos", "precio": 25000, "cantidad": 7},
    7: {"titulo": "Harry Potter y la piedra filosofal", "precio": 18000, "cantidad": 6},
    8: {"titulo": "La Odisea", "precio": 13000, "cantidad": 8},
    9: {"titulo": "Crimen y castigo", "precio": 16000, "cantidad": 3},
    10: {"titulo": "El Alquimista", "precio": 11000, "cantidad": 9},}
    
    
    for id_libro, datos in libros.items():
    print(f"Libro ID: {id_libro}")
    print(f"  Título: {datos['titulo']}")
    print(f"  Precio: ${datos['precio']}")
    print(f"  Cantidad: {datos['cantidad']}")
    print("-" * 30)
    
    