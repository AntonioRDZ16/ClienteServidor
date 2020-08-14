"""
Nombre: funciones.py
Objetivo: Muestra la operaciòn de las funciones en python
Autor: Antonio Rodriguez
Fecha: 27/07/2020
"""

def mensaje():
	print ("Hola desde mensaje")



def regresamensaje():
	return "Saludo desde el regresa mensaje"


def printmensaje(msg):
	print (msg)



def suma(n1, n2):
	return n1+n2


def resta(n1, n2):
	return n1-n2


def mult(n1, n2):
	return n1*n2


def div(n1, n2):
	if (n2 != 0):
		return n1/n2
	else:
		print ("Error en la division, no es posible dividir entre cero")

def compara(n1, n2):
	if n1>n2:
		print ("El mayor es n1: ", n1, " ", n2)
	elif n2>n1:
		print ("El mayor es n2: {},{}".format(n2,n1))
	else:
		print ("Los numeros son iguales: {},{}".format(n1,n2))


#Funcion para mostrar operacion FOR
def cuenta(n1, n2):
	if(n2>n1):
		for i in range (n1,n2+1):
			print ("Valor de i: {}".format(i))
	elif(n1>n2):
		for i in range (n1,n2-1, -1):
			print ("valor de i: {}".format(i))
	else:
		print ("Los numeros son iguales, no puedo contar: {},{}".format(n1,n2))
def main():

	ciclo = 'S'
	while ciclo == 'S' or ciclo =='s':
		#invocamos funcion mensaje
		mensaje()
		#invocamos funcion regresamensaje
		print (regresamensaje())
		#invocamos funcion printmensaje
		printmensaje("Hola te saludo...")
		
		#leemos los datos por teclado
		a = int(input("Ingresa el primer numero entero: "))
		b = int(input("Ingresa el segundo numero entero: "))
		#Invocamos la funcion suma
		print ("La suma es: ", suma(a,b))
		print ("=========================")
		print ("La resta es: ", resta(a,b))
		print ("=========================")
		print ("La multiplicacion es: ", mult(a,b))
		print ("=========================")
		print ("La division es: ", div(a,b))
		print ("=========================")

		compara(a,b)
		cuenta(a,b)
		#preguntamos por otra operacion
		ciclo = input("¿Desea otra operacion (s/n)?")
	else:
		print ("*** Fin de programa")

if __name__ == "__main__":
	main()
