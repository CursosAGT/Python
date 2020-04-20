from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║            * Tipos de variables                                             ║
║            * Procesamiento de cadenas                                       ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                                                             ║
║                                    Variables                                ║
║                            -----------------------                          ║
║                                                                             ║
║                           tipos de variables                                ║
║                                               Mutable                       ║
║                                               Inmutable                     ║
║                                                                             ║
║                                               Intenger                      ║
║                                               Float                         ║
║                                               Complex                       ║
║                                               Booleans                      ║
║                                                                             ║
║                                               String                        ║
║                                               List                          ║
║                                               Tuple                         ║
║                                               Set                           ║
║                                               Dictionary                    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
pausa();limpiar();
print("""
Mutable: su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.
Inmutable: su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.

Categoría de tipo________Nombre______Descripción"
Números inmutables_______int_________entero"
_________________________long________entero largo"
_________________________float_______coma flotante"
_________________________complex_____complejo"
_________________________bool________booleano True / False"
Secuencias inmutables____str_________cadena de caracteres"
_________________________unicode_____cadena de caracteres Unicode"
_________________________tuple_______tupla"
_________________________xrange______rango inmutable"
Secuencias mutables______list________lista"
_________________________range_______rango mutable"
Mapeosprint______________dict________diccionario"
Conjuntos mutables_______set_________conjunto mutable"
Conjuntos inmutables_____frozenset___Conjunto inmutable"
""");
pausa();limpiar();
print("""
\nhttp://docs.python.org.ar/tutorial/3/classes.html"
\n Objeto, es su materialización de algo incluso un dato"
\n Clase, es el razonamiento abstracto de un objeto"
\n Instanciar, es crear objetos desde una clase"
\n Las clases en este contexto permiten definir los atributos y el comportamiento, mediante métodos, de los objetos de un programa. Una clase es una especie de plantilla o prototipo que se utiliza para crear instancias individuales del mismo tipo de objeto."
\n Los atributos definen las características propias del objeto y modifican su estado. Son datos asociados a las clases y a los objetos creados a partir de ellas."
\n De ello, se deducen los dos tipos de atributos o de variables existentes: variables de clase y variables de instancia (objetos)."
\n Los métodos son bloques de código (o funciones) de una clase que se utilizan para definir el comportamiento de los objetos."
\n Tanto para acceder a los atributos como para llamar a los métodos se utiliza el método denominado de notación de punto que se basa en escribir el nombre del objeto o de la clase seguido de un punto y el nombre del atributo o del método con los argumentos que procedan: clase.atributo, objeto.atributo, objeto.método([argumentos])."
\n
\n Una variable de clase es compartida por todas las instancias de una clase. Se definen dentro de la clase (después del encabezado de la clase) pero nunca dentro de un método. Este tipo de variables no se utilizan con tanta frecuencia como las variables de instancia."
\n Una variable de instancia se define dentro de un método y pertenece a un objeto determinado de la clase instanciada.
""");
nuevo(0);
#################################################################
#Ej_Variables_01

