# -*- coding: utf-8 -*-
import sys, os
reload(sys)
sys.setdefaultencoding('utf8')
import codecs

def addFeatures(pathin, pathout):
	filas=codecs.open(pathin, 'r', "ISO-8859-1")
	cont=0
	for linea in filas:
		lista=linea.split()
		if(len(lista)==8):
			1
		else:
			print "NO",cont
		cont+=1

if __name__ == '__main__':
	print "Iniciando creacion de archivos..."
	#***Se envia un archivo train a modificar y un nombre para la salida
	#***OJO: el train que se envia ya debe tener el modelo 1
	#***Es decir ya debe tener 4 columnas.
	addFeatures("train","train")