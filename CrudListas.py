"""
Nombre: CrudListas.py
Objetivo: Implementa las funciones CRUD en una lista en python
Autor: Antonio Rodríguez
Fecha: 04/08/2020
"""
#Declaramos una lista como variable global
lista = []

#Funcion para agregar elementos a la lista
def addElement():
    e = input("Ingresa el elemento: ")
    lista.append(e)
    print("** Elemento agregado **")
    return

#Fucnion para buscar elementos en la lista
def getElement():
    return

#Funcion para modificiar elementos en la lista
def modifyElement():
    return

#Funcion para eliminar un elemento de la lista
def delElement():
    e = input("Ingresa lo que quieres eliminar de la lista")
    lista.remove(e)
    return

#Imprimir los elementos de la lista
def showElement():
    for i in lista:
        print("Elementos de la lista", i)

def dashboard():
    print("=== Operaciones GRUD con listas ===")
    print("1.- Agregar elementos")
    print("2.- Buscar elementos")
    print("3.- Modificar elementos")
    print("4.- Eliminar elementos")
    print("5.- Imprimir todos los elementos")
    print("6.- Salir")
    return



def main():
    ciclo = 'S'
    while ciclo == 'S' or ciclo == 's':
        dashboard()
        ciclo = int(input("Selecciona una opción entre 1 y 6: "))
        if ciclo == 1:
            #invocar función para agregar elementos
            addElement()
        elif ciclo == 2:
            getElement()
        elif ciclo == 3:
            modifyElement()
        elif ciclo == 4:
            delElement()
        elif ciclo == 5:
            showElement()
        elif ciclo == 6:
            print("Saliendo del programa...")
            quit()
    else:
        print("**Fin de programa **")



if __name__ == "__main__":
    main()