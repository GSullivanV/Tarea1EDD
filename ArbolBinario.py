######
#### Arbol Binario
#####

class NodoAB:
    def __init__(self, nombre=None, apellido=None, telefono=None, mail=None, izq=None, der=None):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.mail=mail
        self.izq=izq
        self.der=der

    def __str__(self):
        return "%s %s %s %s" %(self.nombre, self.apellido, self.telefono, self.mail)



class ArbolB:
    def __init__(self):
        self.raiz=None

    def AgregarAB(self, contacto):
        if self.raiz == None:
            self.raiz = contacto
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if str(contacto.apellido)>=str(aux.apellido):
                    aux = aux.der
                else:
                    aux = aux.izq
            if str(contacto.apellido)>=str(padre.apellido):
                padre.der = contacto
            else:
                padre.izq = contacto

    def buscarAB(self, data):
	    if self.raiz:
		    return self.raiz.buscarAB(data)
	    else:
		    return False




    def listarAB(self, contacto):
        if contacto != None:
            self.listarAB(contacto.izq)
            print(contacto)
            self.listarAB(contacto.der)

    def getRaiz(self):
        return self.raiz







