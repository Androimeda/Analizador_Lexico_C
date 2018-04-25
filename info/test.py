#### Importacion de archivos
import re
from reglas import *
from estados import *
from automata import *

## ESTADOS DEL AUTOMATA
INIT = 7
ESTADO_ACTUAL = INIT

# COMPROBACION DE REGLAS Y CAMBIOS DE ESTADO SEGUN <AUTOMATA>


linea = "}\n}"
alcanza_fin_linea=False
while not alcanza_fin_linea:
	reglas_estado = AUTOMATA[ESTADO_ACTUAL]
	for r in reglas_estado:
		patron =re.compile(r[1])
		match = patron.search(linea)
		if match:
			ESTADO_ACTUAL = r[0]
			token = match.group(0)
			linea = linea.replace(token,'',1)
			if token == '\n':
				alcanza_fin_linea = True
			break
	# f.write(r[2]+" ")
	print(ESTADO_ACTUAL)
	if alcanza_fin_linea:
		break