from Estructura import *
nuevo(0,"inicio");
#################################################################
import math
def Ej_ya_hechos():
	#Con tab colocaremos aquí las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                               Guia de ejercicios                            ║
║                                                                             ║
║                                  Bucles While                               ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
nuevo(0,"inicio");
#################################################################
#Practica_While_Ej_01
print("""
Dada una variable edad que inicia con el valor 0 (cero).
Una capacidad de 100 personas.
*Ingresa la edad en la entrada del boliche si es mayor a 18 años.
*Si es mayor imprime "entra", sino "que pase el siguiente".
*Al llegar a 100 cierra la puerta.
""")
nuevo(1);
#################################################################
#Practica_While_Ej_02
print("""
Dada una variable edad que inicia con el valor 0 (cero).
Una capacidad de 100 personas.
*Ingresa la edad en la entrada del boliche si es mayor a 18 años.
*consultar en la entrada del boliche si es mayor a 18 años.
*Si es mayor imprime "entra", sino "que pase el siguiente"
*Llevar un contador de los que ingresen y otro de los que no fueron aceptados
	imprimir al final el total
""")
nuevo(2);
#################################################################
#Practica_While_Ej_03
print("""
Dada una variable edad que inicia con el valor 0 (cero).
Una capacidad de 100 personas.
*Ingresa la edad en la entrada del boliche si es mayor a 18 años.
*Si es mayor imprime "entra", sino "que pase el siguiente"
*Llevar un contador de los que ingresen y otro de los que no fueron aceptados
	imprimir al final el total
*Si en el boliche hay mas de 100 personas se pide disculpas al cliente 
	No puede entrar por el momento por estar colmada la capacidad, debe esperar
""")
nuevo(3);
#################################################################
#Practica_While_Ej_04
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                               Guia de ejercicios                            ║
║                                                                             ║
║                                   while                                     ║
║                                                                             ║
║                               or , and , not                                ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
print("""
Dada una variable edad que inicia con el valor 0 (cero).
Una capacidad de 100 personas.
*Ingresa la edad en la entrada del boliche si es mayor a 18 años.
*Si ingresa 99 cierra por el dia y se hacen las estadísticas
*Si es mayor imprime "entra", sino "que pase el siguiente"
*Llevar un contador de los que ingresen y otro de los que no fueron aceptados
	imprimir al final el total
*Si en el boliche hay mas de 100 personas se pide disculpas al cliente 
	No puede entrar por el momento por estar colmada la capacidad, debe esperar
""")
nuevo(4);
#################################################################
#Practica_While_Ej_05
print("""
Dada una variable edad que inicia con el valor 0 (cero).
Una capacidad de 100 personas.
*Ingresa la edad en la entrada del boliche si es mayor a 18 años.
*Si ingresa 99 cierra por el dia y se hacen las estadísticas
*Si es mayor imprime "entra", sino "que pase el siguiente"
*Llevar un contador de los que ingresen y otro de los que no fueron aceptados
	imprimir al final el total
*Si en el boliche hay mas de 100 personas se pide disculpas al cliente 
	No puede entrar por el momento por estar colmada la capacidad, debe esperar
*Consulta si es Hombre o mujer. LLeva una estadística e imprime al final.
*Con un promedio de $1 en la mujer y de $1,5 en el hombre los viernes, sabados y domingos,
	y el 50% el resto de los días.
	LLeva una estadística e imprime al final.
*Has un bucle fijo de los 7 dias. LLeva una estadística diaria y final, imprime al final.
""")
nuevo(5);
#################################################################
#Practica_While_Ej_06
print("""
Reformula en el ejercicio anterior y en los bucles utiliza las modificaciones pedidas

Dada una variable edad que inicia con el valor 0 (cero).
Una capacidad de 100 personas.
*Ingresa la edad en la entrada del boliche si es mayor a 18 años.
*Si ingresa 99 cierra por el dia y se hacen las estadísticas
*Ingresa la edad en la entrada del boliche
	si esta en el rango >=16 años y <18 puede entrar, se cuenta pero no se le vende alcohol.(consumo promedo $0,25 para hombres y mujeres),
	>= 18 años y < 50, se cuenta y se le vende alcohol.(consumo promedo $2 para hombres y 1.75 para mujeres),
	>= 50, se cuenta y se le vende alcohol.(consumo promedo $1 para hombres y 1 para mujeres),
*Si es Hombre paga una entrada de 0.5 , la dama gratis.
*Si es mayor imprime una leyenda distinta para cada segmento.
*Llevar un contador de los ingresos, imprimir al final el total
*con un promedio de ventas antes mencionado para los viernes, sabados y domingos,
	y el 50% el resto de los días.
	LLeva una estadistica e imprime al final.
*Has un bucle fijo de una lista de "Lunes", "martes", "miercoles", "jueves", "viernes", "sabados" y "Domingo"
LLeva una estadística diaria y final, imprime al final.
""")
nuevo(6);

