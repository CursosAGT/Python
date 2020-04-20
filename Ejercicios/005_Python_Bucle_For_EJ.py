from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aquí las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                               Guia de ejercicios                            ║
║                                                                             ║
║                                 Bucles // for                               ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                 range (rango)                               ║
╚═════════════════════════════════════════════════════════════════════════════╝
for i in range(10):<------------recordar los dos puntos ':'
Range - rango   ╚════════  10 h, sin otro dato empieza en 0 y termina en 9

for i in range(5,20):<------------recordar los dos puntos ':'
			   ║  ╚════════ 20 valor final termina en 19
			   ╚═══════════ 5 valor inicial empieza 5

for i in range(3,300,10):
				║  ║   ═════ Step incremento 10, ira de 10 en 10
				║  ╚════════ 300 valor final termina en 293
				╚═══════════ 3 valor inicial empieza 3

""");
nuevo(0,"inicio");
#################################################################
#Practica_For_Ej_01

print("""
Dada una variable alumnos que inicia con el valor 0 (cero).
Una clase de 20 Chicos
*	Ingresa nota de los 4 bimestes.
*	Imprime el promedio de cada alumno.
""")
nuevo(1);
#################################################################
#Practica_For_Ej_02
print("""
Dada una variable alumnos que inicia con el valor 0 (cero).
Una clase de 20 Chicos.
*	Ingresa nota de los 4 bimestes.
*	Imprime el promedio de cada alumno.
*	haz un contador que sume todo los promedios de todos los alumnos y al final imprime el promedio final de cada aula.
""")
nuevo(2);
#################################################################
#Practica_For_Ej_03
print("""
Dada una variable alumnos que inicia con el valor 0 (cero).
consulta la cantidad de alumnos y guardala en la variable Cant_alumnos
*	Ingresa nota de los 4 bimestes para cada alumno.
*	Imprime el promedio de cada alumno.
*	haz un contador que sume todos los promedios de cada bimestre para cada alumno
*	haz un contador que sume todos los promedios de cada alumno para sacar el promedio anual.
*	Al final imprime los promedios bimestrales y el promedio anual de cada aula.
""")
nuevo(3);
#################################################################
#Practica_For_Ej_04
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                   Bucles // for                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                        Array:  limites no numéricos                         ║
╚═════════════════════════════════════════════════════════════════════════════╝
for i in [1,2,3,4,5]:<------------recordar los dos puntos ':'
lista         ╚════════  5 valores ordenados

for i in [6,2,5,4,8]:<------------recordar los dos puntos ':'
lista         ╚════════  5 valores sin orden

for i in ["Nombre_1","Nombre_2","Nombre_3","Nombre_4"]:<-recordar los dos puntos ':'
lista         ╚════════  lista[], tupla (), etc

lista = ["Nombre_1","Nombre_2","Nombre_3","Nombre_4"]
for i in lista:
lista         ╚════════  lista[], tupla (), etc

Nombre_diccionario_1 = {"clave 1":"dato_asociado 1","clave 2":"dato_asociado 2","clave 3":"dato_asociado 3","clave 4":"dato_asociado 4","clave 5":"dato_asociado 5","clave 6":"dato_asociado 6","clave 7":"dato_asociado 7","clave 8":"dato_asociado 8","clave 9":"dato_asociado 9","clave 10":"dato_asociado 10"}
for K,V in Nombre_diccionario_1.items():
               ╚════════  diccionario
""");
print("""
En cada mes hay una cantidad distinta de dias,
Genera una lista de esta cantidad de dias [31,28,31,30,31,30,31,31,30,31,30,31]
*	Recorre esta lista con un bucle. 
*	Consulta las horas trabajadas por mes(20 dias laborables x 8 hs = +- 160 hs mensuales).
*	Imprime este promedio diario
*	Suma los promedio diario de cada mes e imprime al final el promedio de horas diarias trabajadas por an-io.

""")
nuevo(4);
#################################################################
#Practica_For_Ej_05
print("""
Nombre_diccionario_1 = {"clave 1":"dato_asociado 1","clave 2":"dato_asociado 2","clave 3":"dato_asociado 3","clave 4":"dato_asociado 4","clave 5":"dato_asociado 5","clave 6":"dato_asociado 6","clave 7":"dato_asociado 7","clave 8":"dato_asociado 8","clave 9":"dato_asociado 9","clave 10":"dato_asociado 10"}
for K,V in Nombre_diccionario_1.items():
               ╚════════  diccionario

En cada mes hay una cantidad distinta de dias,
Genera una diccionario de estos datos ["Enero":31,"Febrero":28,"Marzo":31,"Abril":30,"Mayo":31,"Junio":30,"Julio":31,"Agosto":31,"Septiembre":30,"Octubre":31,"Nobiembre":30,"Diciembre":31]

*	Recorre este diccionario con un bucle. Asigna una variable al primer valor Clave = Mes_Nombre y otra al valor Mes_cant_dias
*	Consulta las horas trabajadas imprimiendo a que mes corresponde(clave del diccionario) por mes(20 dias laborables x 8 hs = +- 160 hs mensiales).
*	Imprime este promedio diario y a que mes corresponde.
*	Suma los promedio diario de cada mes e imprime al final el promedio de horas diarias trabajadas por an-io.
""")
nuevo(5);
#################################################################
#Practica_For_Ej_06
print("""
Imprime una tabla pitagórica usando un bucle
_| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
0| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
1| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
2| 0 | 2 | 4 | 6 | 8 |10 |12 |14 |16 |18 |
3| 0 | 3 | 6 | 9 |12 |15 |18 |21 |24 |27 |
4| 0 | 4 | 8 |12 |16 |20 |24 |28 |32 |36 |
5| 0 | 5 |10 |15 |20 |25 |30 |35 |40 |45 |
6| 0 | 6 |12 |18 |24 |30 |36 |42 |48 |54 |
7| 0 | 7 |14 |21 |28 |35 |42 |49 |56 |63 |
8| 0 | 8 |16 |24 |32 |40 |48 |56 |64 |72 |
9| 0 | 9 |18 |27 |36 |45 |54 |63 |72 |81 |

concepto:
	bucle para tabla entre 0 a 10
		imprimir ( tabla * 0 ,"|",tabla * 1 ,"|",tabla * 2 ..............,"|",tabla * 9 ,"|") 
""")
nuevo(6);
#################################################################
#Practica_For_Ej_07
print("""
Imprime una tabla pitagórica usando dos bucles anillados
concepto:
	bucle para fila entre 0 a 10
		bucle para columna entre 0 a 10
			imprimir ( fila * columna ,end="|");<--el end elimina el linea abajo - enter y lo reemplaza por "|"
		imprime una linea vacia entre la salida de un bucle y el siguiente("") 
""")
nuevo(7);
#################################################################
#Practica_For_Ej_08
print("""
Recorrer una lista
A partir de una lista de 10 alumnos ["Juan","Ana","Laura","Pedro","Ines","Raul","Sandra","Andres","Pablo","Mabel"]
ingresa el nombre y genera un diccionario con la edad mediante un bucle.
""")
nuevo(8);
#################################################################
#Practica_For_Ej_09
print ("""
Recorrer un string
Pide que ingresen un mail en una variable string
Verificar consultando caracter por caracter de esta variable si tiene @ y como minimo un punto.
Imprime si es correcto o no
""");
nuevo(9);
#################################################################
#Practica_For_Ej_10
print ("""
Bucle invertido
Pide que ingresen la cantidad de datos a chequear
Inicia un bucle desde el valor final al inicial con un step -1
En cada iteraccion ingresa un valor.
Guarda en una variable el valor_mayor y el valor_menor.
al final del bucle imprime estos valores
"""); 
nuevo(10);
