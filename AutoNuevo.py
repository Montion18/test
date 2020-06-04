from ClassVehiculo import vehiculo
from zope.interface import Interface
from zope.interface import implementer
from Interfaz import INuevo
@implementer(INuevo)
class AutoNuevo(vehiculo):
     marca="Fiat"
     __version=''

     def __init__(self,mod,cantp,color,precio,ver):
         super().__init__(mod,cantp,color,precio)
         self.__version=ver


     def toJson(self):
        d=dict(
            __class__= self.__class__.__name__,
            __atributos__=dict(

                            mod=super()._vehiculo__modelo,                    
                            cantp=super()._vehiculo__cantpuertas,
                            color=super()._vehiculo__color,
                            precio=super()._vehiculo__precio,
                            vers=self.__version
                               )
                           )
        return d
    

