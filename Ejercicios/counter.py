#!/usr/bin/env python
from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las precticas hechas
	pass
	print("""
	╔═════════════════════════════════════════════════════════════════════════════╗
	║                                                                             ║
	║      Unidad 2 - Variables, Listas                                           ║
	║            * Tipos de variables                                             ║
	║            * Procesamiento de cadenas                                       ║
	║                                                                             ║
	╠═════════════════════════════════════════════════════════════════════════════╣
	║                                                                             ║
	║                                                                             ║
	║                                    Variables                                ║
	║                            -----------------------                          ║
	║                                                                             ║
	║                            Crear archivos con extencion                     ║
	║                                                        .py                  ║
	║                                                        .pyc                 ║
	║                                                        .c                   ║
	║                                                                             ║
	║                    and, as, assert, break, class, continue                  ║
	║                    def, del, elif, else, except, exec                       ║
	║                    finally, for, from, global, if, import                   ║
	║                    in, is, lambda, nonlocal, not, or                        ║
	║                    pass, raise, return, try, while, with                    ║
	║                    yield, True, False, None                                 ║
	║                                                                             ║
	║                           tipos de variables                                ║
	║                                               Mutable                       ║
	║                                               Inmutable                     ║
	║                                                                             ║
	║                                               string                        ║
	║                                               float                         ║
	║                                               Intenger                      ║
	║                                               long...                       ║
	║                                                                             ║
	║                 espacio en memoria                                          ║
	║                                                                             ║
	║                 limites de entrega del valor                                ║
	║                                     locales                                 ║
	║                                     nonlocal                                ║
	║                                     globales                                ║
	║                                                                             ║
	║                 escribir un texto                                           ║
	║                                                                             ║
	║                 texto desde una variable                                    ║
	║                                                                             ║
	║                                                                             ║
	╚═════════════════════════════════════════════════════════════════════════════╝
		""");
	limpiar();
	

from collections import Counter

def comparar(a,b):
	resultado = Counter(a)==Counter(b);
	return resultado;
	
lista_base=["Juan","Pedro","Laura","Andrea"];
lista_actualizada=["Laura","Juan","Andrea","Pedro"];
lista_modificada=["JUAN","PEDRO","LAURA","ANDREA"];


regreso = comparar(lista_base, lista_actualizada)
print ("resultado de comparacion: ",regreso)

regreso = comparar(lista_base, lista_modificada)
print ("resultado de comparacion: ",regreso)


regreso = comparar(lista_base.upper(), lista_modificada.upper())
print ("resultado de comparacion: ",regreso)