#################################################################
#Practica_While_Ej_07
print("""
A partir de lo visto en  ejercicio anterior
Has la estructura de ingreso a un hotel
Pregunta a cada grupo cuantas personas entran
Nuestro hotel tiene 10 habitaciones para 4 personas, 15 para 3, 20 para 2 y 10 para 1 
El costo por día en base cuadruple por persona es de $5, base triple por persona $7,base doble por persona $9 y habitación personal $12 por persona
*Lleva la estadistica y capacidad del hotel
*Si vienen cuatro personas y no quedan habitaciones cuadruples haz 2 dobles al mismo precio que una cuádruple más el 10%
*Similar en 3 personas derivando a base doble más individual
*Similar en 2 personas derivando a dos individuales
""")
nuevo(7);
#################################################################
#Practica_While_Ej_08
print("""
A partir de lo visto en  ejercicio anterior
Haz la estructura de ingreso a un hotel
Pregunta a cada grupo cuantas personas entran
Nuestro hotel tiene 10 habitaciones para 4 personas, 15 para 3, 20 para 2 y 10 para 1 
El costo por día en base cuadruple por persona es de $5, base triple por persona $7,base doble por persona $9 y habitacion personal $12 por persona
*Lleva la estadistica y capacidad del hotel
*Si vienen cuatro personas y no quedan habitaciones cuadruples haz 2 dobles al mismo precio que una cuádruple más el 10%
*Similar en 3 personas derivando a base doble más individual
*Similar en 2 personas derivando a dos individuales

consulta al entrar las personas lo siguiente
Haz un módulo por un precios base para hospedaje más desayuno, 1/2 pensión o pensión completa 
Haz un módulo por un precios base para hospedaje más pileta, spa y visitas guiadas
""")
nuevo(8);
#################################################################
#Practica_While_Ej_09
print("""
A partir de lo visto en  ejercicio anterior
Haz la estructura de ingreso a un hotel
Pregunta a cada grupo cuantas personas entran
Nuestro hotel tiene 10 habitaciones para 4 personas, 15 para 3, 20 para 2 y 10 para 1 
El costo por día en base cuadruple por persona es de $5, base triple por persona $7,base doble por persona $ 9 y habitacion personal $12 por persona
*Lleva la estadística y capacidad del hotel
*Si vienen cuatro personas y no quedan habitaciones cuadruples haz 2 dobles al mismo precio que una cuádruple más el 10%
*Similar en 3 personas derivando a base doble más individual
*Similar en 2 personas derivando a dos individuales

consulta al cliente que va ha hacer cada día mediante un bucle fijo con una lista de "Lunes", "martes", "miercoles", "jueves", "viernes", "sabados" y "Domingo"
Haz un módulo por un precios base para hospedaje más desayuno, 1/2 pensión o pensión completa 
Haz un módulo por un precios base para hospedaje más pileta, spa y visitas guiadas
""")
nuevo(9);
#################################################################
#Practica_While_Ej_10
print("""
A partir de lo visto en  ejercicio anterior
Haz la estructura de ingreso a una fábrica
Datos:
	sector (administración-10 personas, gerencia-4 personas, producción-50 personas, mantenimiento-10 personas)
	8 horas a $1, $1.5, $ 0.75 y $ 0.5 respectivamente por hora
	20 dias al mes
	horas extras por mes para cada sector (administración-1 personas, gerencia-0 personas, producción-20 personas, mantenimiento-2 personas)
haz un buble recorriendo día por día y preguntando si los operarios de cada sector se quedan a hacer horas extras
Sacar el costo de de mano de obra al final de cada mes


""")
nuevo(10);
