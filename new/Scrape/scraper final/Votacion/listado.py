# -*- coding: utf-8 -*-
from votacion import Votacion


class Listado(object):
    @classmethod
    def toObject(cls, Id, Id_Diputado, voto):
        v = Votacion(Id, Id_Diputado, voto)
        return v
