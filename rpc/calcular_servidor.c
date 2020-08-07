/**
 * Nombre: calcular_servidor.c
 * Objetivo:
 * Autor: Antonio Rodríguez
 * Fecha: 07/08/2020
*/


# include "calcular.h"

int * sumar_1_svc(int a, int b, struct svc_req *rqstp)
{
static int r;
r = a + b;
return(&r);
}

int * restar_1_svc(int a, int b, struct svc_req *rqstp)
{
static int r;
r = a - b;
return(&r);
}

int * multiplicar_1_svc(int a, int b, struct svc_req *rqstp)
{
    static int r;
    r = a * b;
    return(&r);
}

float * dividir_1_svc(int a, int b, struct svc_req *rqstp)
{
    static float r;
    r = a / b;
    return(&r);
}