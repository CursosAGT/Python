from Estructura import *
import os
nuevo(0,"inicio");
##################################################################################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aquí las practicas hechas
	pass
limpiar();''' ╝ ╗ ╚ ╔ ╩ ╦ ╠╣ ═ ╬ ¤ ╚ ═ 
« » ¤ ░ ▒ ▓ │ ┤ ┐└ ┴ ┬ ├ ─ ┼  ┘ ┌ ¦ █ ▄  ▀¯-_≡±‗=¾¶§¸°¨·¹³²
■'''
##################################################################################################################################
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║                         ╦     ╔═══════╗      ╔════════╗                     ║
║                         ║     ║       ╚╗     ║                              ║
║                         ║     ║        ║     ║                              ║
║                         ║     ║        ║     ║                              ║
║                         ║     ║        ║     ╠═══════╣                      ║
║                         ║     ║        ║     ║                              ║
║                         ║     ║       ╔╝     ║                              ║
║                         ╩  ¤  ╚═══════╝  ¤   ╚════════╝  ¤                  ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                                                             ║
║        https://www.python.org/downloads/                                    ║
║        ----------------------------------                                   ║
║        https://www.python.org/downloads/release/python-382/                 ║
║        -----------------------------------------------------                ║
║                                                                             ║
║        macOS 64-bit installer                                               ║
║                       https://www.python.org/downloads/mac-osx/             ║
║                                                                             ║
║        Linux x86-64 instaler                                                ║
║                       https://www.python.org/downloads/source/              ║
║                                                                             ║
║        Windows x86-64 executable installer                                  ║
║                       https://www.python.org/downloads/windows/             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
pausa()
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║ 
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║         ¤ Descarga en archivo ejecutable.                                   ║
║                                                                             ║
║         ¤ Ejecutalo.                                                        ║
║                    Por favor cliqueá la casilla.                            ║
║                    agregar a variables de entorno (PATH).                   ║
║                    < no borres el instalador aun >                          ║
║                                                                             ║
║            Una vez terminado abre una consolas                              ║
║                  Tecla windows + R                                          ║
║                  Escribe "cmd + tecla enter"                                ║
║                                                                             ║
║       (A)  Te encontrarás en una pantalla generalmente negra                ║
║                  donde puedas typear comandos (como el los viejos DOS)      ║
║                  Escribe "py + tecla enter"                                 ║
║                                                                             ║
║            Ahora estarás dentro de python.                                  ║
║                  Verás la version del interprete.                        ║
║                  Y tres simbolos mayor junto al cursor ">>>█"               ║
║            Funcionó...Tipea "exit() + tecla enter"                             ║
║                                                                             ║
║            Error...Windows te da un error de que no reconoce el comando     ║
║                  Probablemente no hayas agregado la opción de apregar       ║
║                  python al path - variables de entorno                      ║
║                  Ejecutá el instalador nuevamente                           ║
║                  --->  Modify Setup                                         ║
║                  ----->  Modify                                             ║
║                           Optional Features                                 ║
║                  ------->  Next                                             ║
║                            Advance Options                                  ║
║                            * ve el iten Add Python to environment variable  ║
║                            SU CASILLA DEBE ESTAR ACTIVA                     ║
║                  --------->  Install                                        ║
║                  ----------->  Close   Volver a probar (A)                  ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
pausa()
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║           Una vez instalado debemos agregar varias librerías                ║
║                  Python tiene un instalador propio muy simplie "pip"        ║
║                  Primero deberá actualizar pip,                            ║
║                      Tecla windows + R                                      ║
║                      Escribe "cmd + tecla enter"                            ║
║                  pip install --upgrade pip                                  ║
║                  pip install imutils                                        ║
║                  pip install tkintertable                                   ║
║                  pip install numpy                                          ║
║                  pip install opencv-python                                  ║
║                  pip install pandas                                         ║
║                  pip install Pillow                                         ║
║                  pip install schedule                                       ║
║                  pip install plotly                                         ║
║                  pip install scipy                                          ║
║                  pip install -U matplotlib                                  ║
║                  pip install  tkintertable                                  ║
║                                                                             ║
║         Algunas mas difíciles   https://tkdocs.com/tutorial/install.html    ║
║                  pip install python-tk                                      ║
║                       Windows debería no ser necesario                      ║
║                       Linux  sudo zypper install python3-tk                 ║
║                              sudo apt-get install python3-tk                ║
║                       Mac    https://www.python.org/download/mac/tcltk/     ║
║                              sudo apt-get install python3-tk                ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
pausa()
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║        Instalar MySQL// maria db // workbench // PHP // Apache              ║
║                                                                             ║
║                ¤ Ve a la web de mysql                                       ║
║                     https://dev.mysql.com/downloads/mysql/                  ║
║                        Busca tu versión segun tu sistema operatvo "OS"      ║
║                                                                             ║
║                     Ej-> Windows (x86, xx-bit), MSI Installer               ║
║                                                                             ║
║                En windows                                                   ║
║                  ¤ Descarga en archivo ejecutable 'MSI'                     ║
║                     Begin your Download....                                 ║
║                   ---->No thanks, just start mydownload                      ║
║                                                                             ║
║                     mysql-installer-web-community-......                    ║
║                                                                             ║
║                ¤ Ejecuta y sigue las instrucciones según tu OS              ║
║                     <<debes agregar el complemento "workBench" >>           ║
║                                                                             ║
║                ---->Developer Default                                       ║
║                ------->Next...Next..Next...                                 ║
║                ---------->Ingresa y Recuerda el password                    ║
║                ------------->finish                                         ║
║                                                                             ║
║                Si no instalaste workbench dentro del paquete mysql          ║
║                ¤ Ve a la web de mysql                                       ║
║                       https://dev.mysql.com/downloads/workbench/            ║
║                ¤ Ejecuta y sigue las instrucciones segun tu OS              ║
║                                                                             ║
║                                                                             ║
║           XAMPP                                                             ║
║                ¤ Ve a la web de apachefriends                               ║
║                     https://www.apachefriends.org/es/download.html          ║
║                ¤ Descarga en archivo dependiendo de tu OS                   ║
║                     Instala y recuerda el password de mysql                 ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
"""
												MYSQL
https://dev.mysql.com/downloads/mysql/  
https://codigosql.top/mysql/instalar-mysql-server-y-mysql-workbench-en-windows-10/
https://www.ecodeup.com/aprende-a-instalar-mysql-y-mysql-workbench-en-windows-10/

https://www.mysql.com/products/workbench/
												XAMPP
https://www.apachefriends.org/es/download.html
https://www.ionos.es/digitalguide/servidores/herramientas/instala-tu-servidor-local-xampp-en-unos-pocos-pasos/
https://www.mclibre.org/consultar/php/otros/xampp-instalacion-windows.html
https://www.solvetic.com/tutoriales/article/8154-como-instalar-y-configurar-xampp-en-windows-10/
"""
pausa();limpiar();
##################################################################################################################################
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║     Instalar en python MySQL // maria db                                    ║
║                  pip install mysql-connector                                ║
║                                                                             ║
║     LINUX                                                                   ║
║     como root zypper -n in mysql mysql-administration                       ║
║               zypper -n in mysql-client mysql-query-browser mysql-gui-tools ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");

