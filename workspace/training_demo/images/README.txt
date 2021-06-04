 _____           _                          _                         _                    _         _          _                 
 |  __ \         | |                        (_)                       | |                  | |       (_)        | |                
 | |  | |   ___  | |_    ___    ___    ___   _    ___    _ __       __| |   ___      ___   | |__      _    ___  | |_    ___    ___ 
 | |  | |  / _ \ | __|  / _ \  / __|  / __| | |  / _ \  | '_ \     / _` |  / _ \    / _ \  | '_ \    | |  / _ \ | __|  / _ \  / __|
 | |__| | |  __/ | |_  |  __/ | (__  | (__  | | | (_) | | | | |   | (_| | |  __/   | (_) | | |_) |   | | |  __/ | |_  | (_) | \__ \
 |_____/   \___|  \__|  \___|  \___|  \___| |_|  \___/  |_| |_|    \__,_|  \___|    \___/  |_.__/    | |  \___|  \__|  \___/  |___/
                                                                                                    _/ |                           
                                                                                                   |__/                            

Funcionamiento del setup para escalar y transormar json.

1- Es necesario tener una carpeta "imagenes" con todas las imagenes que vamos a utilizar para entrenar nuestro modelo
2- Es necesario tener una carpeta "Json" donde estarán todos los json con las bounding box de cada imagen
   Los nombres de los json tiene que ser igual al nombre de la imagen
3- Es necesario tener una carpeta "fold" con 3 txt:
	train.txt contiene las rutas de todos los json que se quieren utilizar para el entrenamiento (datasets/JSON/b-59-850/12613.JPG.json)
	test.txt contiene las rutas de todos los json que se quieren utilizar para el test (datasets/JSON/b-59-850/12613.JPG.json)
	val.txt contiene las rutas de todos los json que se quieren utilziar para la evaluacion (datasets/JSON/b-59-850/12613.JPG.json)

4 El setup recibe estos parametros
	1 ancho al que quieres transformar las imagenes para el entrenamiento (sin parametro = 640)
	2 alto al que quieres transformar las imagenes para el entrenamiento (sin parametro = 640)
	3 ruta de la carpeta json (sin parametro = "Json")
	4 nombre de la carpeta que hemos utilizado en la ruta de los fold (sin parametros = b-59-850)

