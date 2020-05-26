from ClaseLista import Lista
from ClassVehiculo import vehiculo
class Manejador:
    __list=Lista()
    def __init__(self):
        self.__list=Lista()
    def agregarauto(self,auto):
        self.__list.Agregarauto(auto)
    def toJSON(self):
        v=vehiculo()
        d=dict(
            __class__=self.__class__.__name__,
            autos=[v.usadotoJson() for vehiculo in self.__list]
            )
        return d

    def insertarauto(self,auto,posicion):
        self.__list.insertar(auto,posicion)
    def mostrar(self):
        for i in self.__list:
            print("datos ",i)