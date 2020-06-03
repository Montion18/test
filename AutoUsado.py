from ClassVehiculo import vehiculo
import zope
from zope.interface import Interface
from zope.interface import implementer
from Interfaz import IUsado
@implementer(IUsado)
class autoUsado(vehiculo):
    __marca=''
    __patente=''
    __anio=0
    __km=0.0

    def __init__(self,mod,cantp,color,p,marca,pat,anio,km):
        self.__marca=marca
        super().__init__(mod,cantp,color,p)
        self.__patente=pat
        self.__anio=anio
        self.__km=km

    def usadotoJson(self):
        d=dict(
            __class__= self.__class__.__name__,
            __atributos__=dict(    mod=super()._vehiculo__modelo,                    
                               cantp=super()._vehiculo__cantpuertas,
                               color=super()._vehiculo__color,
                               precio=super()._vehiculo__precio,
                               marca=self.__marca,
                               patente=self.__patente,
                               anio=self.__anio,
                               km=self.__km
                               )
                           )
        return d