print("""
#Accede a la consola
#	En windows ve con la tecla de windows mas R alli ejecuta cmr(intro)
#		Te aparecera la pantalla donde deberas ejecutar py (intro)
#			debera aparecer '	'esperando que ingreses tu comando python
#	En Linux ve al menu consola
#		Te aparecera la pantalla donde deberas ejecutar python3 (intro)
#			debera aparecer '	'esperando que ingreses tu comando python
#	En Mac ve al menu consola
#		Te aparecera la pantalla donde deberas ejecutar python3 (intro)
#			debera aparecer '	'esperando que ingreses tu comando python
#		""")
nuevo(1);
#################################################################
#Ej_Variables_002
print("""
#Las variables en python son objetos con nombres de fantasia que ponemos a un espacio en memoria. En este espacio guardaremos datos
#En este caso usaremos datos numericos enteros.
	variable_A = 100
	variable_B = 50
	variable_C = 20
#Estos datos podran ser manipulados para obtener un resultado.
	print (variable_A)
	print (variable_B)
	print (variable_C)
	print (variable_A + variable_B + variable_C)
#Podemos crear una variable que guarde el resultado de la operacion con las variables anteriores
	resultado = (variable_A + variable_B + variable_C)
	print (resultado)
#Para mejorar la salida de datos y darle una idea mas coprencible escribamos
	print ("El resultado es :", format(resultado), " metodo uno")
	print ("El resultado es :", str(resultado), " metodo dos")
	print (f"El resultado es : {resultado} metodo tres")
""");
nuevo(2);
#################################################################
#Ej_Variables_003
print("""
#Otra forma de colocar datos en memoria y darles un nombre defantasia
	variable_A,	variable_B,	variable_C = 100,50,20

	print (variable_A)
	print (variable_B)
	print (variable_C)
#           o
	print (variable_A + variable_B + variable_C)
#Podemos crear una variable que guarde el resultado de la operacion con las variables anteriores
	resultado = (variable_A + variable_B + variable_C)
	print (resultado)
""");
nuevo(3);
#################################################################
#Ej_Variables_004
print("""
#Has un ejercicio con cada operador 
	variable_A = 100
	variable_B = 50
	variable_C = 20
#Estos datos podran ser manipulados para obtener un resultado.
	print (variable_A)
	print (variable_B)
	print (variable_A + variable_B )
#                     ^ 
#                     |
#                     operador

#			+ 	Suma 				variable_A + variable_B
#			- 	Resta 				variable_A - variable_B
#			* 	Multiplicación 		variable_A * variable_B
#			** 	Exponente 			variable_A ** variable_B
#			/ 	División 			variable_A / variable_B
#			// 	División entera 	variable_A // variable_B
#			% 	Módulo 				variable_A % variable_B2
""");
nuevo(4);
#################################################################
#Ej_Variables_005
print("""
╔══════════════════════════╦══════════════════════════╦══════════════════════════╗
║                          ║                          ║                          ║ 
║    + Suma                ║         a += b           ║           a = a + b      ║
║    - Resta               ║         a -= b           ║           a = a - b      ║
║    * Multiplicación      ║         a *= b           ║           a = a * b      ║
║    ** Exponente          ║         a **= b          ║           a = a ** b     ║
║    / División            ║         a /= b           ║           a = a / b      ║
║    // División entera    ║         a //= b          ║           a = a // b     ║
║    % Módulo              ║         a %= b           ║           a = a % b      ║
║                          ║                          ║                          ║
╚══════════════════════════╩══════════════════════════╩══════════════════════════╝
""");
nuevo(5);
#################################################################
#Ej_Variables_006
print("""
#Ahora veremos que hay varios tipos de datos que debemos guardar en memoria para manipular sus valores. 
#Estos objetos,variables, solo guardan un dato en memoria bajo un mismo nombre de fantasia  
#Distintos tipos de datos utilizan distintos tipos de objetos - variables
#Type me muestra el tipo de dato guardado en la porcion de memoria asociado al momre de fantacia que elijamos
#En python los valores que ingresamos vajo un nombre de fantasia 
	variable = 100
	print(variable)
	print(type(variable))
#vemos que python me dice que es de la clase 'int' Numerica entera

#################################################################
	variable = 99.999
	print(variable)
	print(type(variable))
#vemos que python me dice que es de la clase 'float' Numerica decimal - punto flotante

#################################################################
	variable = True
	print(variable)
	print(type(variable))
#vemos que python me dice que es de la clase 'bool' Booleana - Solo admite valores 'True' o 'False'

#################################################################
	variable = 3.14159 + 99j
	print(variable)
	print(type(variable))
#vemos que python me dice que es de la clase 'complex' Complejos - Son los números que tienen una parte real y una imaginaria
""");
nuevo(6);
#################################################################
#Ej_Variables_007
print("""
#################################################################
#Ahora veremos como guardamos en memoria no solo un dato sino un conjunto de estos bajo un solo nombre de fantasia.
	variable = "Hola"
	print(variable)
	print(type(variable))
#vemos que python me dice que es de la clase 'str' String- cadena de caracteres
#Reemplasa las dobles comillas " por comillas simples '
	variable = 'Hola'
	print(variable)
	print(type(variable))
#Vemos que obtenemos el mismo resultado peroo ten en cuenta que en ingles suele usarse el apostrofo en un texto It's a cat y daria un dolor de cabeza
#Reemplasa las  comillas " o ' por tres 3 seguidas del mismo tipo " " " o ''' y agrega algun tecto en varias lineas
	variable = '''Hola
como va la vida???
Arriba que esto es facil'''
	print(variable)
	print(type(variable))
""");
nuevo(7);
#################################################################
#Ej_Variables_008
print("""
#################################################################
#Otro ejemplos que se explicaran mas adelante. Solo copialos y ve el resultado. En unas clases nos seran muy utiles

	conjunto = [0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0]
	print(conjunto)
	print(type(conjunto))
#vemos que python me dice que es de la clase 'list' Una Lista de datos todos en memoria separados por , comas

#################################################################
	conjunto = (0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0)
	print(conjunto)
	print(type(conjunto))
#vemos que python me dice que es de la clase 'tupla' Una Tupla de datos todos en memoria separados por , comas

#################################################################
	conjunto = {0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0}
	print(conjunto)
#Ve que ocurre con los datos repetidos
	print(type(conjunto))
#vemos que python me dice que es de la clase 'set' Un set de datos todos en memoria separados por , comas

#################################################################
	conjunto = {"A":"1","B":"2","C":"3","D":"4"}
	print(conjunto)
	print(type(conjunto))
#vemos que python me dice que es de la clase 'Dic' Un Diccionario de pares de datos todos en memoria separados por : y , comas
""");
nuevo(8);
#################################################################
#Ej_Variables_008
print("""
#prueba con este
	paices_America = {AntiguaYBarbuda":"SaintJohn's","Argentina":"BuenosAires","Bahamas":"Nasáu","Barbados":"Bridgetown","Belice":"Belmopán","Bolivia":"Sucre","Brasil":"Brasilia","Canadá":"Ottawa","Chile":"SantiagodeChile","Colombia":"Bogotá","CostaRica":"SanJosé","Cuba":"LaHabana","Dominica":"Roseau","Ecuador":"Quito","ElSalvador":"SanSalvador","EstadosUnidos":"WashingtonD.C.","Granada":"SaintGeorge","Guatemala":"CiudaddeGuatemala","Guyana":"Georgetown","Haití":"PuertoPríncipe","Honduras":"Tegucigalpa","Jamaica":"Kingston","México":"CiudaddeMéxico","Nicaragua":"Managua","Panamá":"Panamá","Paraguay":"Asunción","Perú":"Lima","RepúblicaDominicana":"SantoDomingo","SanCristóbalyNieves":"Basseterre","SanVicenteylasGranadinas":"Kingstown","SantaLucía":"Castries","Surinam":"Paramaribo","TrinidadyTobago":"PuertoEspaña","Uruguay":"Montevideo","Venezuela":"Caracas"}
	print(paices_America)

#################################################################
""");
nuevo(9);
#################################################################
#Ej_Variables_009
print("""
#Juguemos un rato 
	conjunto = "Hola, Como va la practica??"
	print(conjunto)
	print(type(conjunto))
#Esto ya lo vimos, es una cadena de caracteres 'str'
	print(conjunto[0])
#                  ^
#                  |
#                  Ubicacion del caracter

	print(conjunto[1])
	print(conjunto[2])
	print(conjunto[3])
	print(conjunto[6:])
#                  ^ 
#                  | 
#                  Inicio hasta el fin
#
	print(conjunto[:4])
#                   ^
#                   |
#                   Fin desde el inicio [0]
#
	print(conjunto[0:4])
	print(conjunto[6:14])
#                  ^  ^
#                  |  Fin
#                  Inicio
#
""");
nuevo(10);
#################################################################
#Ej_Variables_010
print("""
	variable_A = 100
	variable_B = 50
	variable_C = 20+30
#Estos datos podran ser manipulados para obtener un resultado.
	print (variable_A==variable_B)
	print (variable_B==variable_C)
	print (variable_A==variable_C*2)

#Juguemos un rato 
	conjunto = [0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0]
	incognita = 9
	print("esta incognita en conjunto : ",incognita in conjunto)

	conjunto = "Hola, Como va la practica??"
	incognita ="va"
	print("esta incognita en conjunto : ",incognita in conjunto)
""");
nuevo(11);
#################################################################
#Ej_Variables_011
from collections import Counter#IMPORTAR <------------------------------------luego veremos esto en profundidad
conjunto = [0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0,2,3,3,4,4,4,5,5,5,5]
print(conjunto)
print(Counter(conjunto))

