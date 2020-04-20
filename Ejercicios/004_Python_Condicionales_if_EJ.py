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
║                        Condicionales    if else elif                        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
nuevo(0,"inicio");
#################################################################
#Practica_Condicional_Ej_01
print("""
Dada 4 notas (una variable por cada bimestre).
Sumalas y si el promedio es:
	entre 0 y <4 recursa directamente
	entre >=4 y <6 reprueba y va a diciembre
	entre >=6 y <7 oral para saber que se hace
	entre >=7 y <9 aprobado
	entre >9 y <=10 aprobado con honores
""")
nuevo(1);
#################################################################
#Practica_Condicional_Ej_02
print("""
Dada 4 notas (una variable por cada bimestre).
si cada variable es <0 o >10 error en la carga de datos
	entre 0 y <4 recursa directamente
	entre >=4 y <6 reprueba y va a diciembre
	entre >=6 y <7 oral para saber que se hace
	entre >=7 y <9 aprobado	
	entre >9 y <=10 aprobado con honores
	chequea que parcial debe recuperar o si pasa.
	calcula el promedio y haz lo mismo con las notas del promedio
""")
nuevo(2);
#################################################################n);
#Practica_Condicional_Ej_3
print("""
Ingresa 2 datos. Si su promedio NO es >= a 7 imprime No Alcanzo los objetivos
de lo contrario imprimir que paso a la siguiente etapa
""")
nuevo(3);
#################################################################;
#Practica_Condicional_Ej_4
print("""
A partir de una lista de 10 alumnos ["Juan","Ana","Laura","Pedro","Ines","Raul","Sandra","Andres","Pablo","Mabel"]
ingresa el nombre y compara si este esta en la lista 
	Dato(if nombre in lista)
""")
nuevo(4);
#################################################################
#Practica_Condicional_Ej_5
print("""
A partir de una lista de 10 alumnos ["Juan","Ana","Laura","Pedro","Ines","Raul","Sandra","Andres","Pablo","Mabel"]
ingresa el nombre y compara si esta NO esta en la lista 
	Dato (if nombre not in lista)
""")
nuevo(5);
#################################################################
#Practica_Condicional_Ej_6
print("""
Ingresa un dato:
Chequea si es != a 0 (cero)
Sino coloca si es par o impar 
	Dato (if var % 2 == 0:)
""")
nuevo(6);
#################################################################din);
#Practica_Condicional_Ej_7
print("""
Genera en la funcion principal con print un menu donde las opciones sea Archivo, Editar, Buscar, Configurar y Help
Ingresa la primer letra e imprime un submenu para cada una de estas opciones 
		Archivo		-> Abrir, Guardar, Cerrar, Salir
		Editar		-> Copiar, Xcortar, Pegar, Seleccionar Todo
		Buscar		-> Adelante, Z-atras, Todo el documento, Reemplazar
		Configurar	-> Idioma, Pagina, Dicionario, S_pantalla
		Help		-> Menu, Sitio, Wiky, Fallos
Consulta el submenu en cada funcion y regresa el valor elegido a la funcion principal. Imprimir la opcion final Ej Archivo-->Guardar
""")
nuevo(7);
#################################################################
#Practica_Condicional_Ej_8
print("""
Ingresa un dato_1er_jugador solo debe ser Roca (1), Papel(2) o Tijera(3)
dato_2do_jugador ==  random.randint(1, 3)
	dato (import random)
dato_1er_jugador == dato_2do_jugador imprime empate
dato_1er_jugador == 1 y dato_2do_jugador == 2 imprime gano jugador 2
dato_1er_jugador == 1 y dato_2do_jugador == 3 imprime gano jugador 1
dato_1er_jugador == 2 y dato_2do_jugador == 1 imprime gano jugador 1
dato_1er_jugador == 2 y dato_2do_jugador == 3 imprime gano jugador 2
dato_1er_jugador == 3 y dato_2do_jugador == 1 imprime gano jugador 2
dato_1er_jugador == 3 y dato_2do_jugador == 2 imprime gano jugador 1
""")
nuevo(8);
#################################################################
