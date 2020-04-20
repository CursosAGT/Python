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
print("""

Para entender este paradigma primero tenemos que comprender qué es una clase y qué es un objeto. Un objeto es una entidad que agrupa un
estado y una funcionalidad relacionadas. El estado del objeto se define a través de variables llamadas 'atributos', mientras que la funcionalidad
se modela a través de funciones a las que se les conoce con el nombre de 'métodos' del objeto.

TIPS
Un espacio de nombres es una relación de nombres a objetos.
Cualquier cosa después de un punto es un atributo
Las referencias a nombres en módulos son referencias a atributos:
Ej en la expresión modulo.funcion, modulo es un "objeto módulo" y funcion es un "atributo" de este objeto
Un ámbito es una región textual de un programa en Python donde un espacio de nombres es accesible directamente.
Cuando se ingresa una definición de clase, se crea un nuevo espacio de nombres, el cual se usa como ámbito local;
por lo tanto, todas las asignaciones a variables locales van a este nuevo espacio de nombres.
En particular, las definiciones de funciones asocian el nombre de las funciones nuevas allí.
Una clase se finaliza normalmente se crea un objeto clase que envuelve los contenidos del espacio de nombres creado por la definición de la clase en el ambito
Este objeto clase se asocia al ambito logal original bajo el nombre que se le puso a la clase en el encabezado de su definición (Class Clases_ejemplo).
Los objetos clase soportan dos tipos de operaciones: hacer referencia a atributos e instanciación.

class Clases_ejemplo():
	atributos = 1973
	def instancia(self):
		return 'UTN 2020'

Clases_ejemplo.atributos (numero entero) y Clases_ejemplo.instancia (Función o Metodo).
Asignarcion exterior
	Clases_ejemplo.atributos = 2020
variable = Clases_ejemplo()

...crea una nueva instancia de la clase y asigna este objeto a la variable local "variable".

""")
limpiar();
nuevo(0)
##################################################################################################################################
#Ej POO_1
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║            Creo un Objetos y cargo los datos de forma directa               ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")

print ("1)Creo un constructos de objetos")
#          Nombre de laclase que mecontruye / instancia los objetos (Se utiliza la primer letra en mayuscula)
#          |
class Persona:
	#<--------------En este caso NO tiene parametros de entrada
	pass#<----------------------La deja vacia
print ("2)Creo un objeto con el nombre de fantacia Objeto_1")
#   nombre de fantacia con el que creo/manupulo al objeto
#   |  
objeto_1 = Persona();#<---Nombre de la clase constructora de objetos que estara vacio

print ("3)Verifico los atributos del Objeto instanciado bajo el nombre de fantacia Objeto_1")

#   nombre de fantacia con el que creo/manupulo al objeto
#   |  
#   |      nombre del atributo  
#   |      |  
#   |      |       Valor del atributo para este objeto en particular
#   |      |       |
objeto_1.nombre="Ariel";#<---------------------------Atributo en forma de dato cadena de caracteres - string
objeto_1.sexo="Masculino";#<-------------------------Atributo en forma de dato cadena de caracteres - string 
objeto_1.edad=46;#<----------------------------------Atributo en forma de dato numerico entero
objeto_1.altura=1.78;#<------------------------------Atributo en forma de dato numerico decimal - Flotante
objeto_1.fecha_Nac=[1973,9,22];#<--------------------Atributo en forma de array - Lista
objeto_1.diestro=True;#<-----------------------------Atributo en forma de dato booleana - True / False

nuevo(1)

print ("4)Verifico los atributos del Objeto instanciado bajo el nombre de fantacia Objeto_1")
print (f"El nombre del objeto_1 es de : {objeto_1.nombre} - String")
print (f"La edad del objeto_1 es de : {objeto_1.edad} - Valor Entero"  )
print (f"La fecha de nacimiento del objeto_1 es de : {objeto_1.fecha_Nac} -Lista")
pausa();
print ("Uso de metodos reservados de Pyhton")

