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
║                               Bucles // while                               ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
nuevo(0,"inicio");
#################################################################
#Clase_While_Ej_01
contador = 1
while contador<10:
	print (contador);
	contador +=1
print ("FIN");
nuevo(1);
#################################################################
#Clase_While_Ej_02
edad=0
print ("venta de alcohol en boliches");
edad=int(input("ingrese su edad :"));
while edad<18:
	print ("Cometió un error al ingresar la edad o es menor y debe retirarse");
	edad=int(input("ingrese su edad :"));
else:
	print("que desea beber.......fin....");
nuevo(2);
#################################################################
#Clase_While_Ej_03
print(" break" );
print ("venta de alcohol en boliches");
edad=int(input("ingrese su edad :"));
while edad<18:
	print ("Cometió un error al ingresar la edad o es menor debe ingresar un valor'<10' y retirarse");
	edad=int(input("ingrese su edad :"));
	if edad<=10:
		print ("toma una cindor y Adios");
		break
else:
	print("que desea beber.......fin....");
nuevo(3);
#################################################################
#Clase_While_Ej_04
print("solos rehacer el ej anterior 10 intentos");
nuevo(4);
#################################################################
#Clase_While_Ej_05
valor=0
print("librería math");
valor=int(input("Ingrese numero para sacar raíz cuadrada:"));
while valor<0:
	valor=int(input("Ingreso un numero negativo. Ingrese un numero para sacar raíz cuadrada:"));
resultado = math.sqrt(valor);
print ("la raiz cuadrada de :"+str(valor));
print ("son : + -"+str(resultado));
nuevo(5);

#################################################################
#Clase_While_Ej_06

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                   while                                     ║
║                                                                             ║
║                               or , and , not                                ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
salir = False
while not salir:
	entrada = input("ingrese un string o zz para salir :")
	if entrada.lower() == "zz":
		salir = True
		print("Chau")
	else:
		print ("Ud.ingreso :",entrada)
