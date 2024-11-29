"""
usamos paréntesis


"""
myFruitList = ["Pera", "Banana", "Mango"]

print(type(myFruitList))

print(myFruitList[2])
print(myFruitList[1])
print(myFruitList[0])


## strame o imprima el primer elemento 
#Métodos de las listas
## . append() agrega un elemento a la lista
#lo va agregar al final 
# añadir tomate
myFruitList[2] = "Melon"

print(myFruitList)

myFruitList.append("Tomate")

print(myFruitList[3])
print(myFruitList)

myFruitList.pop()
print(myFruitList)

"""
Tupla 
Es una colección inmutable ordenada de elementos 
se usan parentesis redondos "()" y  comas "," para separar elementos
"""

myFinalAnswerTuple = ( "manzana" , "banana" , "piña" )
print(myFinalAnswerTuple)

"""
Dicciónario de elementos clave valor

clave : entero o string

valor : cualquier tipo dato

Diccionarios son mutables

se busca por la clave 

"""
FondosRestart ={
    "Mario" : "Amarillo",
    "Luna" : "Naranja",
    "jorge" : "Negro",
    "Matias" : "Blanco"
}


print(type(FondosRestart))
print(FondosRestart)
print(FondosRestart["Matias"])
print(FondosRestart["Mario"])

