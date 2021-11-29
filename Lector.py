# creado por freddy Molina para extraer los datos de las fotos
# se necesita poner la carpeta donde estan las fotos
# la sesion entre comillas y
# la carpeta entre comillas
# 13/Noviembre/2021
#====================================================
import os

#poner la carpeta
#carpeta_dir = "M:/02_Procesos/01_Campo/02_Datos_Campo/05_FOTOS/CAM1/20211022/S09/c2_01"
archivo = "M:/02_Procesos/01_Campo/02_Datos_Campo/05_FOTOS/CAM1/20211022/"
sesion = "S09"
carpeta = "C1"
carpeta_dir = archivo+"/"+sesion+"/"+carpeta
#print (carpeta_dir)
contenido = os.listdir(carpeta_dir)
n = 0
imagenes = []
fotos = []
for fichero in contenido:
    if os.path.isfile(os.path.join(carpeta_dir, fichero)) and fichero.endswith('.IIQ'):
        imagenes.append(fichero)
        n = n + 1
    #print(fichero)

#print (imagenes)
inicio = imagenes [0]
final  = imagenes.pop()
#print (n)
#print(inicio)
#print (final)

union = (sesion,carpeta,inicio,final,n)

print (union)


