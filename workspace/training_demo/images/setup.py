import os
import shutil
import sys
import errno
import msvcrt

anchoYAltoPorDefecto=640
carpetaJsonPorDefecto="Json"
nombreCarpetaFold="b-59-850"


def comprobarArgv(argumento):
	valor=anchoYAltoPorDefecto
	try:
		valor=sys.argv[argumento]
	except: 
		print("no hay argumento "+ str(argumento))		
	return valor

def comprobarDir():
	directorio=carpetaJsonPorDefecto
	try:
		directorio=sys.argv[3]
	except: 
		print("no especificado el direcotrio de los Json, argumento 3")		
	return directorio
def comprobarCarpetaFold():
	directorio=nombreCarpetaFold
	try:
		directorio=sys.argv[4]
	except: 
		print("no especificado el nombre de la carpeta fold")		
	return directorio


##Iniciamos el setup
##Creamos las carpetas
print("creamos las carpetas necesarias")
try:
    os.mkdir('imagenes')
    print("carpeta imagenes creada")
except: 
    print("ya existe la carpeta imagenes")
try:
    os.mkdir('train')
    print("carpeta train creada")
except: 
    print("ya existe la carpeta train")
try:
    os.mkdir('test')
    print("carpeta test creada")
except: 
    print("ya existe la carpeta test")
try:
    os.mkdir('val')
    print("carpeta val creada")
except: 
    print("ya existe la carpeta val")
try:
    os.mkdir('Json')
    print("carpeta Json creada")
except: 
    print("ya existe la carpeta Json")
try:
    os.mkdir('fold')
    print("carpeta fold creada")
except: 
    print("ya existe la carpeta fold")
try:
    os.mkdir('xml')
    print("carpeta xml creada")
except: 
    print("ya existe la carpeta xml")
###################################################################


##Comprobar los valores introduccidos o poner los valores por defecto
print("comprobamos valores introduccidos por linea de comando")
ancho=comprobarArgv(1)
if int(ancho) < 1 :
	ancho=anchoYAltoPorDefecto
	print("valor de ancho no valido")
print("ancho ="+ str(ancho))
alto=comprobarArgv(2)
if int(alto)<1:
	alto=anchoYAltoPorDefecto
	print("valor de ancho no valido")
print("alto ="+ str(alto))
directorioJson=comprobarDir()
print("directorio de los json="+directorioJson)

carpetaFold=comprobarCarpetaFold()
print("nombre de la carpeta fold="+carpetaFold)

print("Si los datos son correctos pulsa cualquier tecla para continuar")
msvcrt.getch()
################################################################################

##iniciamos el json to xml con los valores seleccionados 
print("iniciamos json to xml")
os.system("python json-to-xml.py "+str(ancho)+" "+str(alto)+" "+directorioJson)
#########################################################################

## hacemos el escalado de las imagenes con los valores seleccionados
print("iniciamos escalado de imagenes")
os.system("python escalado.py "+str(ancho)+" "+str(alto)+" "+ carpetaFold)
#########################################################



##Generamos los tfredord y los llevamos a la carpeta correspondiente
print("iniciamos TFrecord para train")
os.system("python generate_tfrecord.py -x train -l label_map.pbtxt -o train.record")
shutil.move("train.record", "../annotations/train.record")

print("iniciamos TFrecord para test")
os.system("python generate_tfrecord.py -x test -l label_map.pbtxt -o test.record")
shutil.move("test.record", "../annotations/test.record")
####################################################
