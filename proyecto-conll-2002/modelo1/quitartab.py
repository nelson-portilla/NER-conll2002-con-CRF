import sys, os

#Primera Caracteristica: Uno si la primera letra es Mayuscula, 0 lo contrario
def quitartab():
	filas=open("salida.txt", 'r')
	salida=open("nueva_salida", 'w')
	texto=filas.read()
	texto=texto.replace("\t"," ")
	salida.write(texto)
	salida.close()
	filas.close()

#Segunda Caracteristica: Agrega el tipo
#addSecondCaracter()


if __name__ == '__main__':
	quitartab()