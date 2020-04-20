#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  1.py
#  
#  Copyright 2020 Facundo <Facundo@DESKTOP-881079A>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
def par(a,b,cambio):

	if a>=b:
		mayor,menor=a,b;
	else:
		mayor,menor=b,a;
		cambio+=1;

	return (mayor,menor,cambio);


org=[0,87,77,35,1,32,98,56,87,36,66,32,44,3,89,55,4,2];
lista=[0,87,77,35,1,32,98,56,87,36,66,32,44,3,89,55,4,2];

ordenado = True;
ciclos=0;
while ordenado:
	cambio = 0;
	ciclos+=1
	for contador in range (1,len(lista)):
		lista[contador-1],lista[contador],cambio=(par(lista[contador-1],lista[contador],cambio));
	if cambio == 0:
		ordenado=False;
print(lista)
print("ciclos:",ciclos)
print("---------------------------------------------")
print(org)
org.sort()
print(org)
org.sort(reverse=True)
print(org)