print (f"Confirmar la existencia del atributo 'altura' en el objeto_1 : {hasattr(objeto_1,'altura')} - Via hasattr")
print (f"Confirmar la existencia del atributo  'peso'  en el objeto_1 : {hasattr(objeto_1,'peso')} - Via hasattr")
print (f"Antes\n\tEl nombre del objeto_1 es de : {getattr(objeto_1,'nombre')} - Via getattr")
setattr(objeto_1,'nombre','Juan')
print (f"Despues\n\tEl nombre del objeto_1 es de : {getattr(objeto_1,'nombre')} - Via getattr")
pausa();
print("Borro el atributo con delattr")
print (f"Antes\n\tEl sexo del objeto_1 es de : {hasattr(objeto_1,'sexo')} - Via hasattr")
delattr(objeto_1,"sexo")#<----------------desde el objeto
print (f"Despues\n\tEl sexo del objeto_1 es de : {hasattr(objeto_1,'sexo')} - Via hasattr")


nuevo(2)
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║          Creo un Objetos y cargo los datos desde el constructos             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")
#Ej POO_2
print ("1)Creo un constructos de objetos")
#          Nombre de laclase que mecontruye / instancia los objetos (Se utiliza la primer letra en mayuscula)
#          |
class Persona:
	#<--------------En este caso NO tiene parametros de entrada
	nombre="Ariel";#<---------------------------Atributo en forma de dato cadena de caracteres - string
	sexo="Masculino";#<-------------------------Atributo en forma de dato cadena de caracteres - string 
	edad=46;#<----------------------------------Atributo en forma de dato numerico entero
	altura=1.78;#<------------------------------Atributo en forma de dato numerico decimal - Flotante
	fecha_Nac=[1973,9,22];#<--------------------Atributo en forma de array - Lista
	diestro=True;#<-----------------------------Atributo en forma de dato booleana - True / False
print ("2)Creo un objeto con el nombre de fantacia Objeto_1")
#   nombre de fantacia con el que creo/manupulo al objeto
#   |  
objeto_1 = Persona();#<---Nombre de la clase constructora de objetos
print ("3)Verifico los atributos del Objeto instanciado bajo el nombre de fantacia Objeto_1")
print (f"El nombre del objeto_1 es de : {objeto_1.nombre} - String")
print (f"La edad del objeto_1 es de : {objeto_1.edad} - Valor Entero"  )
print (f"La fecha de nacimiento del objeto_1 es de : {objeto_1.fecha_Nac} -Lista")
pausa();
print ("Uso de metodos reservados de Pyhton")

print (f"Confirmar la existencia del atributo 'altura' en el objeto_1 : {hasattr(objeto_1,'altura')} - Via hasattr")
print (f"Confirmar la existencia del atributo  'peso'  en el objeto_1 : {hasattr(objeto_1,'peso')} - Via hasattr")
print (f"Antes\n\tEl nombre del objeto_1 es de : {getattr(objeto_1,'nombre')} - Via getattr")
setattr(objeto_1,'nombre','Juan')
print (f"Despues\n\tEl nombre del objeto_1 es de : {getattr(objeto_1,'nombre')} - Via getattr")
pausa();
print("Borro el atributo con delattr")
print (f"Antes\n\tEl sexo del objeto_1 es de : {hasattr(objeto_1,'edad')} - Via hasattr")
delattr(Persona,"edad")#<----------------desde el constructor
print (f"Despues\n\tEl sexo del objeto_1 es de : {hasattr(objeto_1,'edad')} - Via hasattr")
nuevo(3)
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║          Creo un Objetos y cargo los datos desde el constructos             ║
║               con datos recibidos como parametros                           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")
print ("1)Creo un constructos de objetos")
#          Nombre de laclase que mecontruye / instancia los objetos (Se utiliza la primer letra en mayuscula)
#          |
class Persona:
	print ("2)Creo un constructos de objetos")
	#     funcion __init__ constructora (se autoejecuta)
	#     |  
	#     |         #parametro self - nombre de fantacia con el que creo/manupulo al objeto  
	#     |         | 
	#     |         |         Parametros
	#     |         |         |
	def __init__(self,nombre,sexo,edad,altura,fecha_Nac,diestro):#constructor-------En este caso SI tiene parametros de entrada
		self.nombre=nombre;#<------------------------------Atributo en forma de dato cadena de caracteres - string
		self.sexo=sexo;#<----------------------------------Atributo en forma de dato cadena de caracteres - string 
		self.edad=edad;#<----------------------------------Atributo en forma de dato numerico entero
		self.altura=altura;#<------------------------------Atributo en forma de dato numerico decimal - Flotante
		self.fecha_Nac=fecha_Nac;#<------------------------Atributo en forma de array - Lista
		self.diestro=diestro;#<----------------------------Atributo en forma de dato booleana - True / False

print ("3)Cargo parmetros")
nombre="Ariel";#<---------------------------Atributo en forma de dato cadena de caracteres - string
sexo="Masculino";#<-------------------------Atributo en forma de dato cadena de caracteres - string 
edad=46;#<----------------------------------Atributo en forma de dato numerico entero
altura=1.78;#<------------------------------Atributo en forma de dato numerico decimal - Flotante
fecha_Nac=[1973,9,22];#<--------------------Atributo en forma de array - Lista
diestro=True;#<-----------------------------Atributo en forma de dato booleana - True / False
print ("4)Creo un objeto con el nombre de fantacia Objeto_1")
#   nombre de fantacia con el que creo/manupulo al objeto  +++++ Este es el parametro self
#   |  
#   |         #<---Nombre de la clase constructora de objetos
#   |         | 
#   |         |         Parametros
#   |         |         |
objeto_1 = Persona(nombre,sexo,edad,altura,fecha_Nac,diestro);
print ("5)Verifico los atributos del Objeto instanciado bajo el nombre de fantacia Objeto_1")
print (f"El nombre del objeto_1 es de : {objeto_1.nombre} - String")
print (f"La edad del objeto_1 es de : {objeto_1.edad} - Valor Entero"  )
print (f"La fecha de nacimiento del objeto_1 es de : {objeto_1.fecha_Nac} -Lista")
pausa();
print ("Uso de metodos reservados de Pyhton")

print (f"Confirmar la existencia del atributo 'altura' en el objeto_1 : {hasattr(objeto_1,'altura')} - Via hasattr")
print (f"Confirmar la existencia del atributo  'peso'  en el objeto_1 : {hasattr(objeto_1,'peso')} - Via hasattr")
print (f"Antes\n\tEl nombre del objeto_1 es de : {getattr(objeto_1,'nombre')} - Via getattr")
setattr(objeto_1,'nombre','Juan')
print (f"Despues\n\tEl nombre del objeto_1 es de : {getattr(objeto_1,'nombre')} - Via getattr")
pausa();
print("Borro el atributo con delattr")
print (f"Antes\n\tEl sexo del objeto_1 es de : {hasattr(objeto_1,'edad')} - Via hasattr")
delattr(objeto_1,"edad")#<----------------desde el constructor
print (f"Despues\n\tEl sexo del objeto_1 es de : {hasattr(objeto_1,'edad')} - Via hasattr")
nuevo(4)

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║          Creo un Objetos y cargo los datos desde el constructos             ║
║               con datos recibidos como parametros y metodo propio           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")
print ("1)Creo un constructos de objetos")
#          Nombre de laclase que mecontruye / instancia los objetos (Se utiliza la primer letra en mayuscula)
#          |
class Persona:
	print ("2)Inicializo los atributos del objetos")
	#     funcion __init__ inicializador (se autoejecuta)
	#     |  
	#     |         parametro self - nombre de fantacia con el que creo/manupulo al objeto  
	#     |         | 
	#     |         |         Parametros
	#     |         |         |
	def __init__(self,nombre,sexo,edad,altura,fecha_Nac,diestro):#constructor-------En este caso SI tiene parametros de entrada
		self.nombre=nombre;#<------------------------------Atributo en forma de dato cadena de caracteres - string
		self.sexo=sexo;#<----------------------------------Atributo en forma de dato cadena de caracteres - string 
		self.edad=edad;#<----------------------------------Atributo en forma de dato numerico entero
		self.altura=altura;#<------------------------------Atributo en forma de dato numerico decimal - Flotante
		self.fecha_Nac=fecha_Nac;#<------------------------Atributo en forma de array - Lista
		self.diestro=diestro;#<----------------------------Atributo en forma de dato booleana - True / False

	print ("3)Creo un metodo propio para todas las instancias creadas por la clase Persona")
	def cumplir_años(self):
		self.edad+=1;

