#include "calcular.h"
int main (int argc, char **argv)
{
char *host;
CLIENT *sv;

//variables para recuperar los resultados recibidos del servidor
int *resS, *resR, *resM; //variables para recibir la suma, resta y multiplicación
float *resD, *areaC;             //Para la división y área
if (argc!=2)
printf("Uso: %s <host>\n", argv[0]);
else
{
host = argv[1];
sv = clnt_create(host, CALCULAR, UNO, "tcp");
//Invocamos los servicios del servidor, las cuatro operaciones básicas
if (sv != NULL)
{
//suma
resS = sumar_1(5, 2, sv);
//resta
resR = restar_1(10, 20, sv);
//multiplicación
resM = multiplicar_1(5, 5, sv);
//división
resD = dividir_1(10, -2, sv);
//invocar función area de circunferencia
areaC = areacircunferencia_1(2.33, sv);


if (resS != NULL)
{
//imprimimos resultados
printf("El servidor enví estos datos...\n");
printf("5 + 2 = %d\n", *resS);
printf("10 - 20 = %d\n", *resR);
printf("5 * 5 = %d\n", *resM);
printf("10 / -2 = %f\n", *resD);
printf("El área de la circunferencia es con radio igual a 2.33 es: %f\n", *areaC);
}
else
{
clnt_perror(sv, "error en RPC");
}
clnt_destroy(sv);
}
else
{
clnt_pcreateerror(host);
}
}
return(0);
}