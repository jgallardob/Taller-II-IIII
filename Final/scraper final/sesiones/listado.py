from objSesion import Sesion


class Listado(object):
    @classmethod
    def getSesiones(cls):
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, _id, fecha, tipo, estado):

        s = Sesion(_id, fecha, tipo, estado)
        return s
