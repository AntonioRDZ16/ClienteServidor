"""
Nombre: listas.py
Objetivo: Muestra la función de las listas en python
Autor: Antonio Rodríguez
Fecha: 04/08/2020
"""



def main():
    #una lista es una estructura de datos en python
    #la ventaja de las listas acpetan datos de tipos distintos
    #Creamos una lista
    lista = [1, 23.01, False, "Hola lista", 'A', [-1, -5, "Hola", 0.0], -12, 'A']
    #Lista vacia
    listaVacia = []
    #accesando elementos de la lista
    print("---------------------------------------")
    for elemento in lista:
        print("El elemento de la lista es: ", elemento)

    for i in listaVacia:
        print("El elemento de la lista es: ", i)

    #imprimir un elemento de la lista
    print("Elemento en la posicion 3: ", lista[3])
    print("Elemento en la posicion -5: ", lista[-5])
    print(lista[-2])
    print(lista[5])
    #leer un elemento de la lista interna
    print(lista[5][-2])
    #metodos de las listas
    
    #Append - Agregas un elemento al final de la lista
    lista.append("Tu puedes antonio")
    print("---------------------------------------")
    for elemento in lista:
        print("El elemento de la lista es: ", elemento)



    #Count - Cuenta las veces que se repite un elemento de la lista 
    print("el elemento se repite: ", lista.count('A'))


    #Index - Imprime el indice de un elemento de la lista
    print("La posición de False es: ", lista.index(False))

    #Remove - Elimina elementos de la lista
    lista.remove("Hola lista")
    print("---------------------------------------")
    for elemento in lista:
        print("El elemento de la lista es: ", elemento)


if __name__ == "__main__":
    main()
    