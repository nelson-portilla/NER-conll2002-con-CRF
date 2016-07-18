import sys, os

def calculo_PR(entrada, salida):
	tabla=str(os.popen("echo | perl conlleval.pl -r -o NOEXIST < "+entrada).read())
	res=open(salida, 'w')
	res.write(tabla)
	res.close()


if __name__ == '__main__':
	calulo_PR()
	