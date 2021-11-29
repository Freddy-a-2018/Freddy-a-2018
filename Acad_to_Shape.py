# creado por freddy Molina para pasar de CAD a SHAPE
#28 de Enero del 2018
print("Importar")
from Tkinter import *
print("!")
from tkinter import *
print("!!")
from tkinter import filedialog
print("!!!")
from tkinter import Listbox
print("!!!!")
from os import listdir
print("!!!!!")
from os import walk
print("!!!!!!")
import ttk as ttk
print("!!!!!!!")
import Tkinter, Tkconstants, tkFileDialog
print("!!!!!!!!")
from tkinter import messagebox
print("!!!!!!!!!")
import arcpy

print ("Done.....")

# Selecciona el directorio y graba el archivo en una variable
# llamada folder_path
def acad_button():
    global archivo
    global directorio
    global directorio2
    directorio1 = "\\" + "\\"+ "Cad_to_Shape" + "\\" + "\\" 
    nombre = tkFileDialog.askopenfilename(initialdir = "\\",
    title = "Seleccione Archivo de AutoCAD",
    filetypes = (("Archivos DWG","*.dwg"),("all files","*.*")))
    etiqueta3 = Label(ventana,text=nombre).place(x=10,y=50)
    disco = nombre [:2]
    directorio = disco + directorio1
    directorio2 = disco + directorio1 + "SHP" + "\\" + "\\"
    archivo = nombre [16:]
    print (directorio)
    print (archivo)
    print (directorio2)

def acad_indice():
    global archivo1
    global directorio7
    global directorio8
    global entrada1
    directorio6 = "\\" + "\\"+ "Cad_to_Shape" + "\\" + "\\" 
    nombre3 = tkFileDialog.askopenfilename(initialdir = "\\",
    title = "Seleccione Archivo de Curvas Indice - Intermedias",
    filetypes = (("Archivos SHP","*.shp"),("all files","*.*")))
    etiqueta11 = Label(ventana1,text=nombre3).place(x=20,y=70)
    disco1 = nombre3 [:2]
    directorio7 = disco1 + directorio6
    directorio8 = directorio7 + "SHP" + "\\" + "\\"
    archivo1 = nombre3 [20:]
    entrada1 = directorio8 + archivo1
    #print (entrada1)


def acad_interm():
    global entrada2
    global archivo2
    global directorio4
    global directorio5
    directorio3 = "\\" + "\\"+ "Cad_to_Shape" + "\\" + "\\" 
    nombre2 = tkFileDialog.askopenfilename(initialdir = "\\",
    title = "Seleccione Archivo de Curvas Indice - Intermedias",
    filetypes = (("Archivos SHP","*.shp"),("all files","*.*")))
    etiqueta11 = Label(ventana1,text=nombre2).place(x=20,y=100)
    disco1 = nombre2 [:2]
    directorio4 = disco1 + directorio3
    directorio5 = directorio4 + "SHP" + "\\" + "\\"
    archivo2 = nombre2 [20:]
    entrada2 = directorio5 + archivo2
    #print (entrada2)


def tin_sal():
    global entrada3
    global archivo20
    global directorio10
    global directorio11
    global directorio12
    directorio10 = "\\" + "\\"+ "Cad_to_Shape" + "\\" + "\\" + "DTM" "\\" + "\\"
    nombre10 = tkFileDialog.asksaveasfilename(initialdir = "\\",
    title = "Archivo Salida TIN",
    filetypes = (("Archivos ","*.*"),("all files","*.*")))
    etiqueta12 = Label(ventana1,text=nombre10).place(x=500,y=80)
    disco10 = nombre10 [:2]
    directorio11 = disco10 + directorio10
    directorio12 = directorio11
    archivo20 = nombre10 [20:]
    entrada3 = directorio12 + archivo20
    print (directorio12)
    print (archivo20)
    print (entrada3)


