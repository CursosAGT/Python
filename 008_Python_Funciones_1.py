from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Funciones y Métodos                            ║
║                              -------------------                            ║
║                                                                             ║
║          Funciones    Descripción                                           ║
║                                                                             ║
║          Métodos son funciones dentro de clases donde se debería instanciar ║
║                   a la clase con self                                       ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                              Funciones y Métodos                            ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

https://www.w3schools.com/python/python_ref_list.asp"
https://www.w3schools.com/python/python_lists.asp"
https://python-para-impacientes.blogspot.com/2014/02/programacion-funcional-funciones-de.html
https://python-para-impacientes.blogspot.com/2014/02/funciones.html

Funciones
=========
Una función es como una caja negra: una vez creada no debemos preocuparnos por lo que tiene en su interior, simplemente, tenemos que recordar su nombre y los datos que necesita para resolver un proceso. Generalmente, devuelven un resultado.
La principal virtud de una función está en la reutilización del código, es decir, una vez creada puede ser llamada cada vez que se necesite. Para mejor aprovechamiento debemos procurar que las funciones ofrezcan soluciones a necesidades muy concretas.

Funciones con un número fijo de parámetros
La siguiente función calcula el área de un triángulo. Una vez definida se utiliza para calcular el área de dos triángulos de distintas dimensiones.
Para definir la función escribiremos def seguido del nombre de la función y entre paréntesis los dos parámetros que son necesarios para calcular el área del triángulo: base y altura. Con return la función devolverá el resultado de la fórmula matemática expresada. Los dos parámetros son obligatorios. Si alguno falta habrá una excepción.
""");
nuevo(0,"inicio");
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Funciones simples                              ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
#################################################################
#Ejercicio_Funciones_Ej_001
#------------empecemos por lo mas simple
print("empecemos por lo mas simple")
print ("linea 1")
print ("linea 2")
print ("linea 3")
print ("linea 4")
print ("linea 5")
def Funcion_1():# ver el orden
	print ("linea 11")
	print ("linea 12")
	print ("linea 13")
	print ("linea 14")
	print ("linea 15")
print ("linea 6")
print ("linea 7")
print ("linea 8")
print ("linea 9")
print ("linea 10")# ver el orden
print("llamo a Funcion1")
Funcion_1()
print("------------")
print("vuelvo a llamar a Funcion1")
Funcion_1()
print("------------")
print("Nuevamente llamo a Funcion1")
Funcion_1()
nuevo(1);
#################################################################
#Ejercicio_Funciones_Ej_002
#------------Ingreso , calculo e impresión de datos en la función
print("Ingreso y calculo de datos en la función")
def Funcion_2():
	dato=int(input("Ingrese un valor : "))
	print ("su dato ",dato," al cuadrado es ", dato ** 2)
	return 0
Funcion_2()
print("------------")
Funcion_2()
print("------------")
Funcion_2()

nuevo(2);
#################################################################
#Ejercicio_Funciones_Ej_003
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: envió de un dato mediante dato=                               ║
║        int(input("Ingrese un valor : "))variable - parametro fijo           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
#------------Ingreso desde fuera de la función y calculo e impresion de datos dentro la funcion
print("Ingreso desde fuera de la función y calculo de datos dentro la funcion")
def Funcion_3(dato_entrada_a_la_Funcion):
	resul= dato_entrada_a_la_Funcion ** 2
	print (f"su dato de entrada fue {dato_entrada_a_la_Funcion} al cuadrado es {resul}")
	return 0
dato_salida_a_la_Funcion=int(input("Ingrese un valor : "))
Funcion_3(dato_salida_a_la_Funcion)
print("------------")
dato_salida_a_la_Funcion=int(input("Ingrese un valor : "))
Funcion_3(dato_salida_a_la_Funcion)
print("------------")
dato_salida_a_la_Funcion=int(input("Ingrese un valor : "))
Funcion_3(dato_salida_a_la_Funcion)
nuevo(3);dato=int(input("Ingrese un valor : "))
#################################################################
#Ejercicio_Funciones_Ej_004
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: return con un dato                                            ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
#------------Ingreso y salida de datos desde fuera de la función y calculo de datos dentro la funcion
print("Ingreso y salida de datos desde fuera de la función y calculo de datos dentro la funcion")
def Funcion_4(dato_entrada):
	resul=dato_entrada ** 2
	print(f"valor de dato entrada es {dato_entrada} ^2 = {resul} desde dentro de la funcion")
	return (resul)
	
	
### fuera de la fuuncion

print("Ingreso y salida de datos desde fuera de la función y calculo de datos dentro la función")

print("El dato lo ingresa el programaador = 50")
dato_salida = 50
resultado = Funcion_4(dato_salida)
print (f"Su dato de salida fue {dato_salida} al cuadrado es {resultado}" )

print("El dato lo ingresa el usuario")
dato_salida=int(input("Ingrese un valor : "))
resultado = Funcion_4(dato_salida)
print (f"Su dato de salida fue {dato_salida} al cuadrado es {resultado}" )
print("------------")
dato_salida=int(input("Ingrese un valor : "))
resultado = Funcion_4(dato_salida)
print (f"Su dato de salida fue {dato_salida} al cuadrado es {resultado}" )
print("------------")
dato_salida=int(input("Ingrese un valor : "))
resultado = Funcion_4(dato_salida)
print (f"Su dato de salida fue {dato_salida} al cuadrado es {resultado}" )
print("--------dentro de un bucle------------")
for conta in range (3):
	dato_salida=int(input("Ingrese un valor : "))
	resultado = Funcion_4(dato_salida)#                    aqui llamo a la función y recibo los datos
	print (f"Su dato de salida fue {dato_salida} al cuadrado es {resultado}" )
	print("------------")
nuevo(4);
#################################################################
#Ejercicio_Funciones_Ej_005
#------------Ingreso y salida de datos desde fuera de la función y calculo de datos dentro la función
print("Ingreso y salida de datos desde fuera de la función y calculo de datos dentro la función")
def Funcion_5(variable_1,variable_2):
	resul = (variable_1*variable_2)
	variable_1=0
	variable_2=0
	print("cambio el valor de las variables dentro de la funcion")
	print ("sus datos ",variable_1," y ",variable_2 )
	return resul

for conta in range (3):
	variable_1=int(input("Ingrese el 1º valor : "))
	variable_2=int(input("Ingrese el 2º valor : "))
	resul = Funcion_5(variable_1,variable_2)
	print ("sus datos ",variable_1," y ",variable_2, " multiplicado dan ", resul )
	print("no se cambio el valor de las variables fuera de la funcion")
	print("------------")
nuevo(5)

#################################################################
#Ejercicio_Funciones_Ej_006

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: envió de 2 o mas datos mediante variables - parámetros fijos  ║
║               return con dos +o mas variables                               ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");9999
def funcion(variable, lista):
	print("Dentro la funcion")
	variable = variable * 1000	#valor modificado
	lista[0]=99	#valor modificado
	lista.append(9999)	#agrego un segundo valor modificado
	print ("dentro del ámbito de la función la variable toma el valor :",variable)
	print ("dentro del ámbito de la función la lista toma el / los valores :",lista)
	print("Salgo de la funcion")
	return variable
print("Valores originales antes de llamar a la funcion")
variable = 2020		#valor original
lista = [2020]		#valor original
print ("Antes de llamar a la funcion")
print ("fuera del ámbito de la función antes de pasar la variable toma el valor :",variable)
print ("fuera del ámbito de la función antes de pasar la lista toma el / los valores :",lista)
print ("------------------------------------------------------------------------------------")
pausa()
print ("Llamo a la funcion")
variable_2=funcion(variable, lista)
print ("------------------------------------------------------------------------------------")
pausa()
print ("Despues de llamar a la funcion")
print ("fuera del ámbito de la función luego de pasar la variable toma el valor :",variable)
print ("fuera del ámbito de la función luego de pasar la lista toma el / los valores :",lista)
print ("dentro de una funcion las variables mantienen en valor de cada ambito, las listas NO")
print ("fuera del  ámbito de la función luego de pasar la variable y retornarla variable2 toma el valor :",variable_2)
print ("------------------------------------------------------------------------------------")
pausa()
print ("""En Python existen objetos inmutables, como las tuplas, por lo que si intentáramos modiﬁcar una tupla pasada como parámetro lo que ocurriría en realidad es que se crearía una nueva instancia,
por lo que los cambios no se verían fuera de la función. Veamos un pequeño programa para demostrarlo:
Como vemos la variable  no conserva los cambios una vez salimos de la función porque los enteros son inmutables en Python.
Sin embargo la lista si los conserva los cambios, porque las listas son mutables.
En resumen: los valores mutables se comportan como paso por refe-rencia, y los inmutables como paso por valor""")

nuevo(6);
#################################################################
#Ejercicio_Funciones_Ej_007
#------------Ingreso y salida de datos desde fuera de la función y calculo de datos dentro la función con datos por defauld

print("""
Funciones con parámetros con valores por defecto
------------------------------------------------
La función pagar tiene el parámetro dto_aplicado con el valor 5 asignado por omisión. Dicho valor se utilizará en la solución en el caso de omitirse este dato cuando sea llamada la función.
""")
def funcion_cuanto_pagar(importe, dto_aplicado = 5):
	''' La función aplica descuentos '''
	resul =(importe - (importe * dto_aplicado / 100))
	return resul
importe=1000
print("sin enviar descuento:",funcion_cuanto_pagar(importe))  				# 950
print("Envio descuento del 0 %:",funcion_cuanto_pagar(importe,0))  				# 1000
print("Envio descuento del 10 %:",funcion_cuanto_pagar(importe, 10), "tuvo un descuento de ",(importe-funcion_cuanto_pagar(importe, 10)))  			# 900

nuevo(7);
#################################################################
#Ejercicio_Funciones_Ej_008
#------------Ingreso y salida de datos desde fuera de la función y calculo de datos dentro la función con datos por defauld
print ("""
En Python, también es posible llamar a una función, pasándole los argumentos esperados, como pares de claves=valor:
""")
def saludar(nombre, mensaje='Hola'):
	print (mensaje, nombre)

print("sin mensaje : ")
saludar("Facu")

for cont in range (3):
	dato_salida_1=(input("Ingrese nombre : "))
	dato_salida_2=(input("Ingrese mensaje : "))
	if dato_salida_2 =="":
		print("salida con saludo no cargado entra el defauld")
		saludar(dato_salida_1)# sin un valor en el 2do parámetro "mensaje"
	else:
		print("salida con saludo con cargado")
		saludar(dato_salida_1,dato_salida_2)#simple
		print("desconozco el orden de las variable")
		saludar(mensaje=dato_salida_2, nombre=dato_salida_1)# con función orden no definido

nuevo(8);
#################################################################
#Ejercicio_Funciones_Ej_009
print("Ingreso y salida de datos desde fuera de la función y calculo de datos dentro la función con datos por defauld")
#def Funcion_5(dato_entrada_1,dato_entrada_2,dato_entrada_3,dato_entrada_4):

def Funcion_5(dato_entrada_1=111,dato_entrada_2=222,dato_entrada_3=333,dato_entrada_4=444):
	resultado = (int(dato_entrada_1)*int(dato_entrada_2)*int(dato_entrada_3)*int(dato_entrada_4))
	return resultado 
resultado = Funcion_5()# LLamo a dato_entrada_2la funcion SIN DATOS
print ("resultado :", resultado )#Regreso de la funcion con los datos por defauld

repet=int(input("Ingrese el numero de repeticiones :"))
for cont in range(repet):
	dato_salida_1=int(input("Ingrese el 1º valor : ")) 
	dato_salida_2=int(input("Ingrese el 2º valor : "))
	dato_salida_3=int(input("Ingrese el 3º valor : "))
	dato_salida_4=int(input("Ingrese el 4º valor : "))
	resultado = Funcion_5(dato_salida_1,dato_salida_2,dato_salida_3,dato_salida_4)
	print ("sus datouncion_5(s ",Funcion_5(dato_salida_1,dato_salida_2,dato_salida_3,dato_salida_4), " multiplicado da ", resultado )
	print("------------")
nuevo(9);
#################################################################
#Ejercicio_Funciones_Ej_010
print("""
Función con todos los parámetros con valores no numéricos por defecto
---------------------------------------------------------------------
Todos los parámetros tienen un valor por defecto. Cuando se utiliza la función si se especifican los nombres de los parámetros éstos pueden estar en distinto orden.
""")
def repite_caracter(caracter="-", repite=3):
	return (caracter * repite)

print(repite_caracter())  						# Se utilizan valores por omisión
print(repite_caracter('.',30)) 					# Muestra línea con 30 puntos
print(repite_caracter(20,'$')) 					# Muestra $ con 20 puntos
print("prestar atencion al orden de variables\n Hay que hacer referencias a las variables de entrada")#
print(repite_caracter(repite=10, caracter='*'))	# Muestra: **********
print(repite_caracter(caracter="%"))			# Muestra: %%%
print(repite_caracter(repite=10))				# Muestra: ----------
nuevo(10);
#################################################################
#Ejercicio_Funciones_Ej_011

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones que llama a otra función                                       ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");


def area_triangulo(base, altura):  					# define función con dos parámetros
	print(" Calcular el área de un triangulo ")  		# cadena de documentación
	print("Regreso el resultado, la base y la altura - 3 datos separdos por coma - una lista")
	resultado =base * altura / 2
	return (resultado,base , altura)# devuelve el resultado de la expresión en una lista

def salida_x_pantalla_l(lista):
	print(f"Dado los valores Base = {lista[1]} y altura = {lista[2]} \nEl resultado es {lista[0]} cm^2")


def salida_x_pantalla_t(*tupla):
	print(f"Dado los valores Base = {tupla[1]} y altura = {tupla[2]} \nEl resultado es {tupla[0]} cm^2")


def salida_x_pantalla_d(**diccionario):
	print("Dado los valores Base = {} y altura = {} \nEl resultado es {} cm^2". format(diccionario["calculo_"],diccionario["base_"],diccionario["altura_"]));


base=6;#base=float(input"Ingrese la base"));
altura=4;#altura=float(input"Ingrese la altura"));
#1er ej
print ("\nfuncion unica")
resultado = area_triangulo(base, altura);									# la función retornará el valor 12
print(f"Dado los valores Base = {resultado[1]} y altura = {resultado[2]} \nEl resultado es {resultado[0]} cm^2");
print ("------------------------------------------------------------------------------------")
pausa()

print("funcion anillada con lista");#	           =        con funcion anilladaaltura
salida_x_pantalla_l(area_triangulo(base, altura));#					desde 1er funcion descompongo lista 
print ("------------------------------------------------------------------------------------")
pausa()
print("funcion anillada con tupla");#	           =        con funcion anillada
calculo,base,altura=(area_triangulo(base, altura));#				desde 1er funcion descompongo lista 
salida_x_pantalla_t(calculo,base,altura);#							Armo la tupla
print ("------------------------------------------------------------------------------------")
pausa()
print("funcion anillada con diccionario");#           =        con funcion anillada
calculo,base,altura=(area_triangulo(base, altura));#				desde 1er funcion descompongo lista 
salida_x_pantalla_d(calculo_=calculo,base_=base,altura_=altura)#	Armo el diccionario

#2do ej
print ("\n---------------------------------------------------------------")
print ("\nfuncion unica - variables invertidas")
calculo = area_triangulo(altura=altura , base=base);
print(f"Dado los valores Base = {calculo[1]} y altura = {calculo[2]} \nEl resultado es {calculo[0]} cm^2");


print("funcion anillada con lista");
salida_x_pantalla_l(area_triangulo(base, altura));
#3er ej
print ("\n---------------------------------------------------------------")
print ("\nfuncion unica")
base=int(input("Ingrese el 1º valor Base: "))
altura=int(input("Ingrese el 2º valor Altura: "))
calculo = area_triangulo(base, altura);									# la función retornará el valor 12
print(f"Dado los valores Base = {calculo[1]} y altura = {calculo[2]} \nEl resultado es {calculo[0]} cm^2");
print ("------------------------------------------------------------------------------------")
pausa()
print("funcion anillada con lista");#           =        con funcion anillada
salida_x_pantalla_l(area_triangulo(base, altura));						# la función retornará el valor 12
print ("------------------------------------------------------------------------------------")
pausa()
print("funcion anillada con tupla");#           =        con funcion anillada
calculo,base,altura=(area_triangulo(base, altura));						# la función retornará el valor 12
salida_x_pantalla_t(calculo,base,altura);						# la función retornará el valor 12
print ("------------------------------------------------------------------------------------")
pausa()
print("funcion anillada con diccionario");#           =        con funcion anillada
calculo,base,altura=(area_triangulo(base, altura));						# la función retornará el valor 12
salida_x_pantalla_d(calculo_=calculo,base_=base,altura_=altura)
nuevo(11);


#################################################################
#Ejercicio_Funciones_Ej_012
#------------Ingreso y salida de datos desde fuera de la función y calculo de datos dentro la función con datos por defauld
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: envió de datos mediante tuplas - parámetros arbitrarios       ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
Python puede pasar una variable como argumento de una función, estas se pasan por referencia o por valor.
En el caso de pasar un valor, python enviá como argumento es el valor que contenía la variable
En el paso por referencia lo que se pasa como argumento es una 'referencia o puntero', realmente la dirección de memoria en la que se encuentra el contenido de la variable o conjuntos, no el contenido en si. En realidad lo que se le pasa a la función son copias de los valores y no las variables en si.
""");
print("Ingreso y salida de datos desde fuera de la función y calculo de datos dentro la función con datos por defauld")
def calcular_promedio(*argumentos):
	total = 0
	for datos_para_suma in argumentos:
		total = total + datos_para_suma
	resultado = total / len(argumentos)
	return resultado
