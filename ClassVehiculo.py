
import abc
from abc import ABC
class vehiculo(ABC):
    __modelo=''
    __cantpuertas=0
    __color=''
    __precio=0.0
    
    def __init__(self,mod,cant,col,p):
        self.__modelo=mod
        self.__cantpuertas=cant
        self.__color=col
        self.__precio=p

    def __str__(self):
        cadena="marca: "+self.__marca
        return cadena
    def setprecio(self,precio):
        self.__precio=precio