def ing_tin():
    global entrada5
    global archivo44
    global directorio40
    global directorio43
    global directorio44
    directorio40 = "\\" + "\\"+ "Cad_to_Shape" + "\\" + "\\" 
    nombre41 = tkFileDialog.askopenfilename(initialdir = "\\",
    title = "Seleccione Archivo de Curvas Indice - Intermedias",
    filetypes = (("Archivos TIF","*.tif"),("all files","*.*")))
    etiqueta11 = Label(ventana2,text=nombre41).place(x=150,y=30)
    disco42 = nombre41 [:2]
    directorio42 = disco42 + directorio40
    directorio43 = directorio42 + "DTM" + "\\" + "\\"
    archivo44 = nombre41 [20:]
    entrada5 = directorio43 + archivo44
    print (entrada5)
    
    



def sal_raster():
    global entrada4
    global archivo20
    global directorio10
    global directorio11
    global directorio12
    directorio10 = "\\" + "\\"+ "Cad_to_Shape" + "\\" + "\\" + "RASTER" "\\" + "\\"
    nombre10 = tkFileDialog.asksaveasfilename(initialdir = "\\",
    title = "Archivo Salida TIN",
    filetypes = (("Archivos ","*.*"),("all files","*.*")))
    etiqueta12 = Label(ventana2,text=nombre10).place(x=150,y=60)
    disco10 = nombre10 [:2]
    directorio11 = disco10 + directorio10
    directorio12 = directorio11
    archivo20 = nombre10 [23:]
    entrada4 = directorio12 + archivo20
    print (entrada4)



def puntos():
    global directorio
    # variables Locales:
    mensaje = "Proceso.....Finalizado"
    Point = directorio + archivo + "\\" + "\\" + "Point"
    POSTE_shp= directorio + "shp" + "\\" + "\\" + "POSTE.shp"
    ARBOL_AISLADO_shp= directorio + "shp" + "\\" + "\\" + "ARBOL_AISLADO.shp"
    ALCANTARILLADO_shp= directorio + "shp" + "\\" + "\\" + "ALCANTARILLADO.shp"
    # Sistema de coordenadas
    arcpy.env.scratchWorkspace = "C:\\Users\\Freddy Molina\\Documents\\ArcGIS\\Default.gdb"
    arcpy.env.outputCoordinateSystem = "PROJCS['WGS_1984_UTM_Zone_17S',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-81.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
    arcpy.env.workspace = "C:\\Users\\Freddy Molina\\Documents\\ArcGIS\\Default.gdb"
    #Proceso
    arcpy.Select_analysis(Point, POSTE_shp,"\"layer\" = 'POSTE'")
    arcpy.Select_analysis(Point, ARBOL_AISLADO_shp,"\"layer\" = 'ARBOL_AISLADO'")
    arcpy.Select_analysis(Point, ALCANTARILLADO_shp,"\"layer\" = 'ALCANTARILLADO'")
    #Mensaje
    #etiqueta4 = Label(ventana,text=mensaje).place(x=200,y=250)
    messagebox.showinfo("Finalizado...", mensaje)




