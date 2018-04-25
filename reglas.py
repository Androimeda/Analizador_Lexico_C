# REGLAS USADAS EN EL AUTOMATA
#
digito="[0-9]"
letra="[a-zA-Z]"
var = letra+"("+letra+"|_|"+digito+")*"
tipo="(INT|FLOAT|DOUBLE|SHORT|BIGINT|NUMBER)"
entero = digito+digito+"*"
decimal=digito+"(\."+digito+"|"+digito+"\.)"+digito+"*"
exponente="(E|e)(\+|\-)?"+entero
flotante="("+entero+exponente+"|"+decimal+"("+exponente+")?)"
numero="("+flotante+"|"+entero+")"

var_num = "("+var+"|"+numero+")"

iz_parent="\("
de_parent="\)"
igual="="
op="(\+|\-|\*|\/)"
op_comp ="(>=|<=|<|>)"
nueva_linea = "\n"
punto_coma = ";"
coma=","