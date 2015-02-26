#!/usr/bin/python
# -*- coding: utf-8 -*-
#Diego Martín Sánchez 1ºASIR, ejercicio_json

#Funciones
import json
from math import sin,cos,sqrt,asin,pi

#Variables
f=open("ecopuntos.json","r")
docu=json.load(f)
elemento=''
direccion=''
latitud=''
longitud=''
total=0
calle=''
ident=''
radiotierra=6371000
gtor=pi/180
encontrado=False

#Listar todas las direcciones de los puntos limpios de Málaga
print("\nDirecciones de puntos limpios:")
for punto in docu["features"]:
    elemento=punto["properties"]["elemento"]
    direccion=punto["properties"]["direccion"]
    print("\nElemento: %s\nDireccion: %s"%(elemento, direccion))

raw_input('Haga clic para continuar...')

#Lista los puntos limpios y genera un enlace con su ubicacion en OpenStreetMap
print("\nUbicaciones de los puntos limpios:")
for punto in docu["features"]:
    elemento=punto["properties"]["elemento"]
    latitud=punto["properties"]["latitud"]
    longitud=punto["properties"]["longitud"]
    print("\nElemento: %s\nUbicacion: http://www.openstreetmap.org/#map=15/%s/%s"%(elemento, latitud, longitud))

raw_input('(\nHaga clic para continuar...)')
    
#Muestra el total de puntos limpios en Málaga
total=len(docu["features"])
print("\nTotal de puntos limpios: %d"%total)

raw_input('(\nHaga clic para continuar...)')

#Pide el nombre de una calle y muestra los puntos limpios que hay en ella
calle=raw_input('\nBusqueda de puntos limpios por calle: ')
for punto in docu["features"]:
    if calle.lower() in punto["properties"]["direccion"].lower():
        print("Punto:%s (%s)"%(punto["properties"]["elemento"], punto["properties"]["direccion"]))

raw_input('(\nHaga clic para continuar...)')
        
#Muestra todos los puntos limpios y pide al usuario que elija uno, posteriormente mostrará todos los puntos limpios a 100m.
print("\nPuntos limpios:")
for punto in docu["features"]:
    ident=punto["id"]
    elemento=punto["properties"]["elemento"]
    print("%s. %s"%(ident, elemento))
seleccion=raw_input('\nIntroduce el identificdor del punto limpio ["ecoPuntos.X"]: ')
for punto in docu["features"]:
    ident=punto["id"]
    if seleccion.lower() == ident.lower():
        lat1=punto["geometry"]["coordinates"][1]
        long1=punto["geometry"]["coordinates"][0]
        encontrado=True
if not encontrado:
    print('Punto limpio no encontrado')
    exit()

print("\nPuntos limpios cercanos: ")
for punto in docu["features"]:
    elemento=elemento=punto["properties"]["elemento"]
    lat2=punto["geometry"]["coordinates"][1]
    long2=punto["geometry"]["coordinates"][0]
    #Fórmula de haversine, para calcular distantia entre dos puntos
    diferencia=2*radiotierra*asin(sqrt(sin(gtor*(lat2-lat1)/2)**2+cos(gtor*lat1)*cos(gtor*lat2)*sin(gtor*(long2-long1)/2)**2))
    if diferencia < 100 and diferencia != 0:
        print("%s, a %0.2f metros"%(elemento, diferencia))
    
f.close
