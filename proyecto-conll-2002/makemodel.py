import sys, os

def makemodel(template, train, nombre_modelo, test, nombre_test):
	os.sys("../CRF++-0.58/crf_learn "+template+" "+train+" "+nombre_modelo+"")
	os.sys("../CRF++-0.58/crf_test -m"+nombre_modelo+" "+test+" >> "+nombre_test+"")


if __name__ == '__main__':
	makemodel()