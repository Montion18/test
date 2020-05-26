from ClaseLista import Lista
from ClaseManejador import Manejador
from ClassVehiculo import vehiculo
from Decodificador import ObjectEncoder
class Menu:
    def mostrarmenu(self):
        print('Menú de Opciones: ')
        print("\n 1.")
        print("\n 2.")
        print("\n 3.")
        print("\n 0.Salir")
        opcionCorrecta = False
        while not opcionCorrecta:
            opcion=int(input('Seleccione una opcion: '))
            if opcion in [1,2,3,4,5,0]:
                opcionCorrecta=True
        return opcion


if __name__=='__main__':
    json=ObjectEncoder()
    m=Manejador()
    v=vehiculo()
    #d=m.toJSON()
    #json.decodificarDiccionario(d)
    #print(d)
    #json.guardarJSONArchivo(d,'vehiculos.json')
    #d=v.usadotoJson(2000,4,'azul',18000,'bmw','abc 123',2020,100000)
    #v.nuevotoJson(2020,5,'rojo',35000,'full')
    bandera=True
    while bandera:
        menu=Menu()
        op=menu.mostrarmenu()
        if op==1:
           # posicion=int(input('Ingrese la posicion donde desea insertar: '))
            md=input("Ingrese el modelo: ")
            cp=int(input('Ingrese la cantidad de puertas: '))
            cl=input("Ingrese el color: ")
            pr=int(input("Ingrese el precio:"))
            mar=input('Ingrese la marca: ')
            pt=input('Ingrese la patente: ')
            an=int(input('Ingrese el año:'))
            k=int(input('Ingrese la cantidad de Km: '))
            auto=v.crearautousado(md,cp,cl,pr,mar,pt,an,k)
            m.agregarauto(auto)
            #m.insertarauto(auto,posicion)
            m.mostrar()
        else:
            if op==2:
                print("op2")
            

            else:
                 bandera=False
                 print('Saliendo...')