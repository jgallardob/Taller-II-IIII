# coding=utf-8
from votacion import Votacion


class Listado(object):
    @classmethod
    def get_Votaciones(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, _id, Id_Diputado, voto):

        v = Votacion(_id, Id_Diputado, voto)
        return v
