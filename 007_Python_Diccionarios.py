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
║                 Listas                                                      ║
║                      * Índices                                              ║
║                      * Recorrer listas                                      ║
║                   Tuplas                                                    ║
║                      * Índices                                              ║
║                      * Recorrer Tuplas                                      ║
║                   Diccionarios                                              ║
║                      * Funcionamiento de diccionarios                       ║
║                      * Estructuras tipo JSON                                ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                Python List/Array Methods                    ║
║                               ---------------------------                   ║
║                                                                             ║
║         Method    Description                                               ║
║                                                                             ║
║         clear()   Removes all the elements from the dictionary              ║
║         copy()    Returns a copy of the dictionary                          ║
║         fromkeys()Returns a dictionary with the specified keys and values   ║
║         get()     Returns the value of the specified key                    ║
║         items()   Returns a list containing a tuple for each key value pair ║
║         keys()    Returns a list containing the dictionary's keys           ║
║         pop()     Removes the element at the specified position             ║
║         popitem() Removes the last inserted key-value pair                  ║
║         reverse() Reverses the order of the dictionary                      ║
║         setdefault() Returns the value of the specified key. If the key     ║
║                   does not exist: insert the key, with the specified value  ║
║         update()  Updates the dictionary with the specified key-value pairs ║
║         values()  Returns a list of all the values in the dictionary        ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                      Diccionarios                           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://www.w3schools.com/python/python_ref_dictionary.asp
https://www.w3schools.com/python/python_dictionaries.asp
https://python-para-impacientes.blogspot.com/2014/01/cadenas-listas-tuplas-diccionarios-y.html


