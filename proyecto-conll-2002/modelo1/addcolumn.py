import sys, os

#Primera Caracteristica: Uno si la primera letra es Mayuscula, 0 lo contrario
def addFirstFeature(pathin, pathout):
	diccionario={'A':[1,3,4,0], 'R':[1,0,0,0]}
	filas=open(pathin, 'r')
	salida=open(pathout, 'w')
	binario={'True':"1", 'False':"0"}
	for linea in filas:
		if (linea[0]!='\n'):					
			flag=linea[0].isupper()
			lista=linea.split()
			lista.insert(2,binario[str(flag)])		
			for palabra in lista:
				salida.write(str(palabra+" "))
			salida.write("\n")
	salida.close()
	filas.close()

#Segunda Caracteristica: Agrega el tipo
#addSecondCaracter()


if __name__ == '__main__':
	print "Iniciando..."
	addFirstFeature("esp.train","train")
	# addFirstCaracter("mytrain","modelo1/train")
	addFirstFeature("esp.testb","test")