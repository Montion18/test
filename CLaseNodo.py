class Nodo:
    __vehiculo=None
    __sig=None
    def __init__(self,auto):
        self.__vehiculo=auto
        self.__sig=None
    def setsig(self,sig):
        self.__sig=sig
    def getauto(self):
        try:
            return self.__vehiculo
        except IndexError:
            print("\nError no existe un elemento en dicha posicion")
    def getSiguiente(self):  
        return self.__sig 



