# -*- coding: utf-8 -*-
from proyecto import Proyecto


class Listado(object):
    @classmethod
    def toObject(cls, _id, nombre, id_votacion, materia):
        pro = Proyecto(_id, nombre, id_votacion, materia)
        return pro