def lineas ():
    global Polyline
    print("lineas")
    # Variable locales
    mensaje = "Proceso.....Finalizado"
    Polyline = directorio + archivo + "\\" + "\\" + "Polyline"
    ACEQUIA_shp =directorio + "shp" + "\\" + "\\" + "ACEQUIA.shp"
    ALAMBRADA_shp =directorio + "shp" + "\\" + "\\" + "ALAMBRADA.shp"
    ARBOLES_shp =directorio + "shp" + "\\" + "\\" + "ARBOLES.shp"
    AREA_EDUCATIVA_shp =directorio + "shp" + "\\" + "\\" + "AREA_EDUCATIVA.shp"
    AREA_RECREATIVA_shp =directorio + "shp" + "\\" + "\\" + "AREA_RECREATIVA.shp"
    Antena_Radio_shp =directorio + "shp" + "\\" + "\\" + "ANTENA_RADIO.shp"
    BASURERO_shp =directorio + "shp" + "\\" + "\\" + "BASURERO.shp"
    BEBEDERO_shp =directorio + "shp" + "\\" + "\\" + "BEBEDERO.shp"
    BORDILLO_shp =directorio + "shp" + "\\" + "\\" + "BORDILLO.shp"
    CALLE_shp =directorio + "shp" + "\\" + "\\" + "CALLE.shp"
    CAMINO_shp =directorio + "shp" + "\\" + "\\" + "CAMINO.shp"
    CANAL_shp =directorio + "shp" + "\\" + "\\" + "CANAL.shp"
    CANCHA_shp =directorio + "shp" + "\\" + "\\" + "CANCHA.shp"
    CARRETERA_shp =directorio + "shp" + "\\" + "\\" + "CARRETERA.shp"
    CERCA_VIVA_shp =directorio + "shp" + "\\" + "\\" + "CERCA_VIVA.shp"
    CUNETA_shp =directorio + "shp" + "\\" + "\\" + "CUNETA.shp"
    CAMINERA_shp =directorio + "shp" + "\\" + "\\" + "CAMINERA.shp"
    CEMENTERIO_shp =directorio + "shp" + "\\" + "\\" + "CEMENTERIO.shp"
    EMBALSE_shp =directorio + "shp" + "\\" + "\\" + "EMBALSE.shp"
    ESTACIONAMIENTO_shp =directorio + "shp" + "\\" + "\\" + "ESTACIONAMIENTO.shp"
    ESTERO_shp =directorio + "shp" + "\\" + "\\" + "ESTERO.shp"
    Eje_Cuneta_shp =directorio + "shp" + "\\" + "\\" + "EJE_CUNETA.shp"
    Eje_Vial_shp =directorio + "shp" + "\\" + "\\" + "EJE_VIAL.shp"
    GRADAS_shp =directorio + "shp" + "\\" + "\\" + "GRADAS.shp"
    INFRAESTRUCTURA_DEPORTIVA_shp =directorio + "shp" + "\\" + "\\" + "INFRAESTRUCTURA_DEPORTIVA.shp"
    ISLOTE_shp =directorio + "shp" + "\\" + "\\" + "ISLOTE.shp"
    JARDINERA_shp =directorio + "shp" + "\\" + "\\" + "JARDINERA.shp"
    Kiosko_Servicio_Publico_shp =directorio + "shp" + "\\" + "\\" + "KIOSKO_SERVICIO_PUBLICO.shp"
    LAGO_shp =directorio + "shp" + "\\" + "\\" + "LAGO.shp"
    Laguna_Oxidacion_shp =directorio + "shp" + "\\" + "\\" + "LAGUNA_OXIDACION.shp"
    Losa_shp =directorio + "shp" + "\\" + "\\" + "LOSA.shp"
    MONUMENTO_shp =directorio + "shp" + "\\" + "\\" + "MONUMENTO.shp"
    MURO_CERRAMIENTO_shp =directorio + "shp" + "\\" + "\\" + "MURO_CERRAMIENTO.shp"
    MURO_CONTENCION_shp =directorio + "shp" + "\\" + "\\" + "MURO_CONTENCION.shp"
    Muro_Tapial_shp =directorio + "shp" + "\\" + "\\" + "MURO_TAPIAL.shp"
    NAVE_INDUSTRIAL_shp =directorio + "shp" + "\\" + "\\" + "NAVE_INDUSTRIAL.shp"
    PARQUE_URBANO_shp =directorio + "shp" + "\\" + "\\" + "PARQUE_URBANO.shp"
    PASO_CEBRA_shp =directorio + "shp" + "\\" + "\\" + "PASO_CEBRA.shp"
    PILETA_shp =directorio + "shp" + "\\" + "\\" + "PILETA.shp"
    PISCINA_ALBERCA_shp =directorio + "shp" + "\\" + "\\" + "PISCINA_ALBERCA.shp"
    PUENTES_shp =directorio + "shp" + "\\" + "\\" + "PUENTES.shp"
    PUERTA_ENTRADA_shp =directorio + "shp" + "\\" + "\\" + "PUERTA_ENTRADA.shp"
    Palizada_shp =directorio + "shp" + "\\" + "\\" + "PALIZADA.shp"
    Parada_Buses_shp =directorio + "shp" + "\\" + "\\" + "PARADA_BUSES.shp"
    Parterre_shp =directorio + "shp" + "\\" + "\\" + "PARTERRE.shp"
    Paso_Peatonal_Elevado_shp =directorio + "shp" + "\\" + "\\" + "PASO_PEATONAL_ELEVADO.shp"
    Plaza_publica_shp =directorio + "shp" + "\\" + "\\" + "PLAZA_PUBLICA.shp"
    RIO_shp =directorio + "shp" + "\\" + "\\" + "RIO.shp"
    Rejilla_shp =directorio + "shp" + "\\" + "\\" + "REJILLA.shp"
    Sendero_shp =directorio + "shp" + "\\" + "\\" + "SENDERO.shp"
    TANQUE_ALMACENAMIENTO_shp =directorio + "shp" + "\\" + "\\" + "TANQUE_ALMACENAMIENTO.shp"
    TERRENO_CULTIVADO_shp =directorio + "shp" + "\\" + "\\" + "TERRENO_CULTIVADO.shp"
    TORRE_ELECTRICA_shp =directorio + "shp" + "\\" + "\\" + "TORRE_ELECTRICA.shp"
    Talud_shp =directorio + "shp" + "\\" + "\\" + "TALUD.shp"
    Techo_Cubierta_shp =directorio + "shp" + "\\" + "\\" + "TECHO_CUBIERTA.shp"
    Tribuna_shp =directorio + "shp" + "\\" + "\\" + "TRIBUNA.shp"
    ZANJA_shp =directorio + "shp" + "\\" + "\\" + "ZANJA.shp"
    ZONA_DE_OBRAS_shp =directorio + "shp" + "\\" + "\\" + "ZONA_DE_OBRAS.shp"
    ZONA_INUNDABLE_shp =directorio + "shp" + "\\" + "\\" + "ZONA_INUNDABLE.shp"
    Manzana_Catastral_shp =directorio + "shp" + "\\" + "\\" + "MANZANA_CATASTRAL.shp"
    Manzana_Cartografica_shp =directorio + "shp" + "\\" + "\\" + "MANZANA_CRTOGRAFICA.shp"
    PISCINA_shp =directorio + "shp" + "\\" + "\\" + "PISCINA.shp"
    # Sistema de coordenadas
    arcpy.env.scratchWorkspace = "C:\\Users\\Freddy Molina\\Documents\\ArcGIS\\Default.gdb"
    arcpy.env.outputCoordinateSystem = "PROJCS['WGS_1984_UTM_Zone_17S',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-81.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
    arcpy.env.workspace = "C:\\Users\\Freddy Molina\\Documents\\ArcGIS\\Default.gdb"
    # Proceso
    arcpy.Select_analysis(Polyline, ACEQUIA_shp,"\"layer\" = 'ACEQUIA'")
    arcpy.Select_analysis(Polyline, ALAMBRADA_shp,"\"layer\" = 'ALAMBRADA'")
    arcpy.Select_analysis(Polyline, ARBOLES_shp,"\"layer\" = 'ARBOLES'")
    arcpy.Select_analysis(Polyline, AREA_EDUCATIVA_shp,"\"layer\" = 'AREA_EDUCATIVA'")
    arcpy.Select_analysis(Polyline, AREA_RECREATIVA_shp,"\"layer\" = 'AREA_RECREATIVA'")
    arcpy.Select_analysis(Polyline, Antena_Radio_shp,"\"layer\" = 'ANTENA_RADIO'")
    arcpy.Select_analysis(Polyline, BASURERO_shp,"\"layer\" = 'BASURERO'")
    arcpy.Select_analysis(Polyline, BEBEDERO_shp,"\"layer\" = 'BEBEDERO'")
    arcpy.Select_analysis(Polyline, BORDILLO_shp,"\"layer\" = 'BORDILLO'")
    arcpy.Select_analysis(Polyline, CALLE_shp,"\"layer\" = 'CALLE'")
    arcpy.Select_analysis(Polyline, CAMINO_shp,"\"layer\" = 'CAMINO'")
    arcpy.Select_analysis(Polyline, CANAL_shp,"\"layer\" = 'CANAL'")
    arcpy.Select_analysis(Polyline, CANCHA_shp,"\"layer\" = 'CANCHA'")
    arcpy.Select_analysis(Polyline, CARRETERA_shp,"\"layer\" = 'CARRETERA'")
    arcpy.Select_analysis(Polyline, CERCA_VIVA_shp,"\"layer\" = 'CERCA_VIVA'")
    arcpy.Select_analysis(Polyline, CUNETA_shp,"\"layer\" = 'CUNETA'")
    arcpy.Select_analysis(Polyline, CAMINERA_shp,"\"layer\" = 'CAMINERA'")
    arcpy.Select_analysis(Polyline, CEMENTERIO_shp,"\"layer\" = 'CEMENTERIO'")
    arcpy.Select_analysis(Polyline, EMBALSE_shp,"\"layer\" = 'EMBALSE'")
    arcpy.Select_analysis(Polyline, ESTACIONAMIENTO_shp,"\"layer\" = 'ESTACIONAMIENTO'")
    arcpy.Select_analysis(Polyline, ESTERO_shp,"\"layer\" = 'ESTERO'")
    arcpy.Select_analysis(Polyline, Eje_Cuneta_shp,"\"layer\" = 'EJE_CUNETA'")
    arcpy.Select_analysis(Polyline, Eje_Vial_shp,"\"layer\" = 'EJE_VIAL'")
    arcpy.Select_analysis(Polyline, GRADAS_shp,"\"layer\" = 'GRADAS'")
    arcpy.Select_analysis(Polyline, INFRAESTRUCTURA_DEPORTIVA_shp,"\"layer\" = 'INFRAESTRUCTURA_DEPORTIVA'")
    arcpy.Select_analysis(Polyline, ISLOTE_shp,"\"layer\" = 'ISLOTE'")
    arcpy.Select_analysis(Polyline, JARDINERA_shp,"\"layer\" = 'JARDINERA'")
    arcpy.Select_analysis(Polyline, Kiosko_Servicio_Publico_shp,"\"layer\" = 'KIOSKO_SERVICIO_PUBLICO'")
    arcpy.Select_analysis(Polyline, LAGO_shp,"\"layer\" = 'LAGO'")
    arcpy.Select_analysis(Polyline, Laguna_Oxidacion_shp,"\"layer\" = 'LAGUNA_OXIDACION'")
    arcpy.Select_analysis(Polyline, Losa_shp,"\"layer\" = 'LOSA'")
    arcpy.Select_analysis(Polyline, MONUMENTO_shp,"\"layer\" = 'MONUMENTO'")
    arcpy.Select_analysis(Polyline, MURO_CERRAMIENTO_shp,"\"layer\" = 'MURO_CERRAMIENTO'")
    arcpy.Select_analysis(Polyline, MURO_CONTENCION_shp,"\"layer\" = 'MURO_CONTENCION'")
    arcpy.Select_analysis(Polyline, Muro_Tapial_shp,"\"layer\" = 'MURO_TAPIAL'")
    arcpy.Select_analysis(Polyline, NAVE_INDUSTRIAL_shp,"\"layer\" = 'NAVE_INDUSTRIAL'")
    arcpy.Select_analysis(Polyline, PARQUE_URBANO_shp,"\"layer\" = 'PARQUE_URBANO'")
    arcpy.Select_analysis(Polyline, PASO_CEBRA_shp,"\"layer\" = 'PASO_CEBRA'")
    arcpy.Select_analysis(Polyline, PILETA_shp,"\"layer\" = 'PILETA'")
    arcpy.Select_analysis(Polyline, PISCINA_ALBERCA_shp,"\"layer\" = 'PISCINA_ALBERCA'")
    arcpy.Select_analysis(Polyline, PUENTES_shp,"\"layer\" = 'PUENTES'")
    arcpy.Select_analysis(Polyline, PUERTA_ENTRADA_shp,"\"layer\" = 'PUERTA_ENTRADA'")
    arcpy.Select_analysis(Polyline, Palizada_shp,"\"layer\" = 'PALIZADA'")
    arcpy.Select_analysis(Polyline, Parada_Buses_shp,"\"layer\" = 'PARADA_BUSES'")
    arcpy.Select_analysis(Polyline, Parterre_shp,"\"layer\" = 'PARTERRE'")
    arcpy.Select_analysis(Polyline, Paso_Peatonal_Elevado_shp,"\"layer\" = 'PASO_PEATONAL_ELEVADO'")
    arcpy.Select_analysis(Polyline, Plaza_publica_shp,"\"layer\" = 'PLAZA_PUBLICA'")
    arcpy.Select_analysis(Polyline, RIO_shp,"\"layer\" = 'RIO'")
    arcpy.Select_analysis(Polyline, Rejilla_shp,"\"layer\" = 'REJILLA'")
    arcpy.Select_analysis(Polyline, Sendero_shp,"\"layer\" = 'SENDERO'")
    arcpy.Select_analysis(Polyline, TANQUE_ALMACENAMIENTO_shp,"\"layer\" = 'TANQUE_ALMACENAMIENTO'")
    arcpy.Select_analysis(Polyline, TERRENO_CULTIVADO_shp,"\"layer\" = 'TERRENO_CULTIVADO'")
    arcpy.Select_analysis(Polyline, TORRE_ELECTRICA_shp,"\"layer\" = 'TORRE_ELECTRICA'")
    arcpy.Select_analysis(Polyline, Talud_shp,"\"layer\" = 'TALUD'")
    arcpy.Select_analysis(Polyline, Techo_Cubierta_shp,"\"layer\" = 'TECHO_CUBIERTA'")
    arcpy.Select_analysis(Polyline, Tribuna_shp,"\"layer\" = 'TRIBUNA'")
    arcpy.Select_analysis(Polyline, ZANJA_shp,"\"layer\" = 'ZANJA'")
    arcpy.Select_analysis(Polyline, ZONA_DE_OBRAS_shp,"\"layer\" = 'ZONA_DE_OBRAS'")
    arcpy.Select_analysis(Polyline, ZONA_INUNDABLE_shp,"\"layer\" = 'ZONA_INUNDABLE'")
    arcpy.Select_analysis(Polyline, Manzana_Catastral_shp,"\"layer\" = 'MANZANA_CATASTRAL'")
    arcpy.Select_analysis(Polyline, Manzana_Cartografica_shp,"\"layer\" = 'MANZANA_CARTOGRAFICA'")
    arcpy.Select_analysis(Polyline, PISCINA_shp,"\"layer\" = 'PISCINA'")
    #Mensaje
    #etiqueta5 = Label(ventana,text=mensaje).place(x=200,y=250)
    messagebox.showinfo("Finalizado...", mensaje)


