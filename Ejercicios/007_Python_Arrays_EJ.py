from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                  Unidad 4 - Listas, Tuplas y Diccionarios   ║
║              Listas                                                         ║
║                 * Índices                                                   ║
║                 * Recorrer listas                                           ║
║              Tuplas                                                         ║
║                 * Índices                                                   ║
║                 * Recorrer Tuplas                                           ║
║              Diccionarios                                                   ║
║                 * Funcionamiento de diccionarios                            ║
║                 * Estructuras tipo JSON                                     ║
║              Set                                                            ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                           Python List/Array Methods                         ║
║                          ---------------------------                        ║
║                                                                             ║
║          Method    Description                                              ║
║                                                                             ║
║          append()  Adds an element at the end of the list                   ║
║          clear()   Removes all the elements from the list                   ║
║          copy()    Returns a copy of the list                               ║
║          count()   Returns the number of elements with the specified value  ║
║          extend()  Add the elements of a list (or any iterable);, to the end ║
║                    of the current list                                      ║
║          index()   Returns the index of the first element with the specified║
║                    value                                                    ║
║          insert()  Adds an element at the specified position                ║
║          pop()     Removes the element at the specified position            ║
║          remove()  Removes the first item with the specified value          ║
║          reverse() Reverses the order of the list                           ║
║          sort()    Sorts the list                                           ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                    Listas                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

""");
pausa();limpiar();
nuevo(0,"inicio");
#################################################################
#Ej_Arrays_Ej_001
print('Array Nombres = "Juan,"Juana","Andrea","Andres","Martin","Martina","Joaquin","Julia","Julio","Facundo"');
print("Ingresa un nombre, ponlo en capitalize ");
print ("Busco si el dato 'nombre' esta en mi Array con print");
print ('print("Nombre" in Nombres);');
nuevo(1);
#################################################################
#Ej_Arrays_Ej_002
print("Modifica el anterior:");
print("Busco si el dato 'nombre' esta en mi Array con print");
print("Ubicar la posicion de 'Nombre' en el index" );
print('print(Nombres.index("Nombre");');
print("Muestra en pantalla");
nuevo(2);

#################################################################
#Ej_Arrays_Ej_003
print("Modifica el anterior:");
print("Ingresa un nombre, ponlo en capitalize ");
print("remuevelo del array");
print('Nombres.remove("Nombre");');
print("Muestra en pantalla");
nuevo(3);

#################################################################
#Ej_Arrays_Ej_004
print("Modifica el anterior:");
print("Busco si el dato 'nombre' esta en mi Array con if");
print("si no se encuentra ponlo al final");
print("Muestra en pantalla");
nuevo(4);
#################################################################
#Ej_Arrays_Ej_005
print("Modifica el anterior:");
print("Ordena el array alfabeticamente");
print("Muestra en pantalla");
nuevo(5);

#################################################################
#Ej_Arrays_Ej_006
print("Modifica el anterior:");
print("Ordena el array alfabeticamente");
print("Verifica si hay iguales");
print("Muestra en pantalla");
nuevo(6);

#################################################################
#Ej_Arrays_Ej_007
print ("""

Función map()
-------------
La función de orden superior map() aplica una función a una lista de datos y devuelve un iterador que contiene todos los resultados para los elementos de la lista.
En el siguiente ejemplo la función cuadrado calcula el cuadrado de un número.
La lista_VALORES contiene una lista de datos numéricos. Con map(cuadrado, lista_VALORES); se aplica la función cuadrado a cada elemento de la lista.
""");
"""
Ejemplo


def cuadrado(numero);:
	return numero ** 2
lista_VALORES = [-2, 4, -6, 8]
lista_CUADRADOS = list(map(cuadrado, lista_VALORES););# Convierte a lista el iterador obtenido
print(lista_CUADRADOS);  # Muestra elementos de la lista
"""
print("Genera una array de 50 elementos con valores de {0 a 99} a partir de una funcion random (import random) - [random.randint(0, 99)]");
print("con la funcion anterior calcula el cuadrado y el cubo de cada numero del array random")
nuevo(7);

#################################################################
#Ej_Arrays_Ej_008
"""
Ejemplo:
from collections import Counter

