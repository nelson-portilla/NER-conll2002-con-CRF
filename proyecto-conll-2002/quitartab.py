import sys, os

#Primera Caracteristica: Uno si la primera letra es Mayuscula, 0 lo contrario
def quitartab(entrada, salida):
	print "QUITANDO TABULACIONES"
	filas=open(entrada, 'r')
	salida=open(salida, 'w')
	texto=filas.read()
	texto=texto.replace("\t"," ")
	salida.write(texto)
	salida.close()
	filas.close()

#Segunda Caracteristica: Agrega el tipo
#addSecondCaracter()


if __name__ == '__main__':
	quitartab("a","b")