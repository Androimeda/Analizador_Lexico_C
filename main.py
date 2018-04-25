#### Importacion de archivos
import re
from reglas import *
from estados import *
from automata import *

#### Carga de archivo a examinar
filename  = "archivos/suma_dos.c"
file = open(filename, "r")
lineas = file.readlines()
file.close()

## ESTADOS DEL AUTOMATA
INIT = 0
ESTADO_ACTUAL = INIT


# INDICES DE TUPLAS, PARA REGLAS DEL AUTOMATA
ESTADO = 0
REGEX = 1
NOMBRE = 2

# COMPROBACION DE REGLAS Y CAMBIOS DE ESTADO SEGUN <AUTOMATA>

tokens=[]
nombre_tokens = []
# print(lineas)
c=1 # Contador de línea para deteccion de errores
cancela_analisis=False
for linea in lineas:
	linea = linea.replace("\t", "") # Se eliminan tabulaciones
	if not ("//" in linea): # Se omiten comentarios
		alcanza_fin_linea=False # valor bandera se dispara al encontrat el token \n
		while not alcanza_fin_linea:
			# Reglas aplicables para el estado actual ver automata.py
			reglas_estado = AUTOMATA[ESTADO_ACTUAL] 
			# Se vefica cada una de las reglas
			for regla in reglas_estado:
				token=''
				patron =re.compile("^"+regla[REGEX])
				match = patron.search(linea)
				# Si se encuentra aplicacion de regla
				if match:
					ESTADO_ACTUAL = regla[ESTADO] # Se cambia al estado que provee la regla
					token = match.group(0) # Se obtiene el token marcado
					tokens+=[token] # Se guarda en arreglo
					nombre_tokens+=[regla[NOMBRE]]
					linea = linea.replace(token,'',1) # Se elimina el token, para proseguir
					linea = linea.lstrip(' ') # Se elimina espacios en blanco al inicio de la 'nueva linea'
					if token == '\n': # Si se alcanza token de nueva_linea
						alcanza_fin_linea = True
					break # Sale del for
			
			if token == '': # Significa que ninguna regla pudo aplicarse, 
				print("Error de sintaxis en la linea "+str(c))
				print("Cerca del token "+str(tokens[-1]))
				print(ESTADO_ACTUAL, "Vea estado")
				cancela_analisis=True
				break #Sale del while
				#	automata inconcluso, error de sintaxis
			
			if alcanza_fin_linea:
				c+=1 # Aumenta en uno el contador de línea
				break # Sale del while

	if cancela_analisis:
		break # Sale del for
	
	if "//" in linea:
		c+=1
	
print nombre_tokens