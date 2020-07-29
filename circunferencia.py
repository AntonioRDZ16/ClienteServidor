"""
Nombre: circunferencia.py
Objetivo: Permite calcular el area de una circunferencia
Autor: Antonio Rodriguez
Fecha: 28/07/2020
"""
#Importamos libreria Math
import math

#Funcion para calcular area
def calcularArea(valorRadio):
	return math.pi*math.pow(valorRadio,2)

#Modulo principal
def main():
	ciclo = 'S' 
	while ciclo == 'S' or ciclo == 's':

		print ("=== Programa para calcular area de una circunferencia ===")
		vradio = int(input("Dijita el valor del radio: "))
		print ("\n")
		print ("El area de la circunferencia con radio igual  a: {}, es: {}".format(vradio, calcularArea(vradio)))
		ciclo = input("¿Otro calculo? (S/n)")
	else:
		print ("** Fin del programa **")



if __name__ == "__main__":
	main()