dato_salida_1=int(input("Ingrese el 1º valor : "))
dato_salida_2=int(input("Ingrese el 2º valor : "))
dato_salida_3=int(input("Ingrese el 3º valor : "))
dato_salida_4=int(input("Ingrese el 4º valor : "))
resul = calcular_promedio(dato_salida_1,dato_salida_2,dato_salida_3,dato_salida_4)

print(f"el promedio de {dato_salida_1}, {dato_salida_2} , {dato_salida_3} y {dato_salida_4} es: {resul}")

print("La funcion se adapta a la cantidad de datos que le envio")
dato_salida_1=int(input("Ingrese el 1º valor : "))
dato_salida_2=int(input("Ingrese el 2º valor : "))
resul = calcular_promedio(dato_salida_1,dato_salida_2)

print(f"el promedio de {dato_salida_1} y {dato_salida_2} es: {resul}")

dato=[];
for cont in range(4):
	dato.append(int(input(f"Ingrese el valor Numero {cont}: ")))

resul = calcular_promedio(*dato)

print(f"el promedio de {dato[0]}, {dato[1]} , {dato[2]} y {dato[3]} es: {resul}")






nuevo(12);
#################################################################
#Ejercicio_Funciones_Ej_013
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: envió de datos mediante tuplas - parámetros arbitrarios       ║
║               devuelve 2 parámetros de resultado                            ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
def calcular_promedio_desv(*argumentos):
	total = 0
	for i in argumentos:
		total += i
	promedio = total / len(argumentos)
	total = 0
	for i in argumentos:
		total += (i - promedio) ** 2
	desviacion_tipica = (total / len(argumentos)) ** 0.5
	return promedio, desviacion_tipica

