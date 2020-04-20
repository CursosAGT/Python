from Estructura import *
nuevo(0,"inicio");
##################################################################################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                     Objetos                                 ║
║                                    ---------                                ║
║  Una recapitulación paso a paso.                                            ║
║                                                                             ║
║     Todo porgrama necesita de comandos que ejecuten acciones                ║
║     imprimir, ingresar, guardar, leer, sumar, cambiar, etc                  ║
║                                                                             ║
║     En realidad toda acción necesita de datos con los que trabajar u operar ║
║     Ej imprimir (datos), ingresar(datos), sumar(datos), restar(datos), etc  ║
║                                                                             ║
║     Para poder hacer que el procesador  ejecute estas tareas los datos      ║
║     deben estar accesibles en la memoria RAM                                ║
║                                                                             ║
║     Para poder guardar un dato en memoria necesito ponerle un nombre de     ║
║     fantasía con el que puedo manipular este dato                           ║
║                                                                             ║
║     En un comienzo, con poca memoria disponible podiamos guardar datos      ║
║     pequenos en variables y constantes.                                     ║
║     Había que reservar espacio en memoria dependiendo del tipo y tamaño     ║
║     del dato a guardar.                                                     ║
║                                                                             ║
║     Luego la evolución del soft y hardware permitió asociar varios datos    ║
║     a un espacio en memoria bajo un mismo nombre de fantasía. Estos se      ║
║     denominan Arrays y sus datos normalmente se separan con (,) comas       ║
║                                                                             ║
║     El constante crecimiento en el soft y hardware permitió tener y         ║
║     manejar espacios en memoria mucho más grandes, donde no solo se         ║
║     almacenan datos-atributos sino que permite guardar funciones-métodos    ║
║     propios de cada nombre de fantasía con el que se accede o manipula      ║
║     este espacio.                                                           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")
pausa();limpiar();
nuevo(1)
##################################################################################################################################
#Ej POO_1
class Perro():
	nombre = ""
	edad = 0
	raza= ""
	pelaje=""
	color=""
	patas=4
	cola=1
	responsable=""
	telefono=""
	diceccion=""
	
	def __init__(self, nombre, edad,raza,pelaje,color):
		self.nombre = nombre
		self.edad = edad
		
		# Agraga aquí los otros atributos

	def datos_basicos(self):
		print(f"Mi perro se llama {self.nombre,} y tiene {self.edad} años de edad")
		#continua aqui con el resto
	def datos_completor(self):
		#en un sector de pantalla de 75 espacios imprime
		print(f"Nombre: {self.nombre,} - Edad {self.edad} años ")
		#continua aqui con el resto
		#propietario, telefono, direccion, ......
	def datos_medalla(self):
		print(f"{self.nombre,} \n{self.telefono}")
		#continua aqui con el resto


mascota_1 = Perro("SccobyDoo", 3,"","corto","marron")
mascota_2 = Perro("Droopy", 8,"","corto","ByN")
mascota_3 = Perro("Snoopy", 5,"","largo","blanco")
mascota_1.datos_basicos()
mascota_2.datos_completor()
mascota_3.datos_medalla()
print("Completa los metodos y atrubutos")
print("Genera metodos propios 'habla' 'saluda' 'compañeros'")
print("Genera una clases padre con los atributos normales de los perros (patas, tam_hocico, etc)")