def poligono():
    global Polygon
    print ("poligonos")
    # Variable locales
    mensaje = "Proceso.....Finalizado"
    Polygon = directorio + archivo + "\\" + "\\" + "Polygon"
    CASA_TERRENO_ABANDONADO_shp = directorio + "shp" + "\\" + "\\" + "CASA_TERRENO_ABANDONADO.shp"
    CONSTRUCCION_shp = directorio + "shp" + "\\" + "\\" + "CONSTRUCCION.shp"
    CONSTRUCCION_PROVISIONAL_shp = directorio + "shp" + "\\" + "\\" + "CONSTRUCCION_PROVISIONAL.shp"
    CONST_PROVISIONAL_shp = directorio + "shp" + "\\" + "\\" + "CONST_PROVISIONAL.shp"
    CONST_AFECTADA_shp = directorio + "shp" + "\\" + "\\" + "CONST_AFECTADA.shp"
    # Sistema de coordenadas
    arcpy.env.scratchWorkspace = "C:\\Users\\Freddy Molina\\Documents\\ArcGIS\\Default.gdb"
    arcpy.env.outputCoordinateSystem = "PROJCS['WGS_1984_UTM_Zone_17S',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-81.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
    arcpy.env.workspace = "C:\\Users\\Freddy Molina\\Documents\\ArcGIS\\Default.gdb"
    # Proceso
    arcpy.Select_analysis(Polygon, CASA_TERRENO_ABANDONADO_shp,"\"layer\" = 'CASA_TERRENO_ABANDONADO'")
    arcpy.Select_analysis(Polygon, CONSTRUCCION_shp,"\"layer\" = 'CONSTRUCCION'")
    arcpy.Select_analysis(Polygon, CONSTRUCCION_PROVISIONAL_shp,"\"layer\" = 'CONSTRUCCION_PROVISIONAL'")
    arcpy.Select_analysis(Polygon, CONST_PROVISIONAL_shp,"\"layer\" = 'CONST_PROVISIONAL'")
    arcpy.Select_analysis(Polygon, CONST_AFECTADA_shp,"\"layer\" = 'CONST_AFECTADA'")
    #Mensaje
    #etiqueta6 = Label(ventana,text=mensaje).place(x=200,y=250)
    messagebox.showinfo("Finalizado...", mensaje)