dato_salida_1=int(input("Ingrese el 1º valor : "))
dato_salida_2=int(input("Ingrese el 2º valor : "))
dato_salida_3=int(input("Ingrese el 3º valor : "))
dato_salida_4=int(input("Ingrese el 4º valor : "))

print("recibo ")
resul_promedio, resul_desviacion_tipica = calcular_promedio_desv(dato_salida_1,dato_salida_2,dato_salida_3,dato_salida_4)
print(f"Datose {dato_salida_1}, {dato_salida_2} , {dato_salida_3} y {dato_salida_4}")
print(f"promedio: es: {resul_promedio}")
print(f"Desviación típica: {resul_desviacion_tipica}")


resul_lista=[];
resul_lista = calcular_promedio_desv(dato_salida_1,dato_salida_2,dato_salida_3,dato_salida_4)
print(f"Datose {dato_salida_1}, {dato_salida_2} , {dato_salida_3} y {dato_salida_4}")
print(f"promedio: es: {resul_lista[0]}")
print(f"Desviación típica: {resul_lista[1]}")


nuevo(13);
#################################################################
#Ejercicio_Funciones_Ej_014
print ("""
Parámetros tupla
Al igual que en otros lenguajes de alto nivel, es posible que una función, espere recibir un número arbitrario -desconocido- de argumentos. Estos argumentos, llegarán a la función en forma de tupla.
Para definir argumentos tupla en una función, se antecede al parámetro un asterisco (*):
Si una función espera recibir parámetros fijos y tupla, los arbitrarios siempre deben suceder a los fijos.
""")
def recorrer_parametros(variable_para_parametro_fijo, *tupla_para_varios_datos_arbitrarios):
	print ("dato parametro fijo - variable :",variable_para_parametro_fijo)
	# Los parámetros tupla se corren como tuplas
	print("datos del array tipo tupla:")
	for argumento in tupla_para_varios_datos_arbitrarios:
		print ("\t",argumento)
