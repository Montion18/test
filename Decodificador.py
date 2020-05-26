import json
from pathlib import Path
from ClaseManejador import Manejador
from ClassVehiculo import vehiculo

class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                list=d['list']
                manejador=class_()
                for i in range(len(list)):
                    dlist=list[i]
                    class_name=dlist.pop('__class__')
                    class_=eval(class_name)
                    atributos=dlist['__atributos__']
                    unauto=class_(**atributos)
                    manejador.agregarauto(unauto)
            return manejador
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close() 

    def leerarchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario