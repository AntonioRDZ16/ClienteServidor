"""
Nombre: MainPunto.py
Objetivo: muestra como trabajar con multiples archivos en python
Autor: Antonio Rodrìguez
Fecha: 30/07/2020
"""
#Incluir el archivo de la clase
from Punto import Punto 

#Creamos objetos dentro del mismo archivo
PuntoA = Punto(0,0)
#Invocamos metodos GET
print("El valor de la coordenada X= ",PuntoA.getX())
print("El valor de la coordenada Y= ",PuntoA.getY())
#Invocamos metodos set
PuntoA.setX(23)
PuntoA.setY(12)
#Imprimimos los valores de los atributos del objeto puntoB
print(PuntoA.toString())




#Creamos objetos dentro del mismo archivo
PuntoB = Punto(-10,-20)
#Invocamos metodos GET
print("El valor de la coordenada X= ",PuntoB.getX())
print("El valor de la coordenada Y= ",PuntoB.getY())
#Invocamos metodos set
PuntoB.setX(10)
PuntoB.setY(20)
#Imprimimos los valores de los atributos del objeto puntoA
print(PuntoB.toString())