def curvas():
    print ("Curvas de Nivel")
    # Variable locales
    mensaje = "Proceso.....Finalizado"
    Polyline = directorio + archivo + "\\" + "\\" + "Polyline"
    Curvas_Indices_shp = directorio + "shp" + "\\" + "\\" + "Curvas_Indices.shp"
    Curvas_Intermedias_shp = directorio + "shp" + "\\" + "\\" + "Curvas_intermedias.shp"
    # Sistema de coordenadas
    arcpy.env.scratchWorkspace = "C:\\Users\\Freddy Molina\\Documents\\ArcGIS\\Default.gdb"
    arcpy.env.outputCoordinateSystem = "PROJCS['WGS_1984_UTM_Zone_17S',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-81.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
    arcpy.env.workspace = "C:\\Users\\Freddy Molina\\Documents\\ArcGIS\\Default.gdb"
    # Proceso
    arcpy.Select_analysis(Polyline, Curvas_Indices_shp,"\"layer\" = 'Curvas_Indices'")
    arcpy.Select_analysis(Polyline, Curvas_Intermedias_shp,"\"layer\" = 'Curvas_Intermedias'")
    #Mensaje
    #etiqueta7 = Label(ventana,text=mensaje).place(x=200,y=250)
    messagebox.showinfo("Finalizado...", mensaje)



