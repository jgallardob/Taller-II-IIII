
from objBoletin import Boletin


class Listado(object):
    @classmethod
    def getBoletines(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, _id):

        b = Boletin(_id)
        return b
