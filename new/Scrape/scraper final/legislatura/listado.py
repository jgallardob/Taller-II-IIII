from legislatura import Legislatura


class Listado(object):
    @classmethod
    def getLegislatura(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, _id, numero, fecha_inicio, fecha_termino):

        l = Legislatura(_id, numero, fecha_inicio, fecha_termino)
        return l
