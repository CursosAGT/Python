from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos(x):
	#Con tab colocaremos aquí las practicas hechas
	pass

####################                  CSV(texto separado por comas)
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                  CVS                                        ║
║                       Abre tu planilla de calculo                           ║
║    Ve el archivo desde_plan_calculo.csv  modifica algun dato (no nombre)    ║
║    y guardalo. Continia con este archivo.                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
aguarde""");

#################################################################
#IO_ext Ej_01;

import csv

with open('desde_plan_calculo.csv', newline='') as archivo_de_csv:
	csv_a_memoria = csv.reader(archivo_de_csv)
	for Columna in csv_a_memoria:
		print(Columna)
nuevo(1);
print("Aqui puedo seleccionar que carácter uso como separación")
with open('desde_plan_calculo.csv', newline='') as archivo_de_csv:
	csv_a_memoria = csv.reader(archivo_de_csv, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
	for Columna in csv_a_memoria:
		print(Columna)

nuevo(2);
import csv
archivo = open('salida_a_csv2.csv', 'w')
with archivo:
	writer = csv.writer(archivo)
	writer.writerows([{ 'B', 'Alex', 'Brian'},
					  { 'A', 'Rachael', 'Rodriguez'},
					  { 'C', 'Tom', 'smith'},
					  { 'B', 'Jane', 'Oscar'},
					  { 'A', 'Kennzy', 'Tim'}])
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║    Grabamos el archivo salida_a_csv2.csv                                    ║
║                       Abrelo tu planilla de calculo                         ║
║    Ve el archivo salida_a_csv2.csv  y compaalo con salida de python         ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
aguarde""");



pausa()
archivo = open('salida_a_csv3.csv', 'w')
with archivo:
	fieldnames = ['Grado','Nombre', 'Apellido', 'Grado']
	writer = csv.DictWriter(archivo, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows([{'Grado': 'B', 'Nombre': 'Alex', 'Apellido': 'Brian'},
					  {'Grado': 'A', 'Nombre': 'Rachael','Apellido': 'Rodriguez'},
					  {'Grado': 'C', 'Nombre': 'Tom', 'Apellido': 'smith'},
					  {'Grado': 'B', 'Nombre': 'Jane', 'Apellido': 'Oscar'},
					  {'Grado': 'A', 'Nombre': 'Kennzy', 'Apellido': 'Tim'}])
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║    Grabamos el archivo salida_a_csv3.csv                                    ║
║                       Abrelo tu planilla de calculo                         ║
║    Ve el archivo salida_a_csv3.csv  y compaalo con salida de python         ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
aguarde""");
nuevo(3);
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                      Ya importamos y exportamos a                           ║
║                         la planilla de calculo                              ║
║                                                                             ║
║                      AHORA JUGUEMOS CON LOS DATOS                           ║
║                                                                             ║
║   Necesitamos instalar varias librerias                                     ║
║                  pip install pandas                                         ║
║                  pip install -U numpy                                       ║
║                  pip install -U matplotlib                                  ║
║                  pip install plotly                                         ║
║                  pip install scipy                                          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
\n\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                     Pandas                                  ║
║  https://www.doctormetrics.com/importando-datos-en-python/                  ║
║  https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html      ║
║  https://pandas.pydata.org/docs/getting_started/index.html#getting-started  ║
║                            pip install pandas                               ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
aguarde....
Buscando las cabeceras "nombre de columnas"
""");

import pandas as pd
df = pd.read_csv('desde_plan_calculo.csv')

print("Abro el archivo 'desde_plan_calculo.csv'" )
print("dataframe = df")
for Columna in df:
	print(Columna)
pausa()

print("Imprimo la columna Dato1")
print(df['Dato1'])
pausa()

print("Invierto la columna Dato1 x Dato3")
print("Antes:\n",df)

df[['Dato3','Dato1']]=df[['Dato1','Dato3']]
print("Despues:\n",df)
pausa()

print("original\n",df)
print(".loc if you want to label index.")

