from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                          Pantalla Gráfica Parte                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                Python tkinter                               ║
║                               ----------------                              ║
║                                                                             ║
║       Operator     Description                                              ║
║                                                                             ║
║       Button       The Button widget is used to display buttons in          ║
║                    your application.                                        ║
║              Option   Description                                           ║
║              activebackground-                                              ║
║                 Background color when the button is under the cursor        ║
║              activeforeground-                                              ║
║                 Foreground color when the button is under the cursor        ║
║              bd     -                                                       ║
║                 Border width in pixels. Default is 2.                       ║
║              bg     -                                                       ║
║                 Normal background color.                                    ║
║              command-                                                       ║
║                 Function or method to be called when the button is clicked. ║
║              fg     -                                                       ║
║                 Normal foreground (text) color.                             ║
║              font   -                                                       ║
║                 Text font to be used for the button's label.                ║
║              height -                                                       ║
║                 Height of the button in text lines (for textual buttons)    ║
║                 or pixels (for images).                                     ║
║              highlightcolor-                                                ║
║                 The color of the focus highlight when the widget has        ║
║                 focus.                                                      ║
║              image  -                                                       ║
║                 Image to be displayed on the button (instead of text).      ║
║              justify-                                                       ║
║                 How to show multiple text lines: LEFT to left-justify each  ║
║                 line; CENTER to center them; or RIGHT to right-justify.     ║
║              padx   -                                                       ║
║                 Additional padding left and right of the text.              ║
║              pady   -                                                       ║
║                 Additional padding above and below the text.                ║
║              relief -                                                       ║
║                 Relief specifies the type of the border. Some of the values ║
║                                                                             ║
║                 are SUNKEN, RAISED, GROOVE, and RIDGE.                      ║
║              state  -                                                       ║
║                 Set this option to DISABLED to gray out the button and make ║
║                 it unresponsive. Has the value ACTIVE when the mouse        ║
║                 is over it. Default is NORMAL.                              ║
║              underline-                                                     ║
║                 Default is -1, meaning that no character of the text on     ║
║                 the button will be underlined. If nonnegative,              ║
║                 the corresponding text character will be underlined.        ║
║              width  -                                                       ║
║                 Width of the button in letters (if displaying text)         ║
║                 or pixels (if displaying an image).                         ║
║              wraplength-                                                    ║
║                 If this value is set to a positive number, the text         ║
║                 lines will be wrapped to fit within this length.            ║
║                                                                             ║
║              Medthod-     Description                                       ║
║              flash() -                                                      ║
║                 Causes the button to flash several times between active     ║
║                 and normal colors. Leaves the button in the state it was    ║
║                 in originally. Ignored if the button is disabled.           ║
║              invoke()-                                                      ║
║                 Calls the button's callback, and returns what that function ║
║                 returns. Has no effect if the button is disabled or there   ║
║                 is no callback.                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║       Canvas       The Canvas widget is used to draw shapes, such as lines, ║
║                    ovals, polygons and rectangles, in your application.     ║
║                                                                             ║
║       Checkbutton  The Checkbutton widget is used to display a number of    ║
║                    options as checkboxes. The user can select multiple      ║
║                    options at a time.                                       ║
║                                                                             ║
║       Entry        The Label widget is used to provide a single-line caption║
║                    field for accepting values from a user.                  ║
║                                                                             ║
║       Frame        The Frame widget is used as a container widget to        ║
║                    organize other widgets.                                  ║
║                                                                             ║
║       Label        Returns the index of the first element with the specified║
║                    for other widgets. It can also contain images.           ║
║                                                                             ║
║       Listbox      The Listbox widget is used to provide a list of options  ║
║                    to a user.                                               ║
║                                                                             ║
║       Menubutton   The Menubutton widget is used to display menus in your   ║
║                    application.                                             ║
║                                                                             ║
║       Menu         The Menu widget is used to provide various commands to   ║
║                    a user. These commands are contained inside Menubutton.  ║
║                                                                             ║
║       Message      The Message widget is used to display multiline text     ║
║                    fields for accepting values from a user.                 ║
║                                                                             ║
║       Radiobutton  The Radiobutton widget is used to display a number of    ║
║                    options as radio buttons. The user can select only one   ║
║                    option at a time.                                        ║
║                                                                             ║
║       Scale        The Scale widget is used to provide a slider widget.     ║
║                                                                             ║
║       Scrollbar    The Scrollbar widget is used to add scrolling capability ║
║                     to various widgets, such as list boxes.                 ║
║                                                                             ║
║       Text         The Text widget is used to display text in multiple lines║
║                                                                             ║
║       Toplevel     The Toplevel widget is used to provide a separate window ║
║                     container.                                              ║
║                                                                             ║
║       Spinbox      The Spinbox widget is a variant of the standard Tkinter  ║
║                    Entry widget, which can be used to select from a fixed   ║
║                    number of values.                                        ║
║                                                                             ║
║       PanedWindow  A PanedWindow is a container widget that may contain any ║
║                     number of panes, arranged horizontally or vertically.   ║
║                                                                             ║
║       LabelFrame   A labelframe is a simple container widget. Its primary   ║
║                     purpose is to act as a spacer or container for complex  ║
║                     window layouts.                                         ║
║                                                                             ║
║       tkMessageBox This module is used to display message boxes in you      ║
║                     applications.                                           ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║              Unidad 8,0                                                     ║
║              pip install Pillow                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
pip install pillow
pip install flask