#Salir de la ventana
def Salir():
    global ventana
    ventana.destroy()


def Salir1():
    global ventana1
    ventana1.destroy()

def Salir2():
    global ventana2
    ventana2.destroy()



def seteo():
    #print ("Configuracion")
    mensaje1 = """ Crear una Carpeta en el disco llamada " "Cad_to_Shape"
    y dentro de esta una carpeta llamada SHP,
    copiar el Archivo .DWG a esta carpeta...../Cad_toShape/.
    para que el programa funcione de la mejor manera
    > NO SOBREESCRIBE LOS ARCHIVOS <
    > LOS NOMBRES DE LOS LAYER DEBEN ESTAR EN MAYUSCULAS <
    
    Creado por: Freddy Molina"""
    messagebox.showinfo("Configuracion", mensaje1)

def seteo1():
    #print ("Configuracion")
    mensaje2 = """ Crear una Carpeta en el disco llamada " "Cad_to_Shape"
    y dentro de esta una carpeta llamada SHP,
    en esta carpeta estaran los Archivos  de las Curvas de Nivel
    LOS NOMBRES DEBEN ESTAR EN Curvas_Indices.shp y Curvas_Intermedias.hp
    para que el programa funcione de la mejor manera
    > NO SOBREESCRIBE LOS ARCHIVOS <
    > LOS NOMBRES DE LOS LAYER DEBEN ESTAR EN MAYUSCULAS <
    
    Creado por: Freddy Molina"""
    messagebox.showinfo("Configuracion", mensaje2)


