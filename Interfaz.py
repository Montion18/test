from zope.interface import Interface
from zope.interface import implementer


class IUsado(Interface):
    def crearautousado(objeto,mod,cantp,color,prec,marca,patente,anio,km):
        pass
 

class INuevo(Interface):
    def crearautonuevo(objeto,mod,cantp,color,precio,marca,version):
        pass