recorrer_parametros('dato parametro fijo', 'dato arbitrario 1', 'dato arbitrario 2', 'dato arbitrario 3')

variable="parametro fijo";
tupla=("arbitrario 1", "arbitrario 2", "arbitrario 3");
recorrer_parametros(variable,*tupla)

nuevo(14);
#################################################################
#Ejercicio_Funciones_Ej_015
print("""
Funciones con un número variable de parámetros
----------------------------------------------
La siguiente función suma la distancia de un número variable de tramos. Si se utiliza sin aportar ningún valor devolverá 0. También, como cabría pensar es posible pasar variables.
""")
def distancia(*tramos):						# define función con nº variable de parámetros
	''' Suma distancia de tramos '''		# cadena de documentación
	total = 0								# inicializa variable numérica
	for distancia in tramos:				# recorre, uno a uno, los tramos...
		total = total + distancia			# … y acumula la distancia
	return total							# devuelve la suma de todos los parámetros

dato_salida_1=int(input("Ingrese los km que condujo 1º: "))
dato_salida_2=int(input("Ingrese los km que condujo 2º: "))
dato_salida_3=int(input("Ingrese los km que condujo 3º: "))
dato_salida_4=int(input("Ingrese los km que condujo 4º: "))
print ("\n---------------------------------------------------------------");
resul = distancia(dato_salida_1,dato_salida_2,dato_salida_3,dato_salida_4)
print(f"distancia {dato_salida_1} + {dato_salida_2} + {dato_salida_3} + {dato_salida_4} = {resul}")
print ("\n---------------------------------------------------------------");
tupla=(dato_salida_1,dato_salida_2,dato_salida_3,dato_salida_4)
resul = distancia(*tupla)
print(f"distancia {dato_salida_1} + {dato_salida_2} + {dato_salida_3} + {dato_salida_4} = {resul}")
print ("\n---------------------------------------------------------------");
lista=[]
cant_viajes=int(input("ingrese la cantidad ve viajes que realizo"));
for cont in range (cant_viajes):
	dato_a_lista=float(input(f"Ingrese los km que condujo {cont+1}º:"));#recuerden que los array empiezan rn 0 cero
	lista.append(dato_a_lista)