print ("4)Cargo parmetros")
nombre="Ariel";#<---------------------------Atributo en forma de dato cadena de caracteres - string
sexo="Masculino";#<-------------------------Atributo en forma de dato cadena de caracteres - string 
edad=46;#<----------------------------------Atributo en forma de dato numerico entero
altura=1.78;#<------------------------------Atributo en forma de dato numerico decimal - Flotante
fecha_Nac=[1973,9,22];#<--------------------Atributo en forma de array - Lista
diestro=True;#<-----------------------------Atributo en forma de dato booleana - True / False
print ("5)Creo un objeto con el nombre de fantacia Objeto_1")
#   nombre de fantacia con el que creo/manupulo al objeto  +++++ Este es el parametro self
#   |  
#   |         #<---Nombre de la clase constructora de objetos
#   |         | 
#   |         |         Parametros
#   |         |         |
objeto_1 = Persona(nombre,sexo,edad,altura,fecha_Nac,diestro);
print (f"Antes:\n\tLa edad del objeto_1 es de : {objeto_1.edad}"  )
print ("6)Llamo a un metodo cumplir_años propio de la clase donde se instancio Objeto_1")
objeto_1.cumplir_años()
print (f"Despues\n\tLa edad del objeto_1 es de : {objeto_1.edad}")

nuevo(5)

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║          Creo un Objetos y cargo los datos desde el constructos             ║
║        con datos recibidos como parametros y varios metodos propios         ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")
print ("1)Creo un constructos de objetos")
#          Nombre de laclase que mecontruye / instancia los objetos (Se utiliza la primer letra en mayuscula)
#          |
class Persona:
	print ("2)Inicializo los atributos del objetos")
	#     funcion __init__ inicializador (se autoejecuta)
	#     |  
	#     |         parametro self - nombre de fantacia con el que creo/manupulo al objeto  
	#     |         | 
	#     |         |         Parametros
	#     |         |         |
	def __init__(self,nombre,sexo,edad,altura,fecha_Nac,diestro):#constructor-------En este caso SI tiene parametros de entrada
		self.nombre=nombre;#<------------------------------Atributo en forma de dato cadena de caracteres - string
		self.sexo=sexo;#<----------------------------------Atributo en forma de dato cadena de caracteres - string 
		self._edad=edad;#<---------------------------------Atributo en forma de dato numerico entero
		self.altura=altura;#<------------------------------Atributo en forma de dato numerico decimal - Flotante
		self.fecha_Nac=fecha_Nac;#<------------------------Atributo en forma de array - Lista
		self.diestro=diestro;#<----------------------------Atributo en forma de dato booleana - True / False


	print ("3)Creo un metodo propio para todas las instancias creadas por la clase Persona")
	def cumplir_años(self):
		self._edad+=1;
		self.imprimir_edad()

	def imprimir_edad(self, saludo="Felicidades, Ahora"):
		print (f"{saludo} {self.nombre} tienes {self._edad} jovenes años"  )



print ("4)Cargo parmetros")
nombre="Ariel";#<---------------------------Atributo en forma de dato cadena de caracteres - string
sexo="Masculino";#<-------------------------Atributo en forma de dato cadena de caracteres - string 
edad=46;#<----------------------------------Atributo en forma de dato numerico entero
altura=1.78;#<------------------------------Atributo en forma de dato numerico decimal - Flotante
fecha_Nac=[1973,9,22];#<--------------------Atributo en forma de array - Lista
diestro=True;#<-----------------------------Atributo en forma de dato booleana - True / False
print ("5)Creo un objeto con el nombre de fantacia Objeto_1")
#   nombre de fantacia con el que creo/manupulo al objeto  +++++ Este es el parametro self
#   |  
#   |         Nombre de la clase constructora de objetos
#   |         | 
#   |         |         Parametros
#   |         |         |
objeto_1 = Persona(nombre,sexo,edad,altura,fecha_Nac,diestro);

print ("Llamo a un metodo imprimir_edad ")
objeto_1.imprimir_edad("Aun ")