Diccionarios o matrices asociativas
Los diccionarios son objetos que contienen una lista de parejas de elementos.
De cada pareja un elemento es la clave, que no puede repetirse, y, el otro, un valor asociado.
La clave que se utiliza para acceder al valor tiene que ser un dato inmutable como una cadena,
El valor puede ser un número, una cadena, un valor lógico (True/False), una lista o una tupla.
Los pares clave-valor están separados por dos puntos, las parejas por comas y todo el conjunto se encierra entre llaves.
""");
limpiar();
#################################################################
#Ejercicio_Diccionarios_Ej_01

Nombre_diccionario_1 = {"clave 1":"dato_asociado 1","clave 2":"dato_asociado 2","clave 3":"dato_asociado 3","clave 4":"dato_asociado 4","clave 5":"dato_asociado 5","clave 6":"dato_asociado 6","clave 7":"dato_asociado 7","clave 8":"dato_asociado 8","clave 9":"dato_asociado 9","clave 10":"dato_asociado 10"}

print (Nombre_diccionario_1)
print ("clave 2  "+Nombre_diccionario_1["clave 2"])
print ("clave 6  "+Nombre_diccionario_1["clave 6"])
print ("clave 5  "+Nombre_diccionario_1["clave 5"])
print ("clave 9  "+Nombre_diccionario_1["clave 9"])
print ("clave 1  "+Nombre_diccionario_1["clave 1"])
print ("cantidad de datos en el dic",len(Nombre_diccionario_1))
print ("items",Nombre_diccionario_1.items())
print ("llaves",Nombre_diccionario_1.keys())
print ("valores",Nombre_diccionario_1.values())
nuevo(2);
#################################################################
#Ejercicio_Diccionarios_Ej_03
print("Agregar")
print (Nombre_diccionario_1)
print ("Agrego un conjunto en la posicion FINAL")
Nombre_diccionario_1["clave 11"]="dato_asociado 11"
print (Nombre_diccionario_1)

nuevo(3);
#################################################################
#Ejercicio_Diccionarios_Ej_04
print("Borrar")
print (Nombre_diccionario_1)
print ("delEteo o borro el dato 'clave 8'")
del Nombre_diccionario_1["clave 8"]
print (Nombre_diccionario_1)

nuevo(4);
#################################################################
#Ejercicio_Diccionarios_Ej_05
print("Reemplazar")
print (Nombre_diccionario_1)
print ("cambio el dato asociado a la clave 9")
Nombre_diccionario_1["clave 9"]="dato_asociado 999"
print (Nombre_diccionario_1)

nuevo(5);
#################################################################
#Ejercicio_Diccionarios_Ej_06
Nombre_tupla_1 = ["linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 1"]
Nombre_tupla_2 = ["columna 1","columna 2","columna 3","columna 4","columna 5","columna 6","columna 7","columna 8","columna 9","columna 10"]

print("de tuplas a diccionrios")
print ("valores tupla 1"+str(Nombre_tupla_1))
print ("valores tupla 2"+str(Nombre_tupla_2))
Nombre_diccionario_3 = {}
Nombre_diccionario_4 = {}
Nombre_diccionario_2 = {Nombre_tupla_1[0]:Nombre_tupla_2[0],Nombre_tupla_1[1]:Nombre_tupla_2[1],Nombre_tupla_1[2]:Nombre_tupla_2[2],Nombre_tupla_1[3]:Nombre_tupla_2[3],Nombre_tupla_1[4]:Nombre_tupla_2[4],Nombre_tupla_1[5]:Nombre_tupla_2[5],Nombre_tupla_1[6]:Nombre_tupla_2[6],Nombre_tupla_1[7]:Nombre_tupla_2[7],Nombre_tupla_1[8]:Nombre_tupla_2[8],Nombre_tupla_1[9]:Nombre_tupla_2[9]}
print ("\ndiccionario hecho a mano:\t",Nombre_diccionario_2)

#                          o
for contador in range (0,9):
	Nombre_diccionario_3[Nombre_tupla_1[contador]] = Nombre_tupla_2[contador]
print ("\ndiccionario hecho en un bucle:\t",Nombre_diccionario_3)
Nombre_diccionario_4 = dict.fromkeys(Nombre_tupla_1,Nombre_tupla_2)
print ("\ndiccionario hecho con fromkey:\t",Nombre_diccionario_4)



del Nombre_diccionario_3
nuevo(6);
#################################################################
#Ejercicio_Diccionarios_Ej_07
print("separo claves de  datos asociados ")
print ("pares de valores del diccionario 1 : "+str(Nombre_diccionario_1))
print ("Claves del diccionario 1 : "+str(Nombre_diccionario_1.keys()))
print ("Datos asociados del diccionario 1 : "+str(Nombre_diccionario_1.values()))
print ("Longitud de pares de datos del diccionario 1 : "+str(len(Nombre_diccionario_1)))
nuevo(7);
#################################################################
#Ejercicio_Diccionarios_Ej_08
diccionario = {1: ["Python", 33.2, 'UP'],
				 2: ["Java", 23.54, 'DOWN'],
				 3: ["Ruby", 17.22, 'UP'],
				 10: ["Lua", 10.55, 'DOWN'],
				 5: ["Groovy", 9.22, 'DOWN'],
				 6: ["C", 1.55, 'UP']
				 }

print ("{:<8} {:<15} {:<10} {:<10}".format('clave','Item_1','Item_2','Item_3'))
for clave_primaria, listas_valores_interiores in diccionario.items():
	Item_1, Item_2, Item_3 = listas_valores_interiores
	print ("{:<8} {:<15} {:<10} {:<10}".format(clave_primaria, Item_1, Item_2, Item_3))
nuevo(8);
#################################################################
#Ejercicio_Diccionarios_Ej_09
# input stored in variable a.
diccionario = {"nombre":"Juan", "apellido":"Perez"}
# Use of format_map() function
print("el apellido de  {nombre} es {apellido}".format_map(diccionario))
# input stored in variable a.
a = {"x":"alfa", "y":"beta"}
# Use of format_map() function
print("{x} {y}".format_map(a))
nuevo(9);
#################################################################
#Ejercicio_Diccionarios_Ej_010
Nombre_diccionario_1 = {"Primero": "wwww","Segundo":"xxxx","Tercero":"yyyy","Cuarto":"zzzz"}
for llaves in Nombre_diccionario_1:
	print("Clave : {} , Valor : {}".format(llaves,Nombre_diccionario_1[llaves]))
print ("Este diccionario contiene las siguientes claves: ", " ".join(Nombre_diccionario_1))
print ("Ordenamos por el largo del la clave ")
for llaves in sorted(Nombre_diccionario_1, key=len):
	print (llaves, Nombre_diccionario_1[llaves])
count = {}
for llaves in Nombre_diccionario_1:
	count[llaves] = count.get(llaves, 0) + 1
print (count)
del Nombre_diccionario_1
nuevo(10);
#################################################################
#Ejercicio_Diccionarios_Ej_011
Nombre_diccionario_1 = {'Abuelo_A':{'Hijos':2,'Nietos':2},
						'Abuelo_B':{'Hijos':3,'Nietos':1},
						'Abuelo_C':{'Hijos':1,'Nietos':0}
						}
for clave_primaria in Nombre_diccionario_1:
	print ("El ",clave_primaria, end="\t")
	for clave_secundaria in Nombre_diccionario_1[clave_primaria]:
		print ("tiene ",clave_secundaria,' ',Nombre_diccionario_1[clave_primaria][clave_secundaria])
		
print("--------------------------------------------------------------------------")
for clave_primaria, listas_valores_interiores in Nombre_diccionario_1.items():
	print(clave_primaria)
	for attribute, listas_valores_interiores in Nombre_diccionario_1[clave_primaria].items():
		print('\t{}\t :\t {}'.format(attribute, listas_valores_interiores))
del Nombre_diccionario_1
nuevo(11);
#################################################################
#Ejercicio_Diccionarios_Ej_012

# Input dictionary
print("transpongo el diccionario");
Nombre_diccionario_1 = {	"nombres":["Juan", "Pedro","Laura","Roxana","Alberto"],
							"profesion":["Astronauta", "Biologo","Quimica","Fisica","Cocinero"],
							"edad":[33, 55, 45, 25, 32] };

print(" Uso de la funcion format_map()");
print("{nombres[0]} trabaja de {profesion[0]} y tiene {edad[0]} años.".format_map(Nombre_diccionario_1));
print("{nombres[1]} trabaja de {profesion[1]} y tiene {edad[1]} años.".format_map(Nombre_diccionario_1));
print("{nombres[2]} trabaja de {profesion[2]} y tiene {edad[2]} años.".format_map(Nombre_diccionario_1));
print("{nombres[3]} trabaja de {profesion[3]} y tiene {edad[3]} años.".format_map(Nombre_diccionario_1));
print("{nombres[4]} trabaja de {profesion[4]} y tiene {edad[4]} años.".format_map(Nombre_diccionario_1));
pausa();limpiar();

print("--------------------------------------------------------------------------")

print ("{:<12} {:<15} {:<10} {:<10} {:<10} {:<10}".format('clave','Item_1','Item_2','Item_3', 'Item_4', 'Item_5'))
for clave_primaria, listas_valores_interiores in Nombre_diccionario_1.items():
	Item_1, Item_2, Item_3, Item_4, Item_5 = listas_valores_interiores;
	print ("{:<12} {:<15} {:<10} {:<10} {:<10} {:<10}".format(clave_primaria, Item_1, Item_2, Item_3, Item_4, Item_5))
pausa();limpiar();

datos = {clave_primaria:listas_valores_interiores for (clave_primaria,listas_valores_interiores) in Nombre_diccionario_1.items()}
print(datos)
pausa();limpiar();

for clave_primaria, listas_valores_interiores in Nombre_diccionario_1.items():
	for listas_valores_interiores in listas_valores_interiores :
		print(clave_primaria,listas_valores_interiores)
pausa();limpiar();
print ("\n\n\nDatos del diccionario:",Nombre_diccionario_1)
print ("\nLongitud del diccionario:",len(Nombre_diccionario_1))
print ("\nItems del diccionario:",Nombre_diccionario_1.items())
print ("\nLlaves del diccionario:",Nombre_diccionario_1.keys())
print ("\nValores del diccionario",Nombre_diccionario_1.values())
pausa();limpiar();

claves_primarias= list(Nombre_diccionario_1.keys())
print("\n\n\n",claves_primarias[0])
for contador in range(5):
	print("sabes que ",Nombre_diccionario_1[claves_primarias[0]][contador],"\t trabaja de ",Nombre_diccionario_1[claves_primarias[1]][contador],"\t y tiene ",Nombre_diccionario_1[claves_primarias[2]][contador]," años.")


nuevo(8);
print("Uso de bucles anillados");
for cont_1 in Nombre_diccionario_1:
	print ("\n",cont_1 ,end=("\t"));
	for cont_2 in Nombre_diccionario_1[cont_1]:
		print(cont_2 ,end=("\t"));
print("\n")
pausa();limpiar();
# Uso de pprint
import pprint
pprint.pprint(Nombre_diccionario_1, width=1)
pausa();limpiar();
# Uso de valor
for cont_1 in Nombre_diccionario_1:
	cont_2 = Nombre_diccionario_1[cont_1]
	print(cont_1,":",cont_2)
pausa();limpiar();
# Uso de format
for cont in Nombre_diccionario_1:
	print("Clave : {} , Valor : {}".format(cont,Nombre_diccionario_1[cont]))
pausa();limpiar();
# Uso de sorted
for row in zip(*([key] + (value) for key, value in sorted(Nombre_diccionario_1.items()))):
	print(*row)

for clave, valor in Nombre_diccionario_1.items():
	print(clave , ":",valor)
pausa();limpiar();
# Uso de json
import json
print(json.dumps(Nombre_diccionario_1, indent = 4))
nuevo(9);
#################################################################
#Ejercicio_Diccionarios_Ej_013
import operator
Weight_details = {'Sam':45, 'Irum':67,'Dolly':80, 'Bela':20}
sorted_weight = sorted(Weight_details.items(), key=operator.itemgetter(1))
print(sorted_weight)
nuevo(10);
#################################################################
#Ejercicio_Diccionarios_Ej_010

Nombre_diccionario_1 = {'Lorca':'Escritor', 'Goya':'Pintor', 'Beethoven':'Musico', 'Freddie Mercury':'Cantante', 'Pablo Picasso':'Pintor', 'Leonardo Da Vinci':'genio total'}
																	# declara diccionario
print(Nombre_diccionario_1) 										# imprime dic1{'Goya': 'Pintor', 'Lorca': 'Escritor'}
print(Nombre_diccionario_1['Lorca'])								# escritor, acceso a un valor por clave
print(Nombre_diccionario_1.get('Gala', 'no existe'))				# acceso a un valor por clave
if 'Lorca' in Nombre_diccionario_1:
	 print('Lorca está')											# comprueba si existe una clave
print(Nombre_diccionario_1.items())									# obtiene una lista de tuplas clave:valor
print(Nombre_diccionario_1.keys())									# obtiene una lista de las claves
print(Nombre_diccionario_1.values())								# obtiene una lista de los valores
pausa();limpiar();
Nombre_diccionario_1['Lorca'] = 'Poeta'								# añade un nuevo par clave:valor
print(Nombre_diccionario_1.items())
pausa();limpiar();
Nombre_diccionario_1['Amenabar'] = 'Cineasta'						# añade un nuevo par clave:valor
print(Nombre_diccionario_1.items())
pausa();limpiar();
Nombre_diccionario_1.update({'Caravaggio' : 'Pintor','Salvador Dalí' : 'Pintor','Claude Monet' : 'Pintor'})
																	# añadir con update()
print(Nombre_diccionario_1.items())									# obtiene una lista de tuplas clave:valor
pausa();limpiar();
del Nombre_diccionario_1['Amenabar']								# borra un par clave:valor
print(Nombre_diccionario_1.items())									# obtiene una lista de tuplas clave:valor
print(Nombre_diccionario_1.pop('Amenabar', 'Amenabar ya no está'))	# borra par clave:valor
del Nombre_diccionario_1
pausa();limpiar();

Nombre_diccionario_1 = dict((('Item_0',5), ('Item_1',10),('Item_2',15), ('Item_3',20),('Item_4',25), ('Item_5',30),('Item_6',35), ('Item_7',40),('Item_8',45),('Item_9',50), ('Item_0',55)))
																						# declara a partir de tupla
print(Nombre_diccionario_1)
del Nombre_diccionario_1
pausa();limpiar();
Nombre_diccionario_1 = dict(Item_0=5, Item_1=10,Item_2=15, Item_3=20,Item_4=25, Item_5=30,Item_6=35, Item_7=40, Item_8=45,Item_9=50, Item_10=55,)
																						# declara a partir de cadenas simples
print(Nombre_diccionario_1)
del Nombre_diccionario_1
pausa();limpiar();
Nombre_diccionario_1 = dict([(z, z**2) for z in (0,1, 2, 3, 4, 5, 6, 7, 8, 9)])			# declara a partir patrón
print(Nombre_diccionario_1)
del Nombre_diccionario_1
pausa();limpiar();
nuevo(11);
#################################################################
#Ejercicio_Diccionarios_Ej_12
artistas = {'Lorca':'Escritor', 'Goya':'Pintor', 'Beethoven':'Musico', 'Freddie Mercury':'Cantante', 'Pablo Picasso':'Pintor', 'Leonardo Da Vinci':'genio total'}	# diccionario
Nombre_diccionario_1={}
for c, v in artistas.items():
	Nombre_diccionario_1[c] = v
	print(Nombre_diccionario_1)
del Nombre_diccionario_1
pausa();limpiar();

paises = ['Chile','España','Francia','Portugal']	# declara lista
Nombre_diccionario_2={}
for i, c in enumerate(paises):
	Nombre_diccionario_2[i] = c						# recorre lista
	print(Nombre_diccionario_2)
del Nombre_diccionario_2
pausa();limpiar();

capitales = ['Santiago','Madrid','París','Lisboa']	# declara lista
paises = ['Chile','España','Francia','Portugal']	# declara lista
Nombre_diccionario_3={}
for p, c in zip(paises, capitales):
	Nombre_diccionario_3[p] = c						# recorre listas
	print(Nombre_diccionario_3)
del Nombre_diccionario_3
nuevo(12);
#################################################################
artistas = {'Lorca':'Escritor', 'Goya':'Pintor', 'Beethoven':'Musico', 'Freddie Mercury':'Cantante', 'Pablo Picasso':'Pintor', 'Leonardo Da Vinci':'genio total'}	# diccionario
print(artistas)
print(artistas["Lorca"])
try:
	print(artistas["Sabato"])#da error xq no esta
except Exception as dato_error:
	print("Ocurrió un error o excepción // Exeception occured:{}".format(dato_error))
print("Sabato : ",artistas.get("Sabato", "Un grande pero no esta en el dic"))

print("Borges : ",artistas.setdefault("Borges", "Genio Nacional"))
print(artistas)
nuevo(13,"fin");
