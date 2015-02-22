#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Diego Martín Sánchez 1ºASIR, ejercicio_json

#Funciones
import json

#Variables
f=open("ecopuntos.json","r")
docu=json.load(f)
elemento=''
direccion=''
latitud=''
longitud=''
total=0
calle=''

#Listar todas las direcciones de los puntos limpios de Málaga
print("\nDirecciones de puntos limpios:")
for punto in docu["features"]:
    elemento=punto["properties"]["elemento"]
    direccion=punto["properties"]["direccion"]
    print("\nElemento: %s\nDireccion: %s"%(elemento, direccion))

#Lista los puntos limpios y genera un enlace con su ubicacion en OpenStreetMap
print("\nUbicaciones de los puntos limpios:")
for punto in docu["features"]:
    elemento=punto["properties"]["elemento"]
    latitud=punto["properties"]["latitud"]
    longitud=punto["properties"]["longitud"]
    print("\nElemento: %s\nUbicacion: http://www.openstreetmap.org/#map=15/%s/%s"%(elemento, latitud, longitud))

#Muestra el total de puntos limpios en Málaga
total=len(docu["features"])
print("\nTotal de puntos limpios: %d"%total)

#Pide el nombre de una calle y muestra los puntos limpios que hay en ella
calle=raw_input('\nBusqueda de puntos limpios por calle: ')
for punto in docu["features"]:
    if calle.lower() in punto["properties"]["direccion"].lower():
        print("Punto:%s (%s)"%(punto["properties"]["elemento"], punto["properties"]["direccion"]))

f.close
