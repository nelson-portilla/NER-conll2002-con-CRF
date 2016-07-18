# -*- coding: utf-8 -*-
import sys, os
reload(sys)
sys.setdefaultencoding('utf8')
import codecs
import quitartab, calculoPR, makemodel

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

def listaDeSoloEagles(listaAM):
			#Obtenemos toda las etiquetas eagles de la palabra con el ciclo 
			n=int(round(len(listaAM)/3))
			#-----------Reiniciamos lista de eagles y agregamos la primera q esta en la posicion 2
			listaeagles=[]
			listaeagles.append(listaAM[2])
			#Obtenemos toda las etiquetas eagles de la palabra con el ciclo 
			y=2
			# print "Tiene:", n
			for i in range(2,n+1):				
				listaeagles.append(listaAM[y+3])
				y+=3	
			return listaeagles


def addFeatures(pathin, pathout):
	diccionario={'A':[1,3,4,0], 'R':[1,0,0,0]}
	filas=codecs.open(pathin, 'r', "ISO-8859-1")
	binario={'True':"1", 'False':"0"}
	salidam2=open("modelo2/"+pathout, 'a')
	salidam3=open("modelo3/"+pathout, 'a')
	salidam4=open("modelo4/"+pathout, 'a')
	salidam5=open("modelo5/"+pathout, 'a')
	cont=1
	for linea in filas:
		print cont
		if (linea[0]!='\n'):
			# print "\n\n------NUEVA LINEA-------\n\n"			
			lista=linea.split()
			# print "***\npalabra para analize: ", str(lista[0])
			post = lista[1]
			# print "Cateoria: ", post
			word=str(lista[0])
			if(word=='"'):
				word="'"
			listaAM=str(os.popen("echo "+'"'+word+'"'+" | analyze -f am.cfg").read()).split()			
			# print "LISTA analye: ",listaAM
			listaeagles=listaDeSoloEagles(listaAM)
			# print "Lista de eagles: ",listaeagles
			# print "eagles: ",listaeagles
			#--Obtiene la lista del diccionario, le entrego la primera letra del postag
			ls= dic[post[0]]
			#Se arma una lista de las primeras letras de la listaEagles y se consulta posicion donde coincida categoria	
			try:
				index = [i[0] for i in listaeagles].index(post[0])
				# print "Posicion Index ",index
				eagles_sing = listaeagles[index]
				# print "Eagles coincidente ",eagles_sing
			except Exception, e:
				# print "NO coincide la CATEGORIA"
				eagles_sing = listaeagles[0]				
			
			try:
				tipo= eagles_sing[ls[0]]
				# print tipo
			except IndexError:
				tipo = "0"
				# print "no tipo"
			try:
				genero= eagles_sing[ls[1]]
				# print genero
			except IndexError:
				genero="0"
				# print "no genero"
			try:
				numero= eagles_sing[ls[2]]
				# print numero
			except IndexError:
				numero="0"
				# print "no numero"
			try:
				persona= eagles_sing[ls[3]]
				# print persona
			except IndexError:
				persona="0"
				# print "no persona"
			
			# print "Lista Inicial: ", lista

			lista.insert(3, tipo)
			for palabra in lista:
				# print "Escribiendo modelo 2..."
				salidam2.write(str(palabra+" "))
			salidam2.write("\n")
			
			lista.insert(4, genero)
			for palabra in lista:
				# print "Escribiendo modelo 3..."
				salidam3.write(str(palabra+" "))
			salidam3.write("\n")
			
			
			lista.insert(5, numero)
			for palabra in lista:
				# print "Escribiendo modelo 4..."
				salidam4.write(str(palabra+" "))
			salidam4.write("\n")

			lista.insert(6, persona)
			for palabra in lista:
				# print "Escribiendo modelo 5..."
				salidam5.write(str(palabra+" "))
			salidam5.write("\n")
		cont+=1
			# print "lista NUEVA: ", lista



	salidam2.close()
	salidam3.close()
	salidam4.close()
	salidam5.close()
	filas.close()




if __name__ == '__main__':
	print "Iniciando creacion de archivos..."
	#***Se envia un archivo train a modificar y un nombre para la salida
	#***OJO: el train que se envia ya debe tener el modelo 1
	#***Es decir ya debe tener 4 columnas.
	# addFeatures("train-Modelo1","train")
	print "TRAIN Exito, Creando Test..."
	# addFeatures("test-Modelo1","test")
	print "Caracteristicas Agregadas con exito...\nIniciando creacion de modelos"



	for x in range(5,6):
		print "Calculando Modelo, Transformando salida y calculando PR del modelo ",x
		# makemodel.makemodel(template, train, nombre_modelo, test, nombre_test)
		makemodel.makemodel("modelo"+str(x)+"/template", "modelo"+str(x)+"/train", "modelo"+str(x)+"/modelo", "modelo"+str(x)+"/test", "modelo"+str(x)+"/salida")
		quitartab.quitartab("modelo"+str(x)+"/salida", "modelo"+str(x)+"/nueva_salida")
		calculoPR.calculo_PR("modelo"+str(x)+"/nueva_salida", "modelo"+str(x)+"/tabla-PR")
	print "Archivos creados exitosamente..."
	