tupla=tuple(lista)
resul = distancia(*tupla)
print(f"distancias:",end="  ")
for cont in tupla:
	print(f"{cont}",end="  +  ")
print(f" = {resul}")
print ("\n---------------------------------------------------------------");
print("envio tupla vacia",distancia())						# la función retornará el valor 0
nuevo(15);
#################################################################

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: envió de datos mediante diccionarios - parámetros clave,valor ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
#Ejercicio_Funciones_Ej_016
def sumar(**argumentos):
	resul=0;
	print ("claves:Valores del diccionario :",argumentos)
	for clave,valor in argumentos.items():
		resul+=valor;
	print ("resultado: ",resul)

print ("\n---------------------------------------------------------------");

sumar(item_1=10, item_2=20)

print ("\n---------------------------------------------------------------");

Dic= {"item_1":10, "item_2":20,"item_3":30, "item_4":40,"item_5":50, "item_6":60,"item_7":70, "item_8":80,"item_9":90, "item_10":100}
sumar(**Dic)

print ("\n---------------------------------------------------------------");

Dic = dict(Item_1=10,Item_2=20, Item_3=30,Item_4=40, Item_5=50,Item_6=60, Item_7=70, Item_8=80,Item_9=90, Item_10=100)
sumar(**Dic)
								
nuevo(16)
#################################################################
#Ejercicio_Funciones_Ej_017
print ("""
Es posible también, obtener parámetros diccionarios como pares de clave=valor. En estos casos, al nombre del parámetro deben precederle dos asteriscos (**):
""")


def recorrer_parametros(variable_para_parametro_fijo, *tupla_para_varios_datos_arbitrarios, **diccionario ):
	print ("dato parametro fijo - variable :",variable_para_parametro_fijo)
	# Los parámetros tupla se corren como tuplas
	print("datos del array tipo tupla:")
	for argumento in tupla_para_varios_datos_arbitrarios:
		print ("\t",argumento)
	print("datos del Diccionario Clave:Valor")
	for clave in diccionario:
		print ("El valor de", clave, "es", diccionario[clave])
print ("\n---------------------------------------------------------------");
recorrer_parametros("parametro fijo", "arbitrario 1", "arbitrario 2", "arbitrario 3", clave1="valor uno", clave2="valor dos")
print ("\n---------------------------------------------------------------");
variable="parametro fijo";
tupla=("arbitrario 1", "arbitrario 2", "arbitrario 3");
dic={"clave1":"valor uno","clave2":"valor dos"}
recorrer_parametros(variable,*tupla,**dic)
print ("\n---------------------------------------------------------------");


nuevo(17)
#################################################################
#Ejercicio_Funciones_Ej_018
print("""
Funciones con parámetros que contienen diccionarios
---------------------------------------------------
La función porc_aprobados tiene el parámetro **aulas que es un diccionario
 que contendrá las aulas de una escuela con el número alumnos de cada una. 
 Cuando es llamada la función se pasa también el número de alumnos que aprobaron el curso.
  La función suma los alumnos de todas las aulas y calcula el porcentaje de aprobados.
""")
def porc_aprobados(aprobados, **aulas):
	print(''' Calcula el % de aprobados ''')
	total=0
	for alumnos in aulas.values():
		total += alumnos
	return aprobados * 100 / total
