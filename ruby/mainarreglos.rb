#Cargamos el archivo de la clase arreglo
load "arreglo.rb"

#Creamos un objeto de la clase
vec = Arreglo.new()

#Reporte de elementos del arreglo
vec.printAll()

#Insertar un elemento
vec.insert("First")
vec.insert(12)
vec.insert(false)
vec.insert("C")
vec.insert(12.45)
vec.printAll()


vec.cambiar("peludo", true)

vec.printAll()

