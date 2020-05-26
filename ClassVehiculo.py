from zope.interface import Interface
import json
from pathlib import Path 
from zope.interface import implementer
from Interfaz import INuevo
from Interfaz import IUsado
@implementer(IUsado)
@implementer(INuevo)
class vehiculo:
    __modelo=''
    __cantpuertas=0
    __color=''
    __precio=0.0
    __marca=''
    __patente=''
    __anio=''
    __km=0
    __version=''
    marca='Fiat'
    
    def __str__(self):
        cadena="marca: "+self.__marca
        return cadena
    def crearautousado(self,mod,cantp,color,prec,marca,patente,anio,km):
        self.__modelo=mod
        self.__cantpuertas=cantp
        self.__color=color
        self.__precio=prec
        self.__marca=marca
        self.__patente=patente
        self.__anio=anio
        self.__km=km
        return self

    def crearautonuevo(self,mod,cantp,color,precio,version):
        self.__modelo=mod
        self.__cantpuertas=cantp
        self.__color=color
        self.__precio=precio
        self.__version=version

    def usadotoJson(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(mod=self.__modelo,
                               cantp=self.__cantpuertas,
                               color=self.__color,
                               precio=self.__precio,
                               marca=self.__marca,
                               patente=self.__patente,
                               anio=self.__anio,
                               km=self.__km
                               )
                           )
        return d

    def nuevotoJson(self,mod,cantp,color,precio,version):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(mod=mod,
                               cantp=cantp,
                               color=color,
                               precio=precio,
                               vers=version
                               )
                           )
        return d
