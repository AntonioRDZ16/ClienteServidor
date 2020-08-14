#Clase que muestra la herencia en ruby

load "punto.rb"

class circunferencia < Punto
    def initialize(vRadio)
        @radio = vRadio
    end
    
    def getRadio()
        return @radio
    end

    def setRadio(vRadio)
        @radio = vRadio
    end
    #Escribir un método que calcule el área de la circunferencia
    def area(vRadio)
        return Math::PI*(vRadio*2)
    end


end

cir = circunferencia.new(3)

puts "El radio es : #{cir.getRadio}"
#Invocamos métodos de la clase Punto
cir.setX(10)
cir.setY(10)
puts "Las coordenadas son: #{cir.getX}, #{cir.getY}"
puts "El area de la circunferencia es: #{cir.getArea(cir.getRadio)}"