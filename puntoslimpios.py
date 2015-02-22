#!/usr/bin/python
# -*- coding: utf-8 -*-
#Diego Martín Sánchez 1ºASIR, ejercicio_json

#Funciones
import json

#Variables
f=open("ecopuntos.json","r")
docu=json.load(f)
elemento=''
direccion=''

#Listar todas las direcciones de los puntos limpios de Málaga
print("\nDirecciones de puntos limpios:")
for punto in docu["features"]:
    elemento=punto["properties"]["elemento"]
    direccion=punto["properties"]["direccion"]
    print("\nElemento: %s\nDireccion: %s"%(elemento, direccion))

#Lista los puntos limpios y genera un enlace con su ubicacion en OpenStreetMap
for punto in docu["features"]:
    elemento=punto["properties"]["elemento"]
    latitud=punto["properties"]["latitud"]
    longitud=punto["properties"]["longitud"]
    print("\nElemento: %s\nUbicacion: http://www.openstreetmap.org/#map=15/%s/%s"%(elemento, latitud, longitud))

f.close
