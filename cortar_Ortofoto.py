# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# cortar.py
# Created on: 2020-11-11 18:15:12.0
# Freddy Molina
# Para que funcione hay que tener los archivos de corte
# Hay q tener muy en cuenta las rutas de los archivos (path)
# el archivo de entrada(RASTER), la carpeta con el limite (Shape)y la carpeta
# de salida (Raster)
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

print (".......ORTOFOTO..............")
# Variables:
print (".......LEYENDO DATOS..............")
# archivo original de donde vamos a cortar (RASTER)
Archivo_Raster = "Y:\\04_LAS_PEÑAS\\12_Orthomaster_1\\mosaic\\Penias\\Penias.tif"
# archivo para cortar es el limite para el corte 
Limite = "Y:\\04_LAS_PEÑAS\\21_Limite_final_partes\\5_km.shp"
# archivo de Salida donde se va ha guardar (RASTER)
Archivo_Salida = "Y:\\04_LAS_PEÑAS\\22_Cortado_kilometros\\Km5.tif"
print (".......Procesando Ortofoto.......")
# Process: Extract by Mask
arcpy.gp.ExtractByMask_sa(Archivo_Raster, Limite, Archivo_Salida)

print (".......Proceso Corte_Ortofoto..Terminado...")
print (Archivo_Salida)