print("Imprimo los index 0 a 5 de Dato2")
print(df.loc[:5])#gets Columnas (or columns) with particular labels from the index
pausa()
print(df.loc[8:15])#c gets Columnas (or columns) at particular positions in the index (so it only takes integers).
pausa()
print(df.loc[5:])
pausa()
print(df.loc[df.index[[0,2,3,4,5]],'Dato2'])
pausa()
print("After index slicing: print(df.loc[10:20, 'Dato1'] )") 
print(df.loc[10:20, 'Dato1'] )
pausa()
print("La estructura es [fila Inicial : fila Final, columna inicial : columna final] -df.loc[FI:FF,CI:CF ]")
print(df.loc[:, 'DatoALF'])
pausa()
print(df.loc[:,'Dato1':'Dato5'])
pausa()
print("La estructura es [[Lista de filas],[lista de columnas]] -df.loc[[listaFila],[ListaColumnas]]")
print(df.loc[[1,2,3,4,5,6,7,8,9],])
pausa()

print(df.loc[:,['Dato1', 'Dato4', 'Dato2']])
pausa()

print(df.loc[:, 'DatoALF'])
print(".iloc if you want to positionally index.\n")
#print(df.loc[df.index[[:,5] )
print(df.iloc[:,[4, 5, 6]])
pausa()

print("print(df.iloc[:,6])")
print(df.iloc[:,6])
pausa()
print(df.iloc[:, [2,4]])
pausa()
print(df.iloc[:,2])
pausa()
print("Imprimo la 5ta columna Datos >1000")
print(df.loc[df.iloc[:,2]>1000])
pausa();
print("Imprimo criterios lambda")
criterio = df['DatoALF'].map(lambda x: x.startswith('b'))
print(criterio)
pausa()

print("Imprimo la columna Dato4 ordenada ascendente")
print(df.sort_values(by='Dato4'))
pausa()
print("Imprimo la columna Dato4 ordenada descendente")
print(df.sort_values(by='Dato4',ascending=False))
pausa()
print("utilizamos los métodos head, que sería cabeza, para mostrar las primeras filas del marco de datos.")
print(df.head())
print("utilizamos tail o cola, que muestra las filas inferiores de los datos.")
print(df.tail())
nuevo(4);

print("Antes\n",df.head())
cabecera = ["ID", "Columna_1", "Columna_2", "Columna_3", "Columna_4", "Columna_5", "Columna_6"]
print("Reemplazo nombres de columnas.")
df.columns = cabecera
df.head()
print("Después\n",df.head())
salida='salida_a_csv.csv'
df.to_csv(salida)

nuevo(5);

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                   Plotly                                    ║
║                             pip install plotly                              ║
╚═════════════════════════════════════════════════════════════════════════════╝
aguarde""");
#desde la web
import pandas as pd
import plotly.express as px
print("importo el archivo desde un sitio web")
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
print("Desde la web\n",df.head())
print("Abriendo el navegador web")
fig = px.line(df, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')
fig.show()

nuevo(6);
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
print("Desde la web\n",df.head())
fig = go.Figure(go.Scatter(x = df['AAPL_x'], y = df['AAPL_y'],
				  name='Share Prices (in USD)'))

fig.update_layout(title='Apple Share Prices over time (2014)',
				   plot_bgcolor='rgb(230, 230,230)',
				   showlegend=True)

fig.show()
nuevo(7);


print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                    Numpy                                    ║
║          https://www.doctormetrics.com/importando-datos-en-python/          ║
║                           pip install -U numpy                              ║
╚═════════════════════════════════════════════════════════════════════════════╝
aguarde""");

import numpy as np
print("""
Si en nuestro archivo tenemos datos de diferentes tipos, podemos usar dos funciones: genfromtext() y recfromcsv().
Cuando exista cabecera, especificaremos names=True.
Al pasar el argumento dtype=None, la función averigua qué tipo corresponde a cada columna.
""")
# Cargamos el fichero como el array: datos
#dato = np.loadtxt('desde_plan_calculo.csv' , delimiter=',')		recfromcsv

