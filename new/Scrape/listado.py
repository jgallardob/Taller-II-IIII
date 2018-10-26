
from parlamentario import Parlamentario

class Listado():
    @classmethod
    def getParlamentarios(cls):
        """
        Retorna un arreglo que contiene todos los parlamentarios necesarios en
        forma de objetos
        """
        raise NotImplementedError('Se debe de implementar dentro de'
                                  'la subclase')

    @classmethod
    def toObject(cls, Id, nombre, AP, AM, sexo):
        """
        Metodo compartido(sirve para todo tipo de parlamentario) en el cual
        se convierte el metadata en un objeto
        """
        return Parlamentario(cls, Id, nombre, AP, AM, sexo)


