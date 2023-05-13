# Funciones en python
# def nombre_funcion(parametros entrada):
#  Sentencias 1
#  Sentencias 2
#  ...

''' Funcion sin parámtros de entrada '''
def encender_coche():
    print('coche encendido')

encender_coche()

'''Funcion con parámetros de entrada'''
def sumar(a, b):
    print(a+b)

sumar(1,2)
sumar(4,7)
sumar(6,1)

'''Funcion con parámetros de entrada y con retorno'''
def sumar(a,b):
    return(a+b)

x=sumar(1,2) * 3
print(x)

'''Funcion con parámetros de entrada inicializados'''
def sumar(a=1,b=2):
    return(a+b)
 
x=sumar() # por defecto toma el valor de a=1 y b=2 "valores inicializados"
x=sumar(3,4) # reemplazamos los valores de los parámetros de manera posicional a = 3 y b = 4
x=sumar(b=5,a=10) # reemplazamos los valores por defecto de a y b, a=10 y b=5
x=sumar(a=10)
x=sumar(b=10)
print(x)


# Ejercicio 1:
# Escribe una función llamada "saludar" que tome un nombre como argumento y muestre un mensaje de saludo, 
# por ejemplo: "¡Hola, [nombre]!"

def saludar(nombre):
    print("¡Hola, " + nombre)

saludar("Yeison")
saludar("Laura")
saludar("Michael")
saludar("David")

# Ejercicio 2:
# Escribe una función llamada "calcular_promedio" que tome una lista de números como argumento y 
# devuelva el promedio de esos números.

def calcular_promedio(lista):
    return sum(lista)/len(lista)

notas = {
    'Laura':{
            'notas': [3.5, 4.2, 5.0, 3.2]
            },
    'David':{
            'notas': [3.5, 4.0, 4.5, 3.3]
            },
    'Michael':{
            'notas': [3.0, 4.2, 4.4, 3.6]
            }    
}

# for nombre, notas in notas.items():
#     print('El estudiante', nombre ,'tiene las notas de', notas['notas'] , 'y su promedio es: ', calcular_promedio(notas['notas']))

# Ejercicio 3:
# Crear una función que retorne el porcentaje de iva de un producto, la funcion debe tener como parametro de IVA del 
# 19 % pero con la opción de poderse modificar en el llamado de la función 

def calcular_iva(valor_producto, iva=0.19):
    print(valor_producto*iva)

calcular_iva(10000)


# Ejercicio 1:
# Escribe una función llamada "es_par" que tome un número como argumento y devuelva True si el número es par, 
# y False si es impar.

# Ejercicio 2:
# Escribe una función llamada "calcular_area_triangulo" que tome la base y la altura de un triángulo como 
# argumentos y devuelva su área.

# Ejercicio 3:
# Escribe una función llamada "contar_vocales" que tome una cadena como argumento y devuelva la cantidad de 
# vocales que contiene.

# Ejercicio 4:
# Escribe una función llamada "ordenar_lista" que tome una lista de números como argumento y devuelva la lista 
# ordenada de menor a mayor.

# Ejercicio 5:
# Escribe una función llamada "invertir_cadena" que tome una cadena como argumento y devuelva la cadena invertida, 
# es decir, en orden inverso.

# Consultar:
# 1. Qué es Open CV y para que sirve
# 2. Ver el siguiente video de instalación de la libreria:
#  https://www.youtube.com/watch?v=6R_VU958jPY