df = np.recfromcsv('desde_mapa.csv', delimiter=',', names=True, dtype=None)
for Columna in df:
	print(Columna)
nuevo(8);
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                 Matplotlib                                  ║
║                         pip install -U matplotlib                           ║
╚═════════════════════════════════════════════════════════════════════════════╝
""");
import csv
import numpy as np
import matplotlib.pyplot as plt

data_path = 'desde_mapa.csv'
with open(data_path, 'r') as f:
	reader = csv.reader(f, delimiter=',')
	# get header from first Columna
	headers = next(reader)
	# get all the Columnas as a list
	data = list(reader)
	# transform data into numpy array
	data = np.array(data).astype(float)

print(headers)
print(data.shape)
print(data[:3])

print("primera pantalla\n cerrarla para continuar")
# Plot the data
plt.plot(data[:, 1], data[:, 0])
plt.axis('equal')
plt.xlabel(headers[1])
plt.ylabel(headers[0])
plt.show()
print("segunda pantalla\n cerrarla para continuar")
plt.plot(data[:, 2])
plt.xlabel('Tablas Index')
plt.ylabel(headers[2])
plt.show()
plt.close()
nuevo(9);


import matplotlib.pyplot as plt
import numpy as np

x,y= np.loadtxt('desde_2c.txt', delimiter=',', unpack=True)
plt.plot(x,y, marker='o')

plt.title('Datos desde archivo externo delimitado txt via  por función "delimiter" en python')
print("Datos desde archivo externo delimitado txt via  por función 'delimiter' en python")
plt.xlabel('Cantidad de gente')
plt.ylabel('Gastos')
print("Pantalla grafica\n cerrarla para continuar")
plt.show()
plt.close()
nuevo(10);

import pandas as pd
import matplotlib.pyplot as plt
print('Datos archivo externo delimitado csv via archivo delimitado por tipo de archivo importado')
plt.title('Datos archivo externo delimitado csv ')
dataframe = pd.read_csv("desde_2c.csv")
x = dataframe.dato_x
y = dataframe.dato_y
plt.scatter(x, y)


print("Ver en directorio local que se exporto la pantalla a un archivo png")
plt.show()
plt.savefig("imagen1_desde_cvs.png")
plt.close()
nuevo(11);
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                   Plotly                                    ║
║                             pip install scipy                               ║
╚═════════════════════════════════════════════════════════════════════════════╝
aguarde""");
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

dataframe = pd.read_csv("desde_3c.csv")

x = dataframe.dato_x
y = dataframe.dato_y

stats = linregress(x, y)
print("La linea roja es la regresión lineal")
m = stats.slope
b = stats.intercept
print("Pantalla grafica\n cerrarla para continuar")
plt.scatter(x, y)
plt.plot(x, m * x + b, color="red")   # I've added a color argument here
print("Ver en directorio local que se exporto la pantalla a un archivo png")

plt.show()
plt.savefig("imagen2_desde_cvs.png")
plt.close()
nuevo(12);
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

dataframe = pd.read_csv("scottish_hills.csv")

x = dataframe.Height
y = dataframe.Latitude

stats = linregress(x, y)

m = stats.slope
b = stats.intercept

# Change the default figure size
plt.figure(figsize=(10,10))

# Change the default marker for the scatter from circles to x's
plt.scatter(x, y, marker='x')
print("La linea azul es la regresión lineal")
# Set the linewidth on the regression line to 3px
plt.plot(x, m * x + b, color="blue", linewidth=3)

# Add x and y lables, and set their font size
plt.xlabel("Altura (m)", fontsize=20)
plt.ylabel("Latitud", fontsize=20)

# Set the font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.savefig("imagen3_desde_cvs.png")
print("Pantalla grafica\n cerrarla para continuar")
plt.show()
plt.close()
nuevo(13,"fin");
