import json
import os
import xml.etree.cElementTree as ET
import re
import cv2
import sys

def comprobarArgv(argumento):
	valor=640
	try:
		valor=sys.argv[argumento]
	except: 
		print("no hay argumento "+ str(argumento))		
	return valor
def comprobarDir():
	directorio="Json"
	try:
		directorio=sys.argv[3]
	except: 
		print("no especificado el direcotrio de los Json, argumento 3")		
	return directorio



anchoImagen=0

def pagina1(ancho,alto):
	try:	
		for i in data["pages"][0]["regions"]:
			objectAux=ET.SubElement(annonation,"object")
			ET.SubElement(objectAux,"name").text=i["type"]
			bbox=ET.SubElement(objectAux,"bndbox")

			fromX=int(i["bounding_box"]["fromX"])
			toX=int(i["bounding_box"]["toX"])
			fromY=int(i["bounding_box"]["fromY"])
			toY=int(i["bounding_box"]["toY"])
			#print(fromX)
			x1=int(fromX*anchoFinal/ancho)
			x2=int(toX*anchoFinal/ancho)
			y1=int(fromY*altoFinal/alto)
			y2=int(toY*altoFinal/alto)
			#print(x1)
			
			ET.SubElement(bbox,"xmin").text=str(x1)
			ET.SubElement(bbox,"ymin").text=str(y1)
			ET.SubElement(bbox,"xmax").text=str(x2)
			ET.SubElement(bbox,"ymax").text=str(y2)

			
			
	except:
  		print("no tiene pagina 1")
  		

def pagina2(ancho,alto):
	try:	
		for i in data["pages"][1]["regions"]:
			objectAux=ET.SubElement(annonation,"object")
			ET.SubElement(objectAux,"name").text=i["type"]
			bbox=ET.SubElement(objectAux,"bndbox")

			fromX=int(i["bounding_box"]["fromX"])
			toX=int(i["bounding_box"]["toX"])
			fromY=int(i["bounding_box"]["fromY"])
			toY=int(i["bounding_box"]["toY"])
			#print(fromX)
			x1=int(fromX*anchoFinal/ancho)
			x2=int(toX*anchoFinal/ancho)
			y1=int(fromY*altoFinal/alto)
			y2=int(toY*altoFinal/alto)
			#print(x1)
			
			ET.SubElement(bbox,"xmin").text=str(x1)
			ET.SubElement(bbox,"ymin").text=str(y1)
			ET.SubElement(bbox,"xmax").text=str(x2)
			ET.SubElement(bbox,"ymax").text=str(y2)
			
	except:
  		print("no tiene pagina 2")
  		
anchoFinal=int(comprobarArgv(1))
altoFinal=int(comprobarArgv(2))
directorio=comprobarDir()

for ficheros in os.listdir(directorio):

	with open("json/"+ficheros) as json_file:
		data=json.load(json_file)

		

	


	
	numpag=len(data["pages"])
	annonation = ET.Element("annonation")

	ET.SubElement(annonation, "filename").text=data["filename"]
	
	img = cv2.imread("imagenes/"+data["filename"])
	
	

	size=ET.SubElement(annonation, "size")
	alto=img.shape[0]
	ancho=img.shape[1]
	
	print(data["filename"])
	print( img.shape)
	
		
	

	
	ET.SubElement(size, "width").text=str(anchoFinal)
	ET.SubElement(size, "height").text=str(altoFinal)
	
	
	correcto1=pagina1(ancho,alto)
	correcto2=pagina2(ancho,alto)

	
	




  	
	tree=ET.ElementTree(annonation)
	nombre=data["filename"]	
	nombreAux=nombre[:-4]	
	tree.write("xml/"+nombreAux+".xml")