print("""
* * * * * Sinoptico* * * * *
  Aplicaciones de Python.

  Distribuciones:
 -----------------
  Python ya viene con una gran biblioteca estándar, sin embargo existen algunas 'distribuciones' que pretenden extender al lenguaje con propósitos particulares. Aquí es posible consultar las diversas distribuciones de Python.
  Instalación:
 --------------
 Las principales distribuciones de GNU/Linux, los sistemas *BSD, así como Mac OS X y la mayoría de los UNIX vienen al menos con Python 2 preinstalado. Del mismo modo, las principales distribuciones de GNU/Linux cuentan con paquetes de instalación de Python 3.
  Las versiones más recientes de Python pueden ser descargadas desde el sitio principal de Python incluyendo binarios para Mac OS X y Windows e incluso es posible descargar el código fuente.

  NOTA Anaconda es una distribución de Python 2 y Python 3 especializada en cómputo científico, sin embargo es de muy fácil instalación y gestión tanto en Windows como en Mac OS X y GNU/Linux. Es una alternativa muy recomendable a las versiones oficiales de Python.
  Breve introducción a los lenguajes de programación.
  Un lenguaje es un conjunto de cadenas de símbolos con los que se pueden crear mensajes. De ese modo los mensajes son transmitidos de un emisor a un receptor. Aún cuando en la naturaleza se pueden identificar ciertos lenguajes, los seres humanos hemos desarrollado lenguajes de diversos tipos y gran complejidad.
  Los lenguajes constan principalmente de la gramática, la cual trata sobre la construcción del lenguaje, y la semántica, la cual trata sobre el significado del lenguaje.
""");
pausa();limpiar();
##################################################################################################################################

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║        para esta cursada debemos instalar las siguientes librerías          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
pip install --upgrade pip
pip install imutils
pip install tkintertable
pip install numpy
pip install pandas
pip install tkintertable
pip install opencv-python
pip install Pillow
pip install schedule
pip install plotly
pip install scipy
pip install -U matplotlib
pip install pytz
pip install nose
pip install sympy
pip install jupyter
pip install ipython

