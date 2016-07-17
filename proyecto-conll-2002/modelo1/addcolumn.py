import sys, os
#tipo, genero, numero, persona
dic= {
	'A': [1, 3, 4],
	'R':[1],
	'D':[1,3,4,2],
	'N': [1,2,3],
	'V': [1,6,5,4],
	'P': [1,3,4,2],
	'C':[1],
	'I':[],
	'S':[1,2,3],
	'F':[],
	'Z':[1],
	'W':[],
}

def getEagles(palabra):
	listaAM=str(os.popen('echo '+palabra+'| analyze -f am.cfg').read()[:-1]).split()
	eagles=listaAM[1:]
	return eagles

#Primera Caracteristica: Uno si la primera letra es Mayuscula, 0 lo contrario
def addFirstFeature(pathin, pathout):
	diccionario={'A':[1,3,4,0], 'R':[1,0,0,0]}
	filas=open(pathin, 'r')
	salida=open(pathout, 'w')
	binario={'True':"1", 'False':"0"}
	for linea in filas:
		if (linea[0]!='\n'):
			lista=linea.split()		
			firstfeature=linea[0].isupper()
			word = lista[0]
			post = lista[1]
			eagles = getEagles(word)
			print eagles
			ls= dic[post[0]]
			index = [int(i[0]) for i in eagles].index(post[0])
			eagles_sing = eagles[index]
			print eagles_sing
			try:
				tipo= eagles_sing[ls[0]]
				print tipo
			except IndexError:
				tipo = 0
				print "no tipo"
			try:
				genero= eagles_sing[ls[1]]
				print genero
			except IndexError:
				genero=0
				print "no genero"
			try:
				numero= eagles_sing[ls[2]]
				print numero
			except IndexError:
				numero=0
				print "no numero"
			try:
				persona= eagles_sing[ls[3]]
				print persona
			except IndexError:
				persona=0
				print "no persona"
			lista.insert(2,binario[str(firstfeature)])
			lista.insert(3, tipo)
			for palabra in lista:
				salida.write(str(palabra+" "))
			salida.write("\n")
	salida.close()
	filas.close()

#Segunda Caracteristica: Agrega el tipo
#addSecondCaracter()


if __name__ == '__main__':
	#print "Iniciando..."
	addFirstFeature("esp.train","train")
	# addFirstCaracter("mytrain","modelo1/train")
	addFirstFeature("esp.testb","test")