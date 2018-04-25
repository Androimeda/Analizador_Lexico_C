# Analizador Léxico 
Script de deteccion de sitaxis para un bloque de C (FOR, ASIGNACIONES, DECLARACIONES)

# Uso:
```bash
python main.py
```

# GFC
```
-- GFC--
bloque--> (INT|VOID) 'main (VOID) ' '{' Cuerpo '}'
cuerpo --> (declaracion|asignacion|ciclo)
ciclo--> cabecera_ciclo '{' cuerpo '}'
cabecera_ciclo --> 'FOR''('(asignacion|declaracion)';' exp.bool ';'var ('++'|'--')'}'
declaracion -->  tipo var (=expresion)? (',' var (=expresion)?)* ';'
asignacion--> var '=' expresion
tipo--> ('INT'|'FLOAT'|'DOUBLE'|'SHORT'|'BIGINT'|'NUMBER')
expresion --> expresion '+' termino | expr '-' termino| termino
termino--> termino '*' factor| termino '/' factor| factor
factor-->'('expresion ')' |var |numero
var --> letra (letra|'_'|digito)*
numero --> (entero|float)
entero --> digito digito *
float--> (entero exponente| decimal(exponente|ε))
decimal --> digito(.digito|digito.) digito*
letra--> [a-zA-Z]
digito--> [0-9]
```

# Autómata Finito
![Automata](https://ajedrez92.files.wordpress.com/2018/04/automatafinito.png)

# Ejemplos de código Analizado
1. Cálculo del factorial de un número
```c
INT main(VOID){
//Factorial de un numero
	INT num, factorial, i;
	factorial=1;
	num=20;
	FOR (i=1; i<=num; i++){ 
		factorial=factorial*1;
	}
}

```
2. Cálculo del promedio para calificaciones
```c
// Calculo de promedio para calificaciones
INT main(VOID){
	INT n, suma, nota1, nota2, nota3;
	DOUBLE promedio;
	nota1=90;
	nota2=87;
	nota3=88;
	suma=nota1+nota2+nota3;
	promedio=suma/3;
}
```
3. Suma

```c
//Suma Los numeros de 2 en 2, hata llegar al 100
INT main(VOID){
INT par=0;
	FOR (INT i = 1; i < 100; i++){
		par = par+2;
	}
}
```
4. Suma
```c
INT main(VOID){
	INT num,suma;
	suma=0;
	FOR (num = 0; i < 10; num++){
		suma=suma+num;
	}
}
```
