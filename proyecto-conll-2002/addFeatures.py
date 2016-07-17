# -*- coding: utf-8 -*-
import sys, os
reload(sys)
sys.setdefaultencoding('utf8')

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
			print "Tiene:", n
			for i in range(2,n+1):				
				listaeagles.append(listaAM[y+3])
				y+=3	
			return listaeagles


def addFeatures(pathin, pathout):
	diccionario={'A':[1,3,4,0], 'R':[1,0,0,0]}
	filas=open(pathin, 'r')
	binario={'True':"1", 'False':"0"}
	salidam2=open("modelo2/"+pathout, 'w')
	salidam3=open("modelo3/"+pathout, 'w')
	salidam4=open("modelo4/"+pathout, 'w')
	salidam5=open("modelo5/"+pathout, 'w')

	for linea in filas:
		if (linea[0]!='\n'):
			print "\n\n------NUEVA LINEA-------\n\n"			
			lista=linea.split()
			print "Palabra para analize: ", str(lista[0])
			post = lista[1]
			print "Cateoria: ", post
			listaAM=str(os.popen("echo '"+str(lista[0])+"' | analyze -f am.cfg").read()).split()
			# print "LISTA analye: ",listaAM
			listaeagles=listaDeSoloEagles(listaAM)
			# print "Lista de eagles: ",listaeagles
			print "eagles: ",listaeagles
			#--Obtiene la lista del diccionario, le entrego la primera letra del postag
			ls= dic[post[0]]
			#Se arma una lista de las primeras letras de la listaEagles y se consulta posicion donde coincida categoria	
			try:
				index = [i[0] for i in listaeagles].index(post[0])
				print "Posicion Index ",index
				eagles_sing = listaeagles[index]
				print "Eagles coincidente ",eagles_sing
			except Exception, e:
				print "NO coincide la CATEGORIA"					
			
			try:
				tipo= eagles_sing[ls[0]]
				print tipo
			except IndexError:
				tipo = "0"
				print "no tipo"
			try:
				genero= eagles_sing[ls[1]]
				print genero
			except IndexError:
				genero="0"
				print "no genero"
			try:
				numero= eagles_sing[ls[2]]
				print numero
			except IndexError:
				numero="0"
				print "no numero"
			try:
				persona= eagles_sing[ls[3]]
				print persona
			except IndexError:
				persona="0"
				print "no persona"
			
			print "Lista Inicial: ", lista

			lista.insert(3, tipo)
			for palabra in lista:
				print "Escribiendo modelo 2..."
				salidam2.write(str(palabra+" "))
			salidam2.write("\n")
			
			lista.insert(4, genero)
			for palabra in lista:
				print "Escribiendo modelo 3..."
				salidam3.write(str(palabra+" "))
			salidam3.write("\n")
			
			
			lista.insert(5, numero)
			for palabra in lista:
				print "Escribiendo modelo 4..."
				salidam4.write(str(palabra+" "))
			salidam4.write("\n")

			lista.insert(6, persona)
			for palabra in lista:
				print "Escribiendo modelo 5..."
				salidam5.write(str(palabra+" "))
			salidam5.write("\n")

			print "lista NUEVA: ", lista



	salidam2.close()
	salidam3.close()
	salidam4.close()
	salidam5.close()
	filas.close()

#Segunda Caracteristica: Agrega el tipo
#addSecondCaracter()


if __name__ == '__main__':
	print "Iniciando..."
	#Se envia un archivo train a modificar y un nombre para la salida
	#OJO: el train que se envia ya debe tener el modelo 1
	#Es decir ya debe tener 4 columnas.
	addFeatures("mytrain","train")
	print "Archivos creados exitosamente..."
	# addFirstCaracter("mytrain","modelo1/train")
	# addFirstFeature("esp.testb","test")