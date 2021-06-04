import cv2
import numpy as np
import shutil
import sys

rutaImagenes="imagenes"
rutaTest="val"
rutaFold="fold"
rutaTrain="train"
rutaVal="test"
rutaXml="xml"

def sacarImagenes(fichero):
	lineas = len(open(rutaFold+"/"+fichero).readlines())
	f=open(rutaFold+"/"+fichero,"r")
	contador=0
	

	imagenes=[''] * (lineas)
	



	while(True):
	    linea = f.readline()
	    corte1=linea.find(nombreACortar) 
	    corte2=linea.find(".json")  
	    try:	    		   
	    	imagenes[contador]=linea[corte1+len(nombreACortar)+1:corte2]  
	    	print(imagenes[contador])	   

	    except:
	    	print("Fin de las imagenes")
	    contador=contador+1
	    if not linea:
	        break
	return imagenes


def nombreXml(nombre):
	nombrexml=nombre[:-4]
	nombrexml=nombrexml+".xml"
	return nombrexml

def comprobarArgv(argumento):
	valor=640
	try:
		valor=sys.argv[argumento]
	except: 
		print("no hay argumento "+ str(argumento))		
	return valor

def comprobarCarpetaFold():
	directorio="b-59-850"
	try:
		directorio=sys.argv[3]
	except: 
		print("no especificado el nombre de la carpeta fold")		
	return directorio
#///////////////////////
print("iniciamos el escalado")
ancho=int(comprobarArgv(1))
alto=int(comprobarArgv(2))
nombreACortar=comprobarCarpetaFold()
print(nombreACortar)

iTest=sacarImagenes("test.txt")
iTrain=sacarImagenes("train.txt")
iVal=sacarImagenes("val.txt")







for imagen in iTest:

	if imagen != "":
		image=cv2.imread("imagenes/"+imagen)
		imageOut=cv2.resize(image,(ancho,alto),interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(rutaTest+"/"+imagen, imageOut)
		nombrexml=nombreXml(imagen)		
		shutil.move(rutaXml+"/"+nombrexml, rutaTest+"/"+nombrexml)


for imagen in iTrain:

	if imagen != "":
		image=cv2.imread("imagenes/"+imagen)
		imageOut=cv2.resize(image,(ancho,alto),interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(rutaTrain+"/"+imagen, imageOut)
		nombrexml=nombreXml(imagen)		
		shutil.move(rutaXml+"/"+nombrexml, rutaTrain+"/"+nombrexml)
		


for imagen in iVal:

	if imagen != "":
		image=cv2.imread("imagenes/"+imagen)
		imageOut=cv2.resize(image,(ancho,alto),interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(rutaVal+"/"+imagen, imageOut)
		nombrexml=nombreXml(imagen)		
		shutil.move(rutaXml+"/"+nombrexml, rutaVal+"/"+nombrexml)
