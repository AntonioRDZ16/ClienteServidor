#Clase para el manejo de arreglos en ruby

class Arreglo

    #Método constructor
    def initialize()
        @vector = []
    end

    #Insertar elemento en el arreglo
    def insert(elem)
        @vector.push(elem)
    end

    #Buscar un elemento dentro del arreglo
    def buscar(elem)
        @vector.each_with_index do |elemento, index|
            if elemento == elem
                puts "El elemento buscado es:[#{index}]=#{elemento}"
                return index

            #Verificamos que estamos al final del arreglo y no encontramos el elemento
            elsif (elemento != elem)  && (index+1 == @vector.length)
                puts "El elemento no existe #{elem}"
                return -1
            end
        end
    end


    #Borra elemento
    def borrar(elem)
        puntero = buscar(elem)
        if (puntero >= 0)
            @vector.delete_at(puntero)
            puts "Elemento borrado: #{elem}"
        else
            puts "nada se borro: [#{elem}]"
        end
    end



    #cambiar elemento
    def cambiar(elem, elem_new)
        puntero = buscar(elem)
        if (puntero >= 0)
            #Elemento existe y lo modificamos
            @vector[puntero]=elem_new
            puts "Elemento modificado"
        else
            puts "nada se modifico"
        end
    end    



    #Imprime todos los elementos del arreglo
    def printAll()
        if @vector.length > 0
            @vector.each_with_index do |elemento, index|
                puts "Elemento[#{index}]=#{elemento}"
            end
        else
            puts "El arreglo está vació"
        end
    end
end