>>>>>>>       o   todo junto asi         ->>>>>

pip install imutils tkintertable numpy pandas tkintertable opencv-python Pillow schedule plotly scipy matplotlib pytz nose sympy jupyter ipython

Algunas más dificiles   https://tkdocs.com/tutorial/install.html    
		 pip install python-tk

sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose plotly

zypper -n in mysql mysql-administration mysql-client mysql-query-browser mysql-gui-tools
zypper -n in python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose plotly

""");
"""copia y pega en consola.........

pip install imutils tkintertable numpy pandas tkintertable opencv-python Pillow schedule plotly scipy matplotlib pytz nose sympy jupyter ipython

pip install mysql-connector-python



"""
pausa();limpiar();
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                         ╦     ╔═══════╗      ╔════════╗                     ║
║                         ║     ║       ╚╗     ║                              ║
║                         ║     ║        ║     ║                              ║
║                         ║     ║        ║     ║                              ║
║                         ║     ║        ║     ╠═══════╣                      ║
║                         ║     ║        ║     ║                              ║
║                         ║     ║       ╔╝     ║                              ║
║                         ╩  ¤  ╚═══════╝  ¤   ╚════════╝  ¤                  ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                                                             ║
║    ¤ Ve a la web de python.org                                              ║
║        http://www.python.org.ar/wiki/IDEs                                   ║
║        https://hackr.io/blog/best-python-ide                                ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║        https://www.geany.org/download/releases                              ║
║        ---------------------------------------                              ║
║                                                                             ║
║        Descargar y ejecutar la version de tu OS                             ║
║                                                                             ║
║        Windows x86-64 installer                                             ║
║                                                                             ║
║        macOS 64-bit installer                                               ║
║                                                                             ║
║        Linux x86-64 instaler                                                ║
║                                                                             ║
║           En linux y mac                                                    ║
║                                                                             ║
║           --->Ve a Build // construir                                       ║
║                                                                             ║
║           ------> Set Build Commands // Establecer comandos de construcción ║
║                                                                             ║
║               * En el 1er y último item  agrega el 3 luego de python        ║
║                 python.... debe quedar python3....                          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
"""
https://www.geany.org/download/releases/

Eclipse + pydev

Pydev es un plugin que permite a los usuarios usar Eclipse para el desarrollo de Python y Jython, haciendo de eclipse una IDE de primera clase para desarrollar python. Este plugin viene con muchas características, como por ejemplo complesión de código, resaltado de sintaxis, analizador de sintaxis, refactor, debug y muchos más.

http://pydev.sourceforge.net/ http://www.eclipse.org/
Netbeans (nbpython)

nbpython es una extensión de netbeans que permite utilizar esta IDE como entorno para desarrollos en python, algunas de sus características son el resaltado de sintaxis, complesión de código, soporte para proyectos python soporte para jython, soporte para pyunit, debugger, administración de versiones, manejo de la librería estándar, ejecución de scripts python etc.

https://nbpython.dev.java.net/ http://www.netbeans.org/
SPE IDE

Entorno de desarrollo multiplataforma para python

http://pythonide.blogspot.com/
Eric

Eric is una IDE para python y ruby, escrita en python. Esta basada en Qt, integrando el control de edición scintilla. Esta diseñado para ser usable ya sea como editor para pequeños scripts como así también para administración de proyectos profesionales. Eric provee un sistema de plugins que permite ser extendido fácilmente.

http://www.die-offenbachs.de/eric/index.html
Komodo Edit

Komodo Edit es un editor open source para expertos en lenguajes dinámicos.

http://www.activestate.com/Products/komodo_ide/komodo_edit.mhtml
Geany

Geany es un editor de texto que usa el toolkit GTK2 toolkit con funciones básicas de un entorno de desarrollo integrado. Es desarrollado para proveer de una IDE pequeña y rápida, que tenga pocas dependencias de otros paquetes. Soporta múltiples tipos de archivo y tiene algunas características muy interesantes.
"""
