#Vamos a crear nuestra primera función.
#Una función se representa matemáticamente como caja negra
#(le introducimos datos y sale un resultado p.ej. gráfica)

#Función a la que le pasemos tres números y nos devuelva la nota media

#Estructura:

#Funciones (definir funciones (definimos lo que hace) /= llamar (hacemos que actúe))

def mediaTresNumeros (num1,num2,num3): 
    resultado = (num1+num2+num3)/3
    return resultado

#Código principal (main)

print ("Probando función")
media = mediaTresNumeros (5,2,7) #tres números aleatorios que quieras, pueden ser p ej. (7,9,3)
                                #Aquí está la llamada a la función
print (media) #Aquí está lo que ha mandado el return de la función pero porque hemos hecho la igualación anterior.
