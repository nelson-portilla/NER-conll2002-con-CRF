import sys, os

#Primera Caracteristica: Uno si la primera letra es Mayuscula, 0 lo contrario
def createEagles(pathin, pathout):
	diccionario={'A':[1,3,4,0], 'R':[1,0,0,0]}
	filas=open(pathin, 'r')
	salida=open(pathout, 'w')
	for linea in filas:
		if (linea[0]!='\n'):			
			lista=linea.split()
			print "antes de analize: ", str(lista[0])
			listaAM=str(os.popen("echo '"+str(lista[0])+"' | analyze -f am.cfg").read()).split()
			print "LISTA analye: ",listaAM
			print "Eagles primero: ",listaAM[2]
			eagles=listaAM[2]
			salida.write(str(eagles+"\n"))
	salida.close()
	filas.close()

#Segunda Caracteristica: Agrega el tipo
#addSecondCaracter()


if __name__ == '__main__':
	print "Iniciando..."
	createEagles("train","listaEagles")
	print "Lista creada exitosamente..."
	# addFirstCaracter("mytrain","modelo1/train")
	# addFirstFeature("esp.testb","test")