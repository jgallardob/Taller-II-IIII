# -*- coding: utf-8 -*-
# Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB
import pymongo
import json
from pymongo import MongoClient
from Votacion.votaciones import Votaciones
from Proyecto.proyectos import Proyectos
from Boletin.boletines import Boletines
from sesiones.sesiones import Sesiones
from legislatura.legislaturas import Legislaturas


client = MongoClient('localhost', 27017)
db = client.integracion

legislaturasDict = {}
for l in Legislaturas.getLegislaturas():
    print l._id
    sesionesDict = {}
    for s in Sesiones.getSesiones(l._id):
        boletinesDict = {}
        for b in Boletines.getBoletines(s._id):
            proyectosDict = {}
            for p in Proyectos.getProyectos(b._id):
                votacionesDict = {}
                for v in Votaciones.getVotaciones(p.id_votacion):
                    votacionesDict[str(v.Id)] = {"Id_Diputado": str(v.Id_Diputado),
                                                 "voto": str(v.voto)}
                proyectosDict[str(p._id)] = {"nombre": str(p.nombre),
                                             "id_votacion": str(p.id_votacion),
                                             "materia": str(p.materia),
                                             "votaciones": votacionesDict}
            boletinesDict[str(b._id)] = {"proyectos": proyectosDict}
        sesionesDict[str(s._id)] = {"tipo": str(s.tipo),
                                    "Fecha": str(s.fecha),
                                    "estado": str(s.estado),
                                    "boletines": boletinesDict}
    legislaturasDict[str(l._id)] = {"numero": str(l.numero),
                                    "FechaInicio": str(l.fecha_inicio),
                                    "FechaTermino": str(l.fecha_termino),
                                    "sesiones": sesionesDict}

db.unica.insert(legislaturasDict)

# Solo para revision de datos se exporta a un json
# json = json.dumps(legislaturasDict)
# f = open("legislaturas.json", "w")
# f.write(json)
# f.close()

# client.close()