def Lista ():
    print ("LISTAR CAPAS")
    master = Tk()
    colorFondo= "#092"
    master.title("Lista de Feature Class")
    master.geometry("500x200")
    master.configure(background=colorFondo)
    arcpy.env.workspace="F:\\Cad_to_Shape\\shp\\"
    listadecapas=arcpy.ListFeatureClasses()
    listbox = Listbox(master,bg=colorFondo)
    listbox.pack(fill=BOTH, expand=2)
    listbox.insert(END, "L I S T A   D E    S H A P E S : ")
    for item in listadecapas:
        item = arcpy.Describe(item)
        listbox.insert(END, item.name + "               " + item.Shapetype)

    mainloop()


def Crear_TIN ():
    global entrada3
    global Curvas_Indices
    global Curvas_Intermedias
    global TIN
    mensaje = "....Finalizado.. TIN ha sido Creado"
    Coordinate_System = "PROJCS['WGS_1984_UTM_Zone_17S',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-81.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]" # provide a default value if unspecified
    TT7 = "C:\\Users\\Freddy Molina\\Documents\\ArcGIS\\T2"
    Curvas_Indices = directorio8 + archivo1
    Curvas_Intermedias = directorio5 + archivo2 
    print (Curvas_Indices)
    print (Curvas_Intermedias)
    print (entrada3)
    global TIN
    # Proceso: Create TIN
    TIN = entrada3
    arcpy.CreateTin_3d(TIN,Coordinate_System,"F:\\Cad_to_Shape\\SHP\\Curvas_Indices.shp Elevation Hard_Line Elevation;F:\\Cad_to_Shape\\SHP\\Curvas_intermedias.shp Elevation Hard_Line Elevation", "DELAUNAY")
    messagebox.showinfo("Proceso...", mensaje)

