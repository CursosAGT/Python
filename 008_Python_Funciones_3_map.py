from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Funciones y Metodos                            ║
║                              -------------------                            ║
║                                                                             ║
║          Funciones    Description                                           ║
║                   Map                                                       ║
║                                                                             ║
║                                                                             ║
║          Metodos son finciones dentro de clases donde se deberia instanciar ║
║                   a la clase con self nombre_objeto                         ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                              Funciones,  Metodos                            ║
║                                  y Generadores                              ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

""")
nuevo(0,"inicio");
#################################################################
#Ejercicio_Funciones_Ej_001
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                     MAP                                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")
#                          como función
lista1=[10,9,8,7,6,5,4,3,2,1,0];
lista2=[0,1,2,3,4,5,6,7,8,9,10];

def funcion (var_1, var_2):
	return  (var_1 * var_2)
lista_resultado =list( map(funcion,lista1,lista2));
print("lista_resultado=",lista_resultado);
nuevo(1);
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                    FILTER                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")
def filtro (var_1, var_2):
	return  ((var_1 * var_2) >= 10) 
lista_filtrada =list( map(filtro,lista1,lista2));
print("lista_filtrada=",lista_filtrada);
nuevo(2);
