class NodoLS(object):
    def __init__(self, nombre=None, apellido=None, telefono=None, mail=None, sig=None):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail
        self.sig = sig

    def __str__(self):
        return "%s %s %s %s" %(self.nombre, self.apellido, self.telefono, self.mail)

class lSimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.contador = 0

    def getVacio(self):
        if (self.primero == None):
            return True

    def AgregarLS(self, contacto):
        if self.primero == None:
            self.primero = contacto
        if self.ultimo != None:
            self.ultimo.sig = contacto
        self.ultimo = contacto
        self.contador = self.contador + 1



    def listarLS(self):
        print("\n=Lista de contactos=")
        aux = self.primero
        while aux != None:
            print(aux)
            aux = aux.sig

    def buscarLS(self, apellido):
        aux = self.primero
        while aux != None:
            if str(aux.apellido) == str(apellido):
                return aux
            aux = aux.sig
        return None

    def eliminarLS (self, apellido):
            
        if str(self.primero.apellido) == str(apellido):
            self.primero = self.primero.sig
            return True
        else:
            aux = self.primero
            anterior =aux
            while aux != None:
                if str(aux.apellido) == str(apellido):
                    anterior.sig = Nodo.
                    return True
                anterior = aux
                aux = aux.sig
            return False







                





