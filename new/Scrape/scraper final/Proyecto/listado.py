# -*- coding: utf-8 -*-
from objProyecto import Proyecto


class Listado(object):
    @classmethod
    def getProyectos(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, _id, nombre, id_votacion, materia):
        pro = Proyecto(_id, nombre, id_votacion, materia)
        return pro
