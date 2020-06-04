from ClaseLista import Lista
from Decodificador import ObjectEncoder
from AutoNuevo import AutoNuevo
from ClassVehiculo import vehiculo
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
    dic=json.leerarchivo('vehiculos.json')
    print(dic)
    print(type(dic))
    lista=json.decodificarDiccionario(dic)
    print(lista)
    print(type(lista))
    bandera=True
    while bandera:
        menu=Menu()
        op=menu.mostrarmenu()
        if op==1:
            tipo=input('Ingrese N si el auto es nuevo o V si es viejo: ').upper()
            if tipo =='V':
                posicion=int(input('Ingrese la posicion donde desea insertar: '))
                md=input("Ingrese el modelo: ")
                cp=int(input('Ingrese la cantidad de puertas: '))
                cl=input("Ingrese el color: ")
                pr=int(input("Ingrese el precio:"))
                mar=input('Ingrese la marca: ')
                pt=input('Ingrese la patente: ')
                an=int(input('Ingrese el año:'))
                k=int(input('Ingrese la cantidad de Km: '))
                auto=v.crearautousado(md,cp,cl,pr,mar,pt,an,k)
                m.insertarauto(auto,posicion)
                m.mostrar()
            elif tipo =='N':
                print("Auto nuevo")
        else:
            if op==2:
                print("op2")
                md=input("Ingrese el modelo: ")
                cp=int(input('Ingrese la cantidad de puertas: '))
                cl=input("Ingrese el color: ")
                pr=int(input("Ingrese el precio:"))
                mar=input('Ingrese la marca: ')
                pt=input('Ingrese la patente: ')
                an=int(input('Ingrese el año:'))
                k=int(input('Ingrese la cantidad de Km: '))
                auto=v.crearautousado(md,cp,cl,pr,mar,pt,an,k)
                auto2=v2.crearautousado(200,4,'rojo',2555,'ford','ab123',2020,30000)
                m.agregarauto(auto)
                m.agregarauto(auto2)
                m.mostrar()
            

            else:
                 bandera=False
                 print('Saliendo...')