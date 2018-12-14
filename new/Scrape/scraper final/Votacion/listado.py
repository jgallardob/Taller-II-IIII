# -*- coding: utf-8 -*-
from objVotacion import Votacion


class Listado(object):
    @classmethod
    def getVotaciones(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, Id, Id_Diputado, voto):
        v = Votacion(Id, Id_Diputado, voto)
        return v
