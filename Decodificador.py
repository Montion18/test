import json
from pathlib import Path
from ClaseLista import Lista
from AutoUsado import autoUsado
from AutoNuevo import AutoNuevo

class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if "__class__" not in d:
            
            return d
        else:
            class_name=d["__class__"]
            class_= eval(class_name)
            if class_name == 'Lista':
                elementos=d['__atributos__']
                la_lista=class_()
                for i in range(len(elementos)):
                    print(elementos["mod"])

                    delemento=elementos[i]
                    class_name = delemento.pop('__class__')
                    class_= eval(class_name)
                    atributos=delemento["__atributos__"]
                    unauto=class_(**atributos)
                    la_lista.agregarauto(unauto)
                return la_lista
    def guardarJSONArchivo(self, diccionario, archivo):
        with open(archivo,"w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close() 

    def leerarchivo(self,archivo):
        with open(archivo,encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario