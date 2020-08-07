/**
Nombre: funciones.c
Objetivo: Muestra las funciones en ansi c
Autor: Antonio Rodríguez
Fecha: 06/08/2020
*/

#include <stdio.h>
#include <string.h>
/**
funcion para regresar un mensaje
*/

char* getMessage()
{
    char msg[]="Hola Mundo"; 
    return "Hola Mundo";
}

int suma(int n1, int n2)
{
    return n1+n2;
}

int resta(int n1, int n2)
{
    return n1-n2;
}

int main()
{
    printf("El mensaje es: %s\n", getMessage());
    printf("La suma es: %d\n", suma(2,5));
    printf("La resta es: %d\n", resta(22,-5));
    return 0;
}