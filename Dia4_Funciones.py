#Funciones. ((A Celia le encanta la función línea)).
#Las funciones son trocitos de código a los que podemos llamar.
#En las funciones nunca se pone un print!!!! Porque las funciones están en el back,
# y esto no se imprimirá en ninguna pantalla, así que no se pone porque no servirá para nada.
#Todos los print tienen que estar en la vista, no en el cómputo.
#Las funciones tienen que tener una función (sumar números, hacer la media...)
#       y esto no es mostrarlo por pantalla.
#A no ser que esté pensada SÓLO para imprimir por pantalla.

#A cada uno de los elementos que entran en la función le llamamos Argumentos.
#                           num1, num2 y num3 son argumentos de entrada.
#Resultado será el argumento de salida que se guarda en la variable resultado.

#Podemos tener funciones sin return.
#Esto es una excepción, de normal no usamos
#           print() en funciones, solo cuando el objetivo de la función sea mostrar algo.

def dibujarLinea (forma): #No tiene argumentos de salida.
    print (forma*20)
    #return no hay
def dibujarLineaPuntos(): #No tiene argumentos de entrada. No tiene return.
    print ("."*20)
#SIn return
#Para hacerlo sin print:

def crearLinea (forma): #Necesitamos crear un print de lo que devuelve esta función,
#porque si solo la llamamos no nos muestra nada.
    return (forma*20) 
    
#____________________________________________
#Se puede hacer de varias formas.

#Para operaciones sencillas
def mediaTresNumeros (num1,num2,num3): 
    resultado = (num1+num2+num3)/3
    return resultado
#Para dividir la operación final en más sencillas.
def mediaTresNumeros (num1,num2,num3): 
    return (num1+num2+num3)/3
#Cuando queramos que nos quede claro.
def mediaTresNumeros (num1,num2,num3): 
    suma = (num1+num2+num3)
    return suma/3

#________________________________________________________________

print ("Probando función")
media = mediaTresNumeros (5,2,7) 
print (media)
dibujarLinea ("=")
dibujarLinea ("x")
dibujarLinea ("_")
dibujarLineaPuntos ()

#Hacemos print() de lo que devuelve la función
#       para no hacer print dentro de la misma.
print (crearLinea ("*"))

#Con estas funciones, sacad por pantalla línea hecha con "o",ç
#"la media de 5, 10 y 15 es:10" y una línea con "O" 

dibujarLinea ("o") #no pongo print porque la función ya tiene un print dentro

print (crearLinea ("o")) #crearLinea si necesita print.

x = 5
y = 10
z = 15

media = mediaTresNumeros (x,y,z)
print ("La media de" + str (x) + ", " + str (y) + " y " + str(z) + " es: " + str (media))
print (media)

#Otra forma

print (f"La media es de {media}")

dibujarLinea ("O")

print (dibujarLinea) #Si hacemos esto, no estamos poniendo el paréntesis que nos permite llamar a la función,
# entonces aparece la direccion de memoria donde esta almacenado el principio de la función.

#Hacer código en el que nos pidan nombre y una edad.

nombre = input("Escribe tu nombre: ")
edad = input ("Escribe tu edad: ")

def presentacion (nombre, edad):
    
    return ("Hola soy " + nombre + " y tengo " + edad + " anios.")

print (presentacion(nombre,edad))


# RECORDAR EL VIERNES A CELIA: " Celia, las funciones solo pueden tener un return".






































