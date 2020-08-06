#Tarea hacer la ventana de captura de atributos de objetos con tkinter

"""
Nombre: MainCilindro.py
Objetivo: Muestra como trabajar con ventanas gui en python y tkinter
Autor: Antonio Rodriguez
Fecha: 30/07/2020
"""
from Circunferencia import Circunferencia
from tkinter import *
from tkinter import ttk

def sendToServer():
    print()

def main():
    win = Tk()
    win.geometry("800x800")
    win.title("Objetos con tkinter")

    label = ttk.Label(win, text="Hola, Bienvenido").pack(side=TOP)
    txtCampo = ttk.Entry(win).pack(side=TOP)

    ttk.Button(win, text="Enviar", command=sendToServer).pack(side=BOTTOM)
    ttk.Button(win, text="Salir", command=quit).pack(side=BOTTOM)

    win.mainloop()

if __name__ == "__main__":
    main()