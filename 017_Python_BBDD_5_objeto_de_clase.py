from Estructura import *

def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                   Bases de Datos                            ║
║                                                                             ║
║                              libreria mysql.connector                       ║
║              https://dev.mysql.com/downloads/connector/python/              ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                              Create Database                                ║
║                              Create Table                                   ║
║                              Insert                                         ║
║                              Select                                         ║
║                              Where                                          ║
║                              Order By                                       ║
║                              Delete                                         ║
║                              Drop Table                                     ║
║                              Update                                         ║
║                              Limit                                          ║
║                              Join                                           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")
#################################################################

#Clase_BBDD_01
print ("Se debe instalar MySQLdb")
import mysql.connector
import datetime

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Este tema llevara un ejercicio que permita recorrer varias acciones con MySQL");
print ("Usa una funcion es especial para llamarla y conectarte cada vez que lo necesites");
print ("Pada cada item genera una funcion que solucione lo requerido.");
print ("	A)Genera el conector con variables");
print ("	B)Necesitando base de datos 'Alumnos', si existe borramos la anterior, luego creamos la nueva");
print ("	C)Genera dentro una tabla para 10 index-automatico, alumnos-Nombres(20), apellidos(20), edada, nota_bimestre_1, nota_bimestre_2 (0 a 10), nota_bimestre_3 (0 a 10), nota_bimestre_4 (0 a 10), nota_promedio (0 a 10), paso_de_grado (true/False)");
print ("	D)Ingresamos los Nombres y apellidos de los alumnos con un bucle y los grabamos en la base" );
print ("	E)Listalos en orden alfabetico");
print ("	F)Un alumno pide el pase y se van, borralo de la tabla.");
print ("	G)Al crearce una vacante ingresa un alumno incertalo con sus notas de la tabla.");
print ("	H)Pide las notas y cargalas");
print ("	I)Calcula el promedio, calcula si pasa de grado, ingresa los datos ");
print ("	J)Listamos los alumnos que tienen un promedio mayor o igual que 7 y los que son menor a 7 por separado - where" );
print ("	K)Hay un alumno cuyas notaa estan equivocadas, Ingresa el nombre y las notas de cada bimestre, busca el alumno y actualiza las notas, promedio y paso de grado");