def comparar(a,b);:
	resultado = Counter(a);==Counter(b);
	return resultado;
	
lista_base=["Juan","Pedro","Laura","Andrea"];
lista_actualizada=["Laura","Juan","Andrea","Pedro"];
lista_modificada=["JUAN","PEDRO","LAURA","ANDREA"];

regreso = comparar(lista_base, lista_actualizada);
print ("resultado de comparacion: ",regreso);

regreso = comparar(lista_base, lista_modificada);
print ("resultado de comparacion: ",regreso);
"""



print("Modifica el anterior:");
print("Genera dos array de 10 elementos con valores de {0 a 99} a partir de una funcion random (import random) - [random.randint(0, 99)]");
print("compara (from collections import Counter) ambos arrays randoms para ver cuantos resultados se repitieron ")

nuevo(8);
#################################################################
#Ej_Arrays_Ej_009
print("Modifica el anterior:");

print("Haz el mismo ejercicio 10 veces con arrays de 10, 20, 30, 40, 50, 60, 70, 80, 90 y 100 elementos ");
print("Guarda la cantidad de elementos que se repiten cada vez, saca un promedio e imprime la tabla de cantidad de repeticiones / cantidad de elementos en el array"); 
nuevo(9);

#################################################################
#Ej_Arrays_Ej_010
"""
Ejemplo:

lista = ["Alba",True,(2020,6,22);,3.1415];
dato_salida_1,dato_salida_2,dato_salida_3,dato_salida_4 = lista;

print(f" dato 1: {dato_salida_1} - dato 2: {dato_salida_2} -  dato 3: {dato_salida_3} - dato 4: {dato_salida_4} - " );
dato_salida_3_A,dato_salida_3_M,dato_salida_3_D=dato_salida_3;
print(f" dato 3 a#o: {dato_salida_3_A} - mes: {dato_salida_3_M } - dia: {dato_salida_3_D}");
"""
print("Muestra los datos de los siguientes diccionarios- Todos por separado con print(f''"); 
Beatles = {"John":"Lennon","Paul":"McCartney","George":"Harrison","Ringo":"Starr"};
Ochentas={"Jackson":"Michael","Collins":"Phil","Mercury":"Freddy","John":"Elton","Houston":"Whitney"};
Sting={"1985":"The Dream Of The Blue Turtles","1986":"Bring On The Night","1987":"Nothing Like The Sun","1988":"Nada Como El Sol","1991":"All This time","1991":"The Soul Cages","1993":"Ten Summoner's Tales","1994":"Fields of Gold: The Best of Sting 1984-1994","1996":"Mercury Falling","1997":"The Very Best Of Sting & The Police","1999":"Brand New Day","2003":"Sacred Love","2006":"Songs from the Labyrinth","2009":"If on a Winter´s Night...","2010":"Symphonicities","2013":"The Last Ship","2016":"57th & 9th","2019":"My Songs"};
print("Hay dos versiones del disco Let It Be, una de 1969 y otra de 1070, cada lado tiene temas diferentes")
Let_It_Be={"1969":{"Lado A":["One After 909","Rocker","Save the Last Dance for Me","Don't Let Me Down","Dig a Pony","I've Got a Feeling","Get Back"],"Lado B":["For You Blue","Teddy Boy","Two of Us","Maggie Mae","Dig It","Let It Be","The Long and Winding Road","Get Back<R>"]},"1970":{"Lado A":["One After 909","Rocker","Save the Last Dance for Me","Don't Let Me Down","Dig a Pony","I've Got a Feeling","Get Back","Let It Be"],"Lado B":["For You Blue","Two of Us","Maggie Mae","Dig It","The Long and Winding Road","I Me Mine","Across the Universe","Get Back<r>"]}};
print("""
haz un diccionario con los siguientes datos:
     Star Trek (James T. Kirk):
        Star Trek: La serie original (1966 - 1969)
        Star Trek: La serie animada (1973 - 1974) 

    Star Trek (Jean-Luc Picard):
        Star Trek: La Nueva Generación (1987 - 1994) 

    Spin offs:
        Star Trek: Espacio Profundo Nueve (1993 - 1999)
        Star Trek: Voyager (1995 - 2001)
        Star Trek: Enterprise (2001 - 2005)
        Star Trek: Discovery (2017 -2020)
