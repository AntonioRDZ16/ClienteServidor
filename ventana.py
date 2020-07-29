"""
Nombre: ventana.py
Objetivo: Muestra como trabajar con ventanas gui en python y tkinter
Autor: Antonio Rodriguez
Fecha: 29/07/2020
"""

#Importar las librerias de tkinter
from tkinter import *
from tkinter import ttk


#Funcion  para  enviar datos al servidor echo
def sendToServer():
	print("Si funciona")


#Definimos funcion main
def main():
	#Creamos la ventana contenedora
	win = Tk()
	#Modificamos parametros de la ventana win
	win.geometry("400x400")
	win.title("Mi primer ventana en Python Tkinter")
	
	#Creamos etiqueta
	label = ttk.Label(win, text="Hello, Tkinter").pack(side=TOP)
	txtCampo = ttk.Entry(win).pack(side=TOP)

	#Creamos un boton para enviar el contenido de la propiedad text del Entry al servidor
	ttk.Button(win, text="Enviar", command=sendToServer).pack(side=BOTTOM)


	#Creamos un boton y lo colocamos en al ventana
	ttk.Button(win, text="Salir", command=quit).pack(side=BOTTOM)

	#Hacemos un ciclo para dibujar y esperar eventos
	win.mainloop()


#Para funcion main
if __name__ == "__main__":
	main()