https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html
https://www.youtube.com/watch?v=CppgV8inf7g&pbjreload=10
https://python-para-impacientes.blogspot.com/2015/12/tkinter-interfaces-graficas-en-python-i.html
https://python-para-impacientes.blogspot.com/2015/12/tkinter-disenando-frame_pantalla_raizs-graficas.html
""");
nuevo(0,"inicio");
#################################################################
#Ej_P_graf_01
print("Ej 1")
print("A)Genera una pantalla con geometría de '640x 480', color de fondo 'white', titulo 'Ejercicios'")
print("B)Coloca un frame por el tamaño de la pantalla equidistantes")
print("C)Ubica 2 etiqueta label1 'Ingrese su nobre', label2 '' y un recuadro de texto"); 
#	var = StringVar()
print("D)Un botón 'ingresar' que al presionarlo tome el empty, lo coloque en label2 y lo grabe en un archivo Ej.txt")
print("D.1)habilita una nueva hoja con emergentes con dos botones 'Confirmar' y 'Cancelar' graba el archivo /borra los datos ")
#from tkinter import messagebox
#messagebox.showinfo(
print("D.2)Coloca un frame de  600x400 y con pads equidistantes a la pantalla-centrado")
nuevo(1)
################################################################
#Ej_P_graf_02
print("Ej 2")
print("A)Genera una pantalla con geometría de '640x 480', color de fondo 'white', título 'Ejercicios'")
print("B)Ubica un listbox de 4 elementos, Coloca en un label la eleccion"); 
#	var = StringVar()
print("C)Ubica un Radiobutton de  4 elementos, Coloca en un label la eleccion"); 
#	var = IntVar()
nuevo(2)
################################################################
#Ej_P_graf_03
print("Ej 3")
print("A)Completa el menu con 6 opciones")
print("B)Cada item del menu debe llevar mínimo 6 opciones de submenu")
print("C)Solo 5 de las opciones del submenu deberan tener una funcion")
print("\tEj:Help debe habilitar una nueva pantalla con los datos del programador, fecha y página web, boton salir")
print("\tEj:Colores debe dar 5 opciones de colores en una ventana emergente.")
print("\t\t Tras seleccionarla cambiar el color del font o fondo actual por el elegido")


from tkinter import *
from tkinter import messagebox

def iniciar_ej_menu():

	pantalla_raiz = Tk()
	pantalla_raiz.geometry("640x480")

	def donothing():
	   filewin = Toplevel(pantalla_raiz)
	   button = Button(filewin, text="Luego se definirán los comandos")
	   button.pack()
	def cambiarcolor():
		pass
	def help():
		pass

	Barra_menu = Menu(pantalla_raiz)
	Item_Menu = Menu(Barra_menu, tearoff = 0)
	Item_Menu.add_command(label = "Recargar", command = donothing)
	Item_Menu.add_command(label = "Abrir", command = donothing)
	Item_Menu.add_command(label = "Grabar", command = donothing)
	Item_Menu.add_command(label = "Grabar como", command = donothing)
	Item_Menu.add_command(label = "Cerrar", command = donothing)
	Item_Menu.add_separator()
	Item_Menu.add_command(label = "Salir", command = pantalla_raiz.destroy)
	Barra_menu.add_cascade(label = "Archivo", menu = Item_Menu)

	Edit_Menu = Menu(Barra_menu, tearoff=0)
	Edit_Menu.add_command(label = "Deshacer", command = donothing)
	Edit_Menu.add_separator()

	Edit_Menu.add_command(label = "Copiar", command = donothing)
	Edit_Menu.add_command(label = "Cortar", command = donothing)
	Edit_Menu.add_command(label = "Pegar", command = donothing)
	Edit_Menu.add_command(label = "Borrar", command = donothing)
	Edit_Menu.add_command(label = "Seleccionar todo", command = donothing)
	Barra_menu.add_cascade(label = "Editar", menu = Edit_Menu)

	Config_Menu = Menu(Barra_menu, tearoff=0)
	Config_Menu.add_command(label = "Color", command = cambiarcolor)
	Config_Menu.add_command(label = "ww", command = donothing)
	Config_Menu.add_command(label = "xx", command = donothing)
	Config_Menu.add_command(label = "yy", command = donothing)
	Config_Menu.add_command(label = "zz", command = donothing)
	Barra_menu.add_cascade(label = "Configurar", menu = Config_Menu)

	Help_Menu = Menu(Barra_menu, tearoff=0)
	Help_Menu.add_command(label = "Help Index", command = Help)
	Help_Menu.add_command(label = "About...", command = donothing)
	Barra_menu.add_cascade(label = "Help", menu = Help_Menu)

	pantalla_raiz.config(menu = Barra_menu)
	pantalla_raiz.mainloop()
	
iniciar_ej_menu()	
var = input ("inicio Ejemplo menu (S/N)")
if var.upper() =="S":iniciar_ej_menu()
nuevo(4);