porcentaje_aprobados = porc_aprobados(48, A = 22, B = 25, C = 21)
print(porcentaje_aprobados)
nuevo(18);
#################################################################
#Ejercicio_Funciones_Ej_019
print("""
Funciones que devuelven más de un valor
---------------------------------------
La función elemento_químico recibe un símbolo químico y devuelve el número atómico del elemento correspondiente y su denominación. Para ello, utiliza un diccionario en el que las claves son los símbolos químicos y los valores son cadenas que contienen para cada elemento su número atómico y denominación, unidos por un guión. Mediante el símbolo se accede a la cadena que luego es dividida con split en dos partes (utilizando como separador el propio guión '-'). split devuelve una lista con las dos partes. En lista[0] queda el número atómico y en lista[1] la denominación, los dos valores que devuelve esta función.
""")
def elemento_quimico(simbolo):
	''' Devuelve número atómico y denominación del elemento '''
	elementos = {'H':'1,Hidrógeno', 'He':'2,Helio', 'Li':'3,Litio'}
	elemento = elementos[simbolo]
	lista = elemento.split(',')
	print("Split divide el strings por el caractér incrustado (ver ejercicios print")
	return (lista[0], lista[1])

num_atomico, denomina = elemento_quimico('He')
print('Núm. Atómico:', num_atomico)
print('Denominación:', denomina)
print ("\n---------------------------------------------------------------");
num_atomico, denomina = elemento_quimico('Li')
print('Núm. Atómico:', num_atomico)
print('Denominación:', denomina)
print ("\n---------------------------------------------------------------");
num_atomico, denomina = elemento_quimico('H')
print('Núm. Atómico:', num_atomico)
print('Denominación:', denomina)
print ("\n---------------------------------------------------------------");
nuevo(19);
	#################################################################
#Ejercicio_Funciones_Ej_020
def elemento_quimico(simbolo):
	''' Devuelve número atómico y denominación del elemento '''
	elementos = {'H':[1,'Hidrógeno'], 'He':[2,'Helio'], 'Li':[3,'Litio']}
	elemento = elementos[simbolo]#aquí relaciono el diccionario con la clave que viene como variable
	return (elemento[0],elemento[1])

num_atomico, denomina = elemento_quimico('He')
print('Núm. Atómico:', num_atomico)
print('Denominación:', denomina)
print("-------------------------------")
num_atomico, denomina = elemento_quimico('Li')
print('Núm. Atómico:', num_atomico)
print('Denominación:', denomina)
print("-------------------------------")
num_atomico, denomina = elemento_quimico('H')
print('Núm. Atómico:', num_atomico)
print('Denominación:', denomina)
print("-------------------------------")
nuevo(20);
#################################################################
#Ejercicio_Funciones_Ej_021
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: envió datos mediante punteros (*tuplas o **diccionarios)      ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
print ("""
Desempaquetado de parámetros
Puede ocurrir además, una situación inversa a la anterior. Es decir, que la función espere una lista fija de parámetros, pero que éstos, en vez de estar disponibles de forma separada, se encuentren contenidos en una lista o tupla. En este caso, el signo asterisco (*) deberá preceder al nombre de la lista o tupla que es pasada como parámetro durante la llamada a la función:
""")
def calcular(importe, descuento):#                            dos datos de entrada
	return (importe - (importe * descuento / 100))#           un solo dato de salida

dato_salida_1=int(input("Ingrese el 1º valor importe : "))
dato_salida_2=int(input("Ingrese el 2º valor descuento : "))

array_de_salida = [dato_salida_1, dato_salida_2]#			 genero una lista o tupla para empaquetar datos
print (calcular(*array_de_salida))#                          sale por tupla

print ("""
El mismo caso puede darse cuando los valores a ser pasados como parámetros a una función, se encuentren disponibles en un diccionario. Aquí, deberán pasarse a la función, precedidos de dos asteriscos (**):
""")
def calcular(importe, descuento):#                            dos datos de entrada
	return importe - (importe * descuento / 100)

datos = {"descuento": dato_salida_2, "importe": dato_salida_1}#					 genero un diccionario para empaquetar datos
print (calcular(**datos))
nuevo(21);
#################################################################
#Ejercicio_Funciones_Ej_022


print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: return con un diccionario                                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");

def area_triangulo(base, altura):  					# define función con dos parámetros
	print(" Calcular el área de un triangulo ")  		# cadena de documentación
	resultado ={calculo:base * altura / 2,base:base , altura:altura}
	return (resultado)		 						# devuelve el resultado de la expresión en una lista
def salida_x_pantalla(**diccionario):
	print(f"Dado los valores Base = {lista[1]} y altura = {lista[2]} \nEl resultado es {lista[0]} cm^2")

base=6;
altura=4;
#1er ej
print ("\nfuncion unica")
calculo = area_triangulo(base, altura);									# la función retornará el valor 12
print(f"Dado los valores Base = {calculo[1]} y altura = {calculo[2]} \nEl resultado es {calculo[0]} cm^2");

print("funcion anillada");#           =        con funcion anillada
salida_x_pantalla(area_triangulo(base, altura));						# la función retornará el valor 12

#2do ej
print ("\nfuncion unica")
calculo = area_triangulo(altura=altura , base=base);					# la función retornará el valor 12
print(f"Dado los valores Base = {calculo[1]} y altura = {calculo[2]} \nEl resultado es {calculo[0]} cm^2");

print("funcion anillada");#          =        con funcion anillada
salida_x_pantalla(area_triangulo(base, altura));						# la función retornará el valor 12
#3er ej
print ("\nfuncion unica")
base=int(input("Ingrese el 1º valor Base: "))
altura=int(input("Ingrese el 2º valor Altura: "))
calculo = area_triangulo(base, altura);									# la función retornará el valor 12
print(f"Dado los valores Base = {calculo[1]} y altura = {calculo[2]} \nEl resultado es {calculo[0]} cm^2");

