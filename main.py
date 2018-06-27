import ListaSimple
LS = ListaSimple

import ArbolBinario
AB = ArbolBinario

import AVL
avl = AVL

import Arbol23
a23 = Arbol23

import Hash
hh = Hash

##########
## MAIN ##
##########

if __name__ == "__main__":
    
    ls = LS.lSimple()


    seguir = True
    while(seguir):
        print("====Eliga el tipo de lista a realizar====\n"+
              "1. Lista enlazada\n"+
              "2. Arbol Binario\n"+
              "3. Arbol AVL\n"+
              "4. Arbol 2-3\n"+
              "5. Hash")
        num = input("\nIngrese la opcion: ")
        

        if num == "1":
            seguir1 = True
            while(seguir1):
                print("\n\n=Lista de contactos: LISTA ENLAZADA=\n"+
                      "1. Agregar contacto\n"+
                      "2. Buscar por apellido\n"+
                      "3. Eliminar contacto\n"+
                      "4. Imprimir lista de contactos\n"+
                      "5. Volver al menu principal")
                num1 = input("\nIngrese la opcion: ")
                if num1 == "1":
                    print("\n== DATOS DEL NUEVO CONTACTO ==")
                    nombre = input("Ingrese el nombre: ")
                    apellido = input("Ingrese el apellido: ")
                    telefono = input("Ingrese telefono de contacto: ")
                    mail = input("Ingrese mail de contacto: ")
                    nod1 = LS.NodoLS(nombre, apellido, telefono, mail)
                    ls.AgregarLS(nod1)
                    print("== %s HA SIDO INGRESADO CORRECTAMENTE ==" %(nod1.nombre))

                if num1 == "2":
                    apellido=input("Ingrese apellido: ")
                    print("\nINFORMACION DEL CONTACTO:")
                    result = ls.buscarLS (apellido)
                    if result is not None:
                        print(result)
                    else:
                        print("Registro no encontrado")

                if num1 == "3":
                    apellido=input("Ingrese el apellido del contacto que desea eliminar: ")
                    if(ls.eliminarLS(apellido)):
                        print("== Contacto eliminado exitosamente==")
                        ls.contador = ls.contador - 1
                    else:
                        print("== No se encontro este contacto ==")
                    
                
                if num1 == "4":
                    ls.listarLS()

                if num1 == "5":
                    seguir1=False
                    

        if num == "2":
            seguir2 = True
            while(seguir2):
                print("\n\nARBOL BINARIO\n"+
                      "1. Agregar contacto\n"+
                      "2. Buscar por apellido\n"+
                      "3. Eliminar contacto\n"+
                      "4. Imprimir lista de contactos\n")
                num2 = input("\nIngrese la opcion: ")
                if num2 == "1":
                    print("\n== DATOS DEL NUEVO CONTACTO ==")
                    nombre = input("Ingrese el nombre: ")
                    apellido = input("Ingrese el apellido: ")
                    telefono = input("Ingrese telefono de contacto: ")
                    mail = input("Ingrese mail de contacto: ")
                    nod2 = NodoAB(nombre, apellido, telefono, mail)
                    ab.AgregarAB(nod2)
                    print("== %s HA SIDO INGRESADO CORRECTAMENTE ==" %(nod2.nombre))

                if num2 == "2":
                    apellido=input("Ingrese apellido: ")
                    print("\nINFORMACION DEL CONTACTO:")
                    result = ls.buscarLS (apellido)
                    if result is not None:
                        print(result)
                    else:
                        print("Registro no encontrado")

                if num1 == "3":
                    apellido=input("Ingrese el apellido del contacto que desea eliminar: ")
                    if(ab.eliminarAB(apellido)):
                        print("== Contacto eliminado exitosamente==")
                    else:
                        print("== No se encontro este contacto ==")

                if num2 == "4":                    
                    ab.listarAB(ab.getRaiz())

                if num2 == "5":
                    seguir2=False

                

        if num == "3":
            seguir3 = True
            while(seguir3):
                print("\n\nARBOL AVL\n"+
                      "1. Agregar contacto\n"+
                      "2. Buscar por apellido\n"+
                      "3. Eliminar contacto\n"+
                      "4. Imprimir lista de contactos\n")

                if num3 == "5":
                    seguir3=False

        if num == "4":
            seguir4 = True
            while(seguir4):
                print("\n\nARBOL 2-3\n"+
                      "1. Agregar contacto\n"+
                      "2. Buscar por apellido\n"+
                      "3. Eliminar contacto\n"+
                      "4. Imprimir lista de contactos\n")

                if num4 == "5":
                    seguir4=False
                    
        if num == "5":
            seguir5 = True
            while(seguir5):
                print("\n\nHASH\n"+
                      "1. Agregar contacto\n"+
                      "2. Buscar por apellido\n"+
                      "3. Eliminar contactp\n"+
                      "4. Imprimir lista de contactos\n")

                if num5 == "5":
                    seguir5=False





