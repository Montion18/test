from CLaseNodo import Nodo

class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            auto=self.__actual.getauto()
            self.__actual=self.__actual.getSiguiente()
            return auto
    def Agregarauto(self,auto):
        nodo=Nodo(auto)
        nodo.setsig(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def insertar(self,auto,pos):
        nodo=Nodo(auto)