print("funcion anillada");#           =        con funcion anillada
salida_x_pantalla(area_triangulo(base, altura));						# la función retornará el valor 12

nuevo(22);
#################################################################
#Ejercicio_Funciones_Ej_023

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: en función                                                    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
a=999
b=999
c=999
print("a=",a,"valor en raiz")
print("b=",b,"valor en raiz")
print("c=",c,"valor en raiz")
print("-----------------")
def subrutina(a):
	def sub_subrutina(a):
		b = a + 1
		c = a * 100
		print("en sub_subrutina a=",a,"valor desde def sub_subrutina(a)")
		print("en sub_subrutina b=",b,"valor en sub_subrutina b=a +1")
		print("en sub_subrutina c=",c,"valor en sub_subrutina c=a * 100")
		print("-----------------")
		return (b)
	b= sub_subrutina(a)
	c = b +1
	print("en subrutina a=",a,"valor desde subrutina def subrutina(a)")
	print("en subrutina b=",b,"valor desde return de subrutina b= sub_subrutina(a)")
	print("en subrutina c=",c,"valor en subrutina c = b +1")
	print("-----------------")
	return (c)

a = int(input("ingrese un valor base y vea como cambian los valores de las variables :"))
c=subrutina(a)
print("en raiz a=",a,"desde input(..) ")
print("en raiz b=",b,"valor en raiz")
print("en raiz c=",c,"valor desde return de subrutina c= sub_subrutina(a)")
print("-----------------")
nuevo(23);

#################################################################
#Ejercicio_Funciones_Ej_024

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                        format_map / filter / reduce                         ║
║                                                                             ║
║                Iteraciones de orden superior sobre listas                   ║
╚═════════════════════════════════════════════════════════════════════════════╝

cadena = 'Empleado {Nombre} esta en la empresa como {Trabajo}'
Nombre_diccionario_1 = {'Nombre': 'Juan X', 'Trabajo': 'Programador'}

print(cadena.format_map(Nombre_diccionario_1))
print(cadena.format(**Nombre_diccionario_1))
""")
cadena = 'Empleado {Nombre} esta en la empresa como {Trabajo}'
Nombre_diccionario_1 = {'Nombre': 'Juan X', 'Trabajo': 'Programador'}

print(cadena.format_map(Nombre_diccionario_1))
print(cadena.format(**Nombre_diccionario_1))
print("""
Funciones de orden superior resulta del pasar iterando los distintos elementos de una lista, tupla, diccionarios, etc como argumentos de las funciones map y devuelve un iterador que contiene todos los resultados para los elementos de la lista.
Estas funciones nos permiten sustituir los bucles típicos de los lenguajes imperativos mediante construcciones equivalentes.
map(function, sequence[, sequence, ...])
La función map aplica una función a cada elemento de una secuencia y devuelve una lista con el resultado de aplicar la función a cada elemento.
Si se pasan como parámetros 'n' número de argumentos el la secuencia, la función tendrá que aceptar la misma cantidad de 'n' argumentos.

def cuadrado(dato_desde_lista_via_map):
	return (dato_desde_lista_via_map ** 2)
lista_origen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista_destino = list(map(cuadrado, lista_origen))
print("Resultado :",lista_destino)
""")
def cuadrado(dato_desde_lista_via_map):
	return (dato_desde_lista_via_map ** 2)
lista_origen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista_destino = list(map(cuadrado, lista_origen))
print("Resultado :",lista_destino)
print("""
Función map()
-------------
La función de orden superior map() aplica una función a una lista de datos
En el siguiente ejemplo la función cuadrado calcula el cuadrado de un número.
La lista_VALORES contiene una lista de datos numéricos. Con map(cuadrado, lista_VALORES) se aplica la función cuadrado a cada elemento de la lista.
""")
def cuadrado(numero):
	return numero ** 2
lista_VALORES = [-2, 4, -6, 8]
lista_CUADRADOS = list(map(cuadrado, lista_VALORES))			# Convierte a lista el iterador obtenido
print(lista_CUADRADOS)											# Muestra elementos de la lista
nuevo(24);
#################################################################
#Ejercicio_Funciones_Ej_025
print ("""
Función filter()
----------------
La función filter() aplica un filtro a una lista de datos y devuelve un iterador con los elementos que superan el filtro.
""")

def esneg(numero):						# La función verifica si un número es negativo
	return (numero < 0)					# Devuelve True/False según sea o no nº negativo
lista5 = [-3, -2, 0, 1, 9, -5]
print(list(filter(esneg, lista5)))
										# Muestra los números negativos de la lista
										# La función esneg() es llamada para comprobar,
										# uno a uno, todos los números de la lista

print(""""
filter(function, sequence)
La funcion filter verifica que los elementos de una secuencia cumplan una determinada condición, devolviendo una secuencia con los
elementos que cumplen esa condición. Es decir, para cada elemento de sequence se aplica la función function ; si el resultado es True se añade
a la lista y en caso contrario se descarta.

def es_par(n):
	return (n % 2.0 == 0)
