# Ejercicio 1. Entrada: Número. Salida: True si es mayor de edad.

edad = int (input ("Introduce tu edad: "))
print ("¿Es mayor de edad?" )
#Se puede escribir 'esMayorEdad = edad>=18'
esMayorEdad = (edad>=18)
print (esMayorEdad)
#esMayorEdad es una variable de tipo bool.
print (type(esMayorEdad))

#Dentro de un IfElse siempre tiene que haber un booleano.

if esMayorEdad: #También podemos poner edad>=18 directamente en lugar de la variable booleana esMayorEdad.
    print ("Es mayor de edad") #OJO!! Es necesario poner UNA tabulación si no se pone,
#hace un print normal que sale siempre.
#print ("Se imprime siempre")
else:
    print ("Es menor de edad") #Else SIEMPRE necesita ir debajo de un if, necesita la condicional para funcional

#_______________________________________________________________________________________________________

#Ejercicio 3: Numero. True si es positivo//False si es negativo.

numero = int (input ("Introduce un número: "))
print ("¿Es positivo?")
esPositivo = (numero > 0)

#print (type(esPositivo)) Para comprobar si es booleana

if esPositivo:
    print ("Es positivo")

elif numero == 0: #else if 
    print ("Es cero")

else:
    print ("Es negativo")


#____________________________________________________________________

#Ejercicio 5: Numero. True si es aprobado // False si es suspenso. Nos va a decir la nota
# 9-10 = Sobresaliente 8-7 notable 6 bien 5 suficiente y menos de 5 suspenso

nota = int (input ("Introduce tu calificación: "))
print ("¿Qué nota tiene?")

#Asumimos que la gente puede introducir números no válidos, entonces hacemos:

if nota > 10 or nota < 0:
    print ("Nota no válida")
elif nota >=9:
    print ("Sobresaliente")
elif nota >=7:
    print ("Tienes notable")
elif nota >=6:
    print ("Tienes un bien")
elif nota >=5:
    print ("Tienes un suficiente")
else:
    print ("Has suspendido")

#Asumimos que se va a introducir una nota válida. (Que la interfaz gráfica no deje poner los otros números).

nota = int (input ("Introduce tu calificación entre 10 y 0: "))
print ("¿Qué nota tiene?")

if nota <= 10 and nota >=9:
    print ("Sobresaliente")
elif nota >=7:
    print ("Tienes notable")
elif nota >=6:
    print ("Tienes un bien")
elif nota >=5:
    print ("Tienes un suficiente")
else:
    print ("Has suspendido")







#Ejercicio 2: Dia de la semana. True si es fin de semana//False: si no es fin de semana.

diaSemana = (input ("Introduce un día de la semana: "))
print ("¿Es fin de semana?")
print (diaSemana == "sabado" or diaSemana == "domingo")



#Ejercicio 4: Letra. True si es vocal // False si es consonante.

letra = (input ("Introduce una letra: "))
print ("¿Es una vocal?")
print (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u")

