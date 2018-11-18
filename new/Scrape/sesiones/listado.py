from sesion import Sesion


class Listado(object):
    @classmethod
    def getParlamentarios(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, Id, numero, fecha_inicio, fecha_termino):

        s = Sesion(Id, numero, fecha_inicio, fecha_termino)
        return s
