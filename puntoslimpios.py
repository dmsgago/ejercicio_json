#!/usr/bin/python
# -*- coding: utf-8 -*-
#Diego Martín Sánchez 1ºASIR, ejercicio_json
import json
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

f.close
