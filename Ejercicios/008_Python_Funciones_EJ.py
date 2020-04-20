from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass

print("""

╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                               Guia de ejercicios                            ║
║                                                                             ║                                                                             ║
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
╚═════════════════════════════════════════════════════════════════════════════╝

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
║                              Funciones con retorno                          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");


#Ejercicio_Funciones_Ej_001
print("Ingresa si la persona es de genero Masculino o Femenino(f/m);. Dependiendo del resultado llama a una funcion distinta que imprima el piso donde estan los toiletes correspondientes de que sea masculino (2do piso); o femenino(1er piso);");
nuevo(1);
#################################################################
#Ejercicio_Funciones_Ej_002
print("Ingresa I para Iniciar y llamar a una fincion, dentro de esta ingresa un nombre e imprimelo en mayusculas");
nuevo(2);
#################################################################
#Ejercicio_Funciones_Ej_003
print("Ingresa S para suma y R para restar. LLama a una funcion distinta dentro de esta pregunta los dos numeros, operalos e imprime el resultado");
nuevo(3);
#################################################################
#Ejercicio_Funciones_Ej_004
print("Modifica el anterior\nIngresa S para suma y R para restar, pregunta los dos numeros. Luego llama a la funcion suma o resta y pasale los datos (desde la funcion principla a las funciones elejida-  suma o resta);. Operalos e imprime el resultado dentro de esta ");
nuevo(4);
#################################################################
#Ejercicio_Funciones_Ej_005
print("Modifica el anterior\nIngresa S para suma y R para restar, pregunta los dos numeros. Luego llama a la funcion suma o resta y pasale los datos (desde la funcion principla a las funciones elejida-  suma o resta);. Operalos y regreda a la funcion prinsipal el resultado. Imprime el resultado dentro de la f.principal ");
nuevo(5);
#################################################################
#Ejercicio_Funciones_Ej_006
print("Ingresa 2 datos alfanumericos (Ej.usuarios, passwords, email,etc);, compara si son iguales, imprimelo");
nuevo(6);
#################################################################
#Ejercicio_Funciones_Ej_007
print("Ingresa 3 datos numericos y devuelve cual es el mayor, imprimelo");
nuevo(7);
#################################################################
#Ejercicio_Funciones_Ej_008
print("Desde el siguiente array de datos numericos, busca cual es el mayor mediante una funcion e imprimelo");
nuevo(8);
#################################################################
#Ejercicio_Funciones_Ej_009
print("En el main pide un valor de edad mediante un string. Enviala a una funcion donde chequea que el dato sea numerico y si es correcto guardala en una variable numerica, sino vuelve a pedir el dato");
nuevo(9);
#################################################################
#Ejercicio_Funciones_Ej_010
print("Dada lista=[0,87,77,35,1,32,98,56,87,36,66,32,44,3,89,55,4,2]; ordenala de mayor a menor en una funcion(sin sort); -comparar con sort");
nuevo(10);

#################################################################
#Ejercicio_Funciones
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Funciones con punteros                         ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
print("Has lo los ejercicios anteriores 6 a 10 mediante punteros");
nuevo(0);
#################################################################
#Ejercicio_Funciones_Ej_011 desde 006
print("Has lo los ejercicios anteriores 6 mediante punteros");
nuevo(11);
#################################################################
#Ejercicio_Funciones_Ej_012 desde 007
print("Has lo los ejercicios anteriores 7 mediante punteros");
nuevo(12);
#################################################################
#Ejercicio_Funciones_Ej_013 desde 008
print("Has lo los ejercicios anteriores 8 mediante punteros");
nuevo(13);
#################################################################
#Ejercicio_Funciones_Ej_014 desde 009
print("Has lo los ejercicios anteriores 9 mediante punteros");
nuevo(14);
#################################################################
#Ejercicio_Funciones_Ej_015 desde 010
print("Has lo los ejercicios anteriores 10 mediante punteros");
nuevo(10);
#################################################################
#Ejercicio_Funciones_Ej_016
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones que llama a otra función                                       ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
print("""
Genera una funcion_Inicio con print un menu donde las opciones sea Archivo, Editar, Buscar, Configurar y Help en funciones distintas
Ingresa la primer letra e imprime un submenu para cada una de estas opciones 
		Funcion_Archivo		-> Abrir, Guardar, Cerrar, Salir
		Funcion_Editar		-> Copiar, Xcortar, Pegar, Seleccionar Todo
		Funcion_Buscar		-> Adelante, Z-atras, Todo el documento, Reemplazar
		Funcion_Configurar	-> Idioma, Pagina, Dicionario, S_pantalla
		Funcion_Help		-> Menu, Sitio, Wiky, Fallos
Consulta el submenu en cada funcion y regresa el valor elegido a la funcion_Inicior. Imprimir la opcion final Ej Archivo-->Guardar
""");
nuevo(16);
#################################################################
#Ejercicio_Funciones_Ej_017 desde 16
print("""
Desde el ejercicio anterior\n Modifica usando listas Ej:Archivo=["Abrir","Guardar","Cerrar","Salir"] y demas
Utiliza la posicion de la primera letra [0] de cada lista para las condiciones de igualdad 
""");
nuevo(17);
#################################################################
#Ejercicio_Funciones_Ej_018 desde 17
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: envió de datos mediante tuplas - parámetros arbitrarios       ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
print ("""
Desde el ejercicio anterior\n Modifica usando tuplas Ej:Archivo=("Abrir","Guardar","Cerrar","Salir"); y demas
Utiliza la posicion de la primera letra [0] de cada tupla para las condiciones de igualdad 
""");
nuevo(18);
#################################################################
#Ejercicio_Funciones_Ej_019 desde 18
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: envió de datos mediante tuplas - parámetros arbitrarios       ║
║               devuelve 2 parámetros de resultado                            ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
print ("""
Desde el ejercicio anterior\n Modifica usando tuplas Ej:Archivo=("Abrir","Guardar","Cerrar","Salir"); y demas
Utiliza la posicion de la primera letra [0] de cada tupla para las condiciones de igualdad 
Devuelve los parametros menu_Inicial y SubMenu elejidos (Ej:"Archivo","Guardar");:
""");
nuevo(19);
#################################################################
#Ejercicio_Funciones_Ej_020 desde 19
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: envió de datos mediante diccionarios - parámetros clave,valor ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
print ("""
Desde el ejercicio anterior\n 
Modifica usando Diccionarios Ej: Menu={Archivo:["Abrir","Guardar","Cerrar","Salir"],"Editar":["Copiar","Xcortar","Pegar","Seleccionar Todo"],..... y demas}
Utiliza la posicion de la primera letra [0] de cada clave(en el menuInicial); y la de los valores(para los submenues); para las condiciones de igualdad. 
Devuelve los parametros menu_Inicial y SubMenu elejidos (Ej:"Archivo","Guardar");:
""");
nuevo(20);
#################################################################
#Ejercicio_Funciones_Ej_021 desde 20
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    Funciones: return con un diccionario                                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");

print ("""
Desde el ejercicio anterior\n 
Modifica usando Diccionarios Ej: Menu={Archivo:["Abrir","Guardar","Cerrar","Salir"],"Editar":["Copiar","Xcortar","Pegar","Seleccionar Todo"],..... y demas}
Utiliza la posicion de la primera letra [0] de cada clave(en el menuInicial); y la de los valores(para los submenues); para las condiciones de igualdad. 
Devuelve los parametros menu_Inicial y SubMenu elejidos en un diccionario (Ej:return {"Archivo":"Guardar"});:
""");
nuevo(21);

#################################################################
#Ejercicio_Funciones_Ej_022 desde 21
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                             Función Decorador                               ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
# Define decorador
#	@decorador                       # Otra forma más elegante, usando @:

print ("""
Agrega una funcion decoradore que genere una estructura similar al siguente ejemplo
╔═════════════════════════════════════════════════════════════════════════════╗
║   Archivo  Editar  Buscar  Configurar  Help                                 ║
╚═════════════════════════════════════════════════════════════════════════════╝
            ╔════════════════════╗
            ║ Copiar             ║
            ║ Xcortar            ║
            ║ Pegar              ║
            ║ Seleccionar Todo   ║
            ╚════════════════════╝
""");
nuevo(22, "fin");

'''
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
""");
print("""Pendiente""");

nuevo(26);
'''