print ("Llamo a un metodo cumplir_años ")
objeto_1.cumplir_años()
nuevo(6)

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║          Herencias:                                                         ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""")

class Persona(object):
	def __init__(self,sexo):#,madre_p_de_dar_un_gen_x=True,madre_p_de_dar_un_gen_y=False):
		self.sexo=sexo;
class Madre(Persona):
	pass
	"""
	def __init__(self,sexo):#,madre_p_de_dar_un_gen_x=True,madre_p_de_dar_un_gen_y=False):
		self.madre_gen_x=True;
		self.madre_herencia="mitocondrias";
		self.nota_madre_h="El hijo Hereda ADN mitocondrial - Unicamente de la madre ya que el nucleo del espermatosoide penetra el citoplasma, pero no las otras estructuras no nucleares";
	def M_Saber(self,sexo):
		print(self.madre_herencia,self.nota_madre_h)
	"""
class Padre(Persona):
	pass
	"""
	def __init__(self,sexo):#,padre_p_de_dar_un_gen_x=True,padre_p_de_dar_un_gen_y=True):
		self.padre_gen_x=True
		self.padre_gen_y=True		
		self.padre_herencia="Hipertricosis Auricular"
		self.nota_padre_h= "Desarrollo exesivo de bello en el pabellon auricular - mucho pelo en toda las orejas"
		#"El hijo No Hereda ADN mitocondrial del padre ni de la abuela - Solo el nucleo del espermatosoide penetra el citoplasma, pero no las otras estructuras no nucleares";
	def P_Saber(self):
		print(self.padre_herencia,self.nota_padre_h)
	"""
class Hijo(Madre,Padre):
	pass
	"""
	def __init__(self,sexo):#constructor-------En este caso SI tiene parametros de entrada
		super(Madre,self).__init__(madre_gen_x)
		super(padre,self).__init__(padre_gen_x)
		super(Padre,self).__init__(padre_gen_y)
	"""
objeto_1 = Hijo(sexo="M");

nuevo(7)
"""
###################################################################################
class Persona(object):
	def __init__(self):
		pass
class Madre(Persona):#				clases padre
	def __init__(self,sexo):#					Constructor de estado inicial
		self.sexo=sexo;
		self.madre_gen_x=True
		self.madre_herencia="mitocondrias";
		self.nota_madre_h="El hijo Hereda ADN mitocondrial - Unicamente de la madre ya que el nucleo del espermatosoide penetra el citoplasma, pero no las otras estructuras no nucleares"; 

class Padre(Persona):#				clases padre
	def __init__(self,sexo):
		self.sexo=sexo;
		self.padre_herencia="Hipertricosis Auricular";
		self.nota_padre_h= "Desarrollo exesivo de bello en el pabellon auricular - mucho pelo en toda las orejas";
		#"El hijo No Hereda ADN mitocondrial del padre ni de la abuela - Solo el nucleo del espermatosoide penetra el citoplasma, pero no las otras estructuras no nucleares";

class Hijo(Madre,Padre):#									 		clases hija
	def __init__(self,sexo):#,madre_gen_x,padre_gen_x,padre_gen_y):

		Madre.__init__(self, madre_herencia, nota_madre_h)
		Padre.__init__(self, padre_herencia, nota_padre_h)
		
		#super().__init__(self.madre_herencia,self.nota_madre_h)#				se define a partir del constructor padre
		#super().__init__(self.padre_herencia,self.nota_padre_h)	
	def M_Saber(self,madre_herencia,nota_madre_h):
		print(madre_herencia,nota_madre_h)
	def P_Saber(self,padre_herencia,nota_padre_h):
		print(padre_herencia,nota_padre_h)
	pass
	" ""
	def __init__(self,sexo):#,madre_gen_x,padre_gen_x,padre_gen_y):
		super(Madre).__init__(self.madre_herencia,self.nota_madre_h)#				se define a partir del constructor padre
		super(Padre).__init__(self.padre_herencia,self.nota_padre_h)
		self.sexo=sexo;
		if self.sexo=="M":
			self.padre_gen_x=False
			self.padre_gen_y=True
		else:
			self.padre_gen_x=True
			self.padre_gen_y=False
		self.madre_gen_x=True

	def Saber(self):
		print(self.padre_gen_x,	self.padre_gen_y,self.madre_gen_x)


Mjose=Hijo(sexo="F")
pedro=Hijo(sexo="M")
#Mjose.Saber()
#print(pedro.padre_gen_x);
#print(pedro.padre_gen_y);
#print(pedro.madre_gen_x);
print(pedro.M_Saber())
print(pedro.P_Saber())
pausa()
"""
