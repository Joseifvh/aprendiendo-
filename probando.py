import unicodedata

def normalizar_titulo(titulo):
    """Convierte un título a minúsculas y sin acentos para comparaciones."""
    return ''.join(c for c in unicodedata.normalize('NFD', titulo.lower()) if unicodedata.category(c) != 'Mn')

def buscar_libro(inventario, titulo_parcial):
    """Busca libros que coincidan parcialmente con el título proporcionado."""
    titulo_normalizado = normalizar_titulo(titulo_parcial)
    return {titulo: datos for titulo, datos in inventario.items() if titulo_normalizado in normalizar_titulo(titulo)}

def mostrar_menu():
    print("\n1. Agregar libro")
    print("2. Actualizar libro")
    print("3. Eliminar libro")
    print("4. Consultar libro")
    print("5. Listar inventario")
    print("6. Salir")

def agregar_libro(inventario):
    titulo = input("Título del libro: ")
    if titulo in inventario:
        print("El libro ya existe.")
        return
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    inventario[titulo] = {"precio": precio, "cantidad": cantidad}
    print(f"Libro '{titulo}' agregado.")

def actualizar_libro(inventario):
    titulo = input("Título del libro a actualizar: ")
    libros = buscar_libro(inventario, titulo)
    if not libros:
        print("Libro no encontrado.")
        return
    if len(libros) == 1:
        titulo_encontrado = list(libros.keys())[0]
    else:
        print("Libros encontrados:")
        for i, libro in enumerate(libros.keys(), 1):
            print(f"{i}. {libro}")
        opcion = int(input("Seleccione un libro: "))
        titulo_encontrado = list(libros.keys())[opcion - 1]
    print(f"Actualizar {titulo_encontrado}.")
    nueva_cantidad = int(input("Nueva cantidad: "))
    nuevo_precio = float(input("Nuevo precio: "))
    inventario[titulo_encontrado] = {"precio": nuevo_precio, "cantidad": nueva_cantidad}

def eliminar_libro(inventario):
    titulo = input("Título del libro a eliminar: ")
    libros = buscar_libro(inventario, titulo)
    if not libros:
        print("Libro no encontrado.")
        return
    if len(libros) == 1:
        titulo_encontrado = list(libros.keys())[0]
    else:
        print("Libros encontrados:")
        for i, libro in enumerate(libros.keys(), 1):
            print(f"{i}. {libro}")
        opcion = int(input("Seleccione un libro: "))
        titulo_encontrado = list(libros.keys())[opcion - 1]
    del inventario[titulo_encontrado]
    print(f"Libro '{titulo_encontrado}' eliminado.")

def consultar_libro(inventario):
    titulo = input("Título del libro a consultar: ")
    libros = buscar_libro(inventario, titulo)
    if not libros:
        print("Libro no encontrado.")
        return
    for titulo, datos in libros.items():
        print(f"'{titulo}': Precio: {datos['precio']}, Cantidad: {datos['cantidad']}")

def listar_inventario(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    for titulo, datos in inventario.items():
        print(f"'{titulo}': Precio: {datos['precio']}, Cantidad: {datos['cantidad']}")

def main():
    inventario = {
        "Cien Años de Soledad": {"precio": 20.0, "cantidad": 5},
        "El Amor en los Tiempos del Cólera": {"precio": 18.5, "cantidad": 3},
        "Don Quijote de la Mancha": {"precio": 25.0, "cantidad": 10},
        "1984": {"precio": 12.0, "cantidad": 4},
        "Fahrenheit 451": {"precio": 14.0, "cantidad": 6}
    }
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_libro(inventario)
        elif opcion == "2":
            actualizar_libro(inventario)
        elif opcion == "3":
            eliminar_libro(inventario)
        elif opcion == "4":
            consultar_libro(inventario)
        elif opcion == "5":
            listar_inventario(inventario)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