""")
print("Imprime el diccionario de modo que quede con una estructura similar a la muestra")
nuevo(10);
#################################################################
#Ej_Arrays_Ej_011
print('Array Nombres = "Juan,"Juana","Andrea","Andres","Martin","Martina","Joaquin","Julia","Julio","Facundo"');
print("Genera un bucle que recorra el array");
print("Imprime cada dato del array Nombre.");
print("Ingresa y genera un array Apellidos donde coloques los apellidos de los Nombres ");
nuevo(11);
#################################################################
#Ej_Arrays_Ej_012
print("Modifica el anterior:");
print("Imprime juntos los valores de los Array Nombres y Apellidos ");
print("Ingresa en otro array el telefono (como string ya que lleva un - y no debe restarse);");
nuevo(12);
#################################################################
#Ej_Arrays_Ej_013
print("Modifica el anterior:");
print("junta los Array Nombres y Apellidos en un diccionario - Clave Apellido y Valor Nombre "); 
print("Graba el array en un archivo Json o pickle"); 

nuevo(13);
#################################################################
#Ej_Arrays_Ej_014
print("Modifica el anterior:");
print("Lee el archivo json o pickle");
print("Imprimelos en forma de tabla"); 
print("Genera un diccionario con clave=apellido, valor=lista de[ Nombre, Telefono=lista[casa, cel, otro], Direccion, Email[opcion mas de uno] ]"); 
print("Graba el array en un archivo Json o pickle"); 
nuevo(14);
#################################################################
#Ej_Arrays_Ej_015
print("Modifica el anterior:");
print("Lee el archivo json o pickle");
print("Genera un menu donde puedas buscar por clave o por valor - (Apellido, nombre, direccion, email); ");
nuevo(15);

#################################################################
#Ej_Arrays_Ej_016
print("Modifica el anterior:");
print("Lee el archivo json o pickle");
print("Genera un menu donde puedas buscar por clave o por valor - (Apellido, nombre, direccion, email); ");
print("Agregar Borrar, Modificar y Grabar en el archivo JSON o Pickle");
nuevo(16);

#################################################################
#Ej_Arrays_Ej_017
print("Modifica el anterior:");
print("Lee el archivo json o pickle");
print("Genera una copia de seguridad con los datos antes de modificarlos ");
print("y graba lo nuevo  en el archivo JSON o Pickle de siempre");
nuevo(17);
#################################################################
#Ej_Arrays_Ej_018
print ("""
Comprensión de listas
----------------------
Es un tipo de construcción que consta de una expresión que determina cómo modificar los elementos de una lista, seguida de una o varias clausulas for y, opcionalmente, una o varias clausulas if. El resultado que se obtiene es una lista.
""");
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Modifica el anterior:");
cubos = [valor ** 3 for valor in lista]
print("Cambia la variable cubo por una lista con 'list' ")
nuevo(18);

#################################################################
#Ej_Arrays_Ej_019
numeros = [135, 154, 180, 193, 210]
divisiblespor3 = [valor for valor in numeros if valor % 3.0 == 0]
# Muestra lista con los números divisibles por 3
print(divisiblespor3);
print("Cambia la variable divisiblespor3 por un array no modificable")



nuevo(19);

#################################################################
#Ej_Arrays_Ej_020
# Define función devuelve el inverso de un número
def funcion(x):
	result= 1/x;
	return result
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Muestra lista con inversos de cada número
print([funcion(i) for i in lista]);
print("Reemplaza la funcion 'result=1/x;' con la funcion del resto 'result = x % 2;'"); 
print("(para comprobar si es par o impar")
print("Diccionario con 'dic' uniendo la lista original y la del resultado de los restos")
nuevo(20,"fin");