def convertir():
    global Sampling_Distance
    print ("To Raster")
    mensaje = "....Finalizado.. RASTER ha sido Creado"
    #Proceso: TIN a Raster
    arcpy.TinRaster_3d(TIN,entrada4, "FLOAT", "LINEAR", "CELLSIZE 0.5", "1")
    messagebox.showinfo("Proceso...", mensaje)


def raster():
    global ventana2
    ventana2 = Tk()
    ventana2.title("Creacion de Raster")
    ventana2.geometry("400x200")
    boton16 = Button(ventana2,text="Archivo de Entrada", command=ing_tin).place(x=20,y=30)
    boton17 = Button(ventana2,text="Archivo de Salida", command=sal_raster).place(x=20,y=60)
    boton18 = Button(ventana2,text="Salir",command=Salir2).place(x=200,y=160)
    boton19 = Button(ventana2,text="Convertir",command=convertir).place(x=200,y=120)
    
    mainloop()
    


def bitmap():
    global ventana1
    ventana1 = Tk()
    colorFondo= "#199"
    ventana1.title("Creacion de Archivo TIN")
    ventana1.geometry("700x200")
    ventana1.configure(background=colorFondo)
    etiqueta11 = Label(ventana1,text="Seleccionar Archivo de Curvas de Nivel    ").place(x=20,y=30)
    boton9 =  Button(ventana1,text="Indices",command=acad_indice).place(x=300,y=30)
    boton10 =  Button(ventana1,text="Intermedias",command=acad_interm).place(x=400,y=30)
    boton11 = Button(ventana1,text="Salir",command=Salir1).place(x=350,y=160)
    boton12 = Button(ventana1,text="Crear TIN..",command=Crear_TIN).place(x=400,y=120)
    boton13 = Button (ventana1,text="Setup", command=seteo1).place(x=650,y=30)
    boton14 = Button (ventana1,text="Archivo Salida",command = tin_sal).place(x=400,y=80)
    boton15 = Button (ventana1,text="A Raster---> ",command = raster).place(x=600,y=120)

    mainloop()
    


#creacion de la ventana

ventana = Tk()
folder_path = StringVar.get
colorFondo= "#004"
ventana.title("Proceso  De AutoCAD a Shapes")
ventana.geometry("600x300")
ventana.configure(background=colorFondo)
folder_path = StringVar()
etiqueta1 = Label(ventana,text="Buscar Archivo de AutoCAD").place(x=10,y=10)
etiqueta2 = Label(ventana,text="Procesar Archivo a ArcGIS_SHP").place(x=10,y=100)
etiqueta8= Label(ventana,text="f.m.",bg=colorFondo,fg="#FFF").place(x=555,y=280)
boton1 = Button(ventana,text="Browse",command=acad_button).place(x=200,y=10)
boton2 = Button(ventana,text="AutoCad a Puntos_SHP",command=puntos).place(x=200,y=100)
boton3 = Button(ventana,text="AutoCad a Lineas_SHP",command=lineas).place(x=400,y=100)
boton4 = Button(ventana,text="AutoCad a Polygonos_SHP",command=poligono).place(x=200,y=140)
boton4 = Button(ventana,text="AutoCad a Curvas de Nivel_SHP",command=curvas).place(x=400,y=140)
boton5 = Button(ventana,text="Salir",command=Salir).place(x=300,y=260)
boton6 = Button (ventana,text="Setup", command=seteo).place(x=550,y=10)
boton7 = Button (ventana,text="Listar Capas Procesadas_SHP",command=Lista).place(x=10,y=200)
boton8 = Button (ventana,text="De Curvas a Raster   ",bg="#090",command= bitmap).place(x=400,y=200)

mainloop()