lista_origen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista_destino = list(filter(es_par, lista_origen))
print("Resultado :",lista_destino)
""")
def es_par(n):
	return (n % 2.0 == 0)
lista_origen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista_destino = list(filter(es_par, lista_origen))
print("Resultado :",lista_destino)
nuevo(25);

#################################################################
#Ejercicio_Funciones_Ej_026
print ("""
Función reduce()
----------------
La función reduce() aplica una función a una lista de datos evaluando los elementos por pares. La primera vez se aplica al primer y segundo elemento, la siguiente, se aplicará al valor devuelto por la función junto al tercer elemento y así, sucesivamente, reduciendo la lista hasta que quede un sólo elemento.
A partir de Python 3 si queremos utilizar reduce() debemos importar el módulo functools:
""")
import functools

def multiplicar(x, y):
	print("resultado parcial",x * y) 						# muestra el resultado parcial
	return (x * y)

lista = [1, 2, 3, 4]
valor = functools.reduce(multiplicar, lista)#La primera vez se aplica al primer y segundo elemento, la siguiente, se aplicará al valor devuelto por la función junto al tercer elemento y así, sucesivamente
print("resultado final",valor)							# muestra el resultado final
nuevo(26);
#################################################################

#Ejercicio_Funciones_Ej_027
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                             Función Decorador                               ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
Función Decorador
-----------------
Es una función que recibe una función como parámetro y devuelve otra función como valor de retorno. Se utiliza cuando es necesario definir varias funciones que son muy parecidas. La función devuelta actúa como un envoltorio (wrapper) resolviendo lo que sería común a todas las funciones. También se aplica a clases.
""")
# Define decorador
def decorador(funcion):# Define función decorada
	print("\nDefine función decorada")
	def funciondecorada(*param1, **param2):
		print('\tInicio', funcion.__name__)
		funcion(*param1, **param2)
		print('\tFin', funcion.__name__)
	return funciondecorada

def suma(a, b):
	print("\t\t",a + b)
print("llamo a la función desde otra función")
suma2 = decorador(suma)
suma2(1,2)#llamo a la función desde otra función
suma3 = decorador(suma)
suma3(2,2)
print("con @")

@decorador                       # Otra forma más elegante, usando @:
def producto(arg1, arg2):
	print("\t\t",arg1 * arg2)

producto(5,5) #llamo a la función previo llamar al decorado con @
nuevo(27);
#################################################################
#Ejercicio_Funciones_Ej_028

print("""podríamos querer añadir la funcionalidad de que se imprimiera el
nombre de la función llamada por motivos de depuración:
def mi_decorador(funcion):
def nueva(*args):
print "Llamada a la funcion", funcion.__name__
retorno = funcion(*args)
return retorno
return nueva
""")


def mi_decorador(funcion):
	def nueva(*args):
		print ("Llamada a la función", funcion.__name__)
		retorno = funcion(*args)
		return retorno
	return nueva
mi_decorador(producto)(5,5)

nuevo(28);
#################################################################
#Ejercicio_Funciones_Ej_029
print("# El siguiente decorador genera tablas de sumas y multiplicaciones. El código que es común a todas las funciones se declara en la función 'envoltura':")
def tablas(funcion):
	def envoltura(tabla=1):
		print('Tabla del %i:' %tabla)
		print('-' * 15)
		for numero in range(0, 11):
			funcion(numero, tabla)
		print('-' * 15)
	return envoltura

@tablas
def suma(numero, tabla=1):
	print('%2i + %2i = %3i' %(tabla, numero, tabla+numero))

@tablas
def multiplicar(numero, tabla=1):
	print('%2i X %2i = %3i' %(tabla, numero, tabla*numero))

# Muestra la tabla de sumar del 1
suma()

# Muestra la tabla de sumar del 4
suma(4)

# Muestra la tabla de multiplicar del 1
multiplicar()

# Muestra la tabla de multiplicar del 10
multiplicar(10)
nuevo(29,"fin")
#Ejercicio_Funciones_Ej_011
def area_triangulo(base, altura):  					# define función con dos parámetros
	print(" Calcular el área de un triangulo ")  		# cadena de documentación
	resultado = base * altura / 2
	return (resultado)		 						# devuelve el resultado de la expresión
def salida_x_pantalla(calculo,base,altura):
	print(f"Dado los valores Base = {base} y altura = {altura} \nEl resultado es "+ str(calculo) +" cm^2")
#1er ej
print ("funcion unica")
calculo = area_triangulo(6, 4)						# la función retornará el valor 12
print("Dado los valores Base = 6 y altura = 4 \nEl resultado es "+ str(calculo) +" cm^2")
print("Funcion anillada")
#           =        con funcion anillada
salida_x_pantalla(area_triangulo(6, 4),6,4)						# la función retornará el valor 12
#2do ej
print ("funcion unica")
calculo = area_triangulo(3.5, 2.4)					# la función retornará el valor 4.2
print("Dado los valores Base = 3,5 y altura = 2.4 \nEl resultado es "+ str(calculo) +" cm^2")
print("funcion anillada")
#           =        con funcion anillada
salida_x_pantalla(area_triangulo(3.5, 2.4),3.5,2.4)						# la función retornará el valor 12
#3er ej
print ("funcion unica")
dato_salida_1=int(input("Ingrese el 1º valor Base: "))
dato_salida_2=int(input("Ingrese el 2º valor Altura: "))
calculo = area_triangulo(dato_salida_1, dato_salida_2)
print(f"Dado los valores Base = {dato_salida_1} y altura = {dato_salida_2} \nEl resultado es "+ str(calculo) +" cm^2")
print("funcion anillada")
#           =        con funcion anillada
salida_x_pantalla(area_triangulo(dato_salida_1, dato_salida_2),dato_salida_1, dato_salida_2)						# la función retornará el valor 12


nuevo(11);
