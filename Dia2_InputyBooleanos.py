#print ("Introduce tu nombre:")
#nombre = input() #Lo que yo introduzca lo va a mostrar
#print (nombre)
#print ("Hola " + nombre)

#Con python podemos meter la pregunta en el input
#El input recoge el dato y lo guarda en nombre

nombre = input("Introduce tu nombre: ")
print ("Hola " + nombre)

#Existen dos tipos de = en programacion:

# = ->  Asigna lo que hay en la izquierda con lo de la derecha
#       Ej. numero = 5
# == -> Igual lógico. Compara los valores que tiene a la izquierda y a la decha
#       El igual lógico devuelve True (son iguales) False (son distintas)

# Ejercicio 1. Entrada: Número. Salida: True si es mayor de edad.

numero = int (input ("Introduce tu edad: "))
# print (type (numero)) para saber el tipo.
print ("¿Es mayor de edad?" )
print ((numero>=18))

#Cuando hacemos un input siempre por defecto guarda el valor introducido como str,
#   si queremos que sea un numero entero,
#   hay que transformarlo. Para ello le pondremos int (input)...)


#__________________________________________________________________________________


#Ejercicio 2: Dia de la semana. True si es fin de semana//False: si no es fin de semana.

diaSemana = (input ("Introduce un día de la semana: "))
print ("¿Es fin de semana?")
print (diaSemana == "sabado" or diaSemana == "domingo")

#Ejercicio 3: Numero. True si es positivo//False si es negativo.

numero = int (input ("Introduce un número: "))
print ("¿Es positivo?")
print ((numero>=0))

#Ejercicio 4: Letra. True si es vocal // False si es consonante.

letra = (input ("Introduce una letra: "))
print ("¿Es una vocal?")
print (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u")

#Ejercicio 5: Numero. True si es aprobado // False si es suspenso.

numero = int (input ("Introduce tu calificación: "))
print ("¿Está aprobado?")
print ((numero >=5 and numero <= 10))

#___________________________________________________________________________________







































