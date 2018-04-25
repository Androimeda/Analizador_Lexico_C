# AUTOMATA FINITO
# Se presenta como un dict de python
# Cada llave representa un estado del automata (estado de salida)
# El valor corresponde a una lista con
### [0]: El estado de llegada
### [1]: La regla de salida
### [2] El nombre de la regla de salida

from reglas import *
AUTOMATA = {
	0:[(1,'(INT|VOID)', "TIPO_MAIN")],
	1:[(2,'main',"MAIN")],
	2:[(3,iz_parent, "parent_izq")],
	3:[(4,var_num, "var_num")],
	4:[(5,de_parent,"parent_der")],
	5:[(6,"\{", "iz_brack")],
	6:[(7,nueva_linea, "nueva_linea")],
	7:[(8,tipo, "tipo"),(21,"FOR\s+\(", "OPEN_FOR"),(15,var, "var"),(37,'\}', "llave_der"), (7, '\n', "nueva_linea")],
	8:[(9,var, "var")],
	9:[(8,coma, "coma"),(10,igual, "igual"),(14,punto_coma, "punto_coma")],
	10:[(11,var_num, "var_num"),(12,iz_parent, "parent_izq")],
	11:[(10,op, "op"),(8,coma, "coma"),(14,punto_coma, "punto_coma")],
	12:[(13,var_num, "var_num")],
	13:[(11,de_parent, "parent_der"),(12,op, "op")],
	14:[(7,nueva_linea, "nueva_linea")],
	15:[(16,igual, "igual")],
	16:[(17,var_num, "var_num"),(19,iz_parent, "parent_izq")],
	17:[(16,op, "op"),(18,punto_coma, "punto_coma")],
	18:[(7,nueva_linea, "nueva_linea")],
	19:[(20,var_num, "var_num")],
	20:[(17,de_parent, "parent_der"),(19,op, "op")],
	21:[(22,tipo, "tipo"),(38,var, "var")],
	22:[(23,var, "var")],
	23:[(24,igual, "igual")],
	24:[(25,iz_parent, "parent_izq"),(27,var_num, "var_num")],
	25:[(26,var_num, "var_num")],
	26:[(25,op, "op"),(27,de_parent, "parent_der")],
	27:[(24,op, "op"),(28,punto_coma, "punto_coma")],
	28:[(29,var, "var")],
	29:[(30,op_comp, "op_comp")],
	30:[(31,var_num, "var_num")],
	31:[(32,punto_coma, "punto_coma")],
	32:[(33,var, "var")],
	33:[(34,"(\+\+|\-\-)", "paso")],
	34:[(35,de_parent, "parent_der")],
	35:[(36,"\{","iz_brack")],
	36:[(7,nueva_linea, "nueva_linea")],
	37:[(7,"\n","nueva_linea")],
	38:[(39,igual, "igual")],
	39:[(40,var_num, "var_num"),(41,iz_parent, "parent_izq")],
	40:[(43,punto_coma, "punto_coma"),(39,op, "op")],
	41:[(42,var_num, "var_num")],
	42:[(40,de_parent, "parent_der"),(41,op, "op")],
	43:[(29,var, "var")]
}