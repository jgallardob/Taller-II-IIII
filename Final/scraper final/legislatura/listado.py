from objLegislatura import Legislatura


class Listado(object):
    @classmethod
    def getLegislaturas(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, _id, numero, fecha_inicio, fecha_termino):

        l = Legislatura(_id, numero, fecha_inicio, fecha_termino)
        return l