nuevo(12);
#################################################################
#Ej_Variables_012

#Algunas formas de utilizar un contador, sus métodos y conversiones:

animales = "gato perro canario perro canario perro"
dato = Counter(animales.split())
print(animales)
print(dato) 
print(dato.most_common(1))  # Primeros elemento más repetido
print(dato.most_common(2))  # Primeros dos elementos más repetidos
print(dato.most_common())   # Elementos ordenadores por repeticiones
print("Cambia y coloca mas datos repetidos o no")
nuevo(13);
#################################################################
#Ej_Variables_14

conjunto = [0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0,2,3,3,4,4,4,5,5,5,5]
print(conjunto)
contador=Counter(conjunto)
print(contador.items())    # Registros del contador por clave-valor
print("Cambia y coloca mas datos repetidos o no")

nuevo(14);
#################################################################
#Ej_Variables_015
dato ="Ariel";
dato_salida_1, dato_salida_2, dato_salida_3, dato_salida_4=1973,"SEPTIEMBRE",True,1.78;
print (f"Soy {dato}, Naci en {dato_salida_1} en {dato_salida_2} llegue a medir {dato_salida_4} y sigo trabajando : {dato_salida_3}");
print("Cambia y pon tus datos")
nuevo(15);
#################################################################
#Ej_Variables_016
array="OK! Practica Variables";
dato_salida_1,dato_salida_2,dato_salida_3,*dato_salida_4=array;
print(f"dato 1 {dato_salida_1} un dato - una variable")
print(f"dato 2 {dato_salida_2} un dato - una variable")
print(f"dato 3 {dato_salida_3} un dato - una variable")
print(f"datos 4 {dato_salida_4} un array de datos - una lista")
nuevo(16,"fin");
#################################################################
