# Módulo principal de funciones 

load "funciones.rb"

ciclo = "S"
while (ciclo =="S" or ciclo=="s")

print "--- Operaciones Básicas con Ruy ---","\n"
print "Introduce el primer número: ","\n"
n1 = Integer(gets.chomp)
print "Introduce el segundo número: ","\n"
n2 = Integer(gets.chomp)

print mensaje()+"\n"
print "La suma es :", suma(n1, n2),"\n"
print "La resta es :", resta(n1, n2),"\n"
print "La multiplicación es :", multiplicacion(n1, n2),"\n"
print "La división es :", division(n1, n2),"\n"
print compara(n1, n2),"\n"
print cuenta(n1, n2),"\n"

puts "El área de la circunferencia es: #{getArea(3)}"

puts "Desea realizar otra operación (S/N)?"
ciclo = gets.chomp

end

puts "*** Fin del programa"