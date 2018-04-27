class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class ListaDoEnca:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def ListaVacia(self):

        if self.inicio == self.fin and self.inicio is None:  # O(1)
            return True
        else:
            return False

    def Inserir(self,x):#O(n)
        new_nodo=Node(x)

        if self.ListaVacia():
            self.inicio = new_nodo
            self.fin = new_nodo
        elif self.inicio==self.fin:
            self.inicio.next=new_nodo
            self.fin=new_nodo
            new_nodo.prev=self.inicio


        else:
            aux=self.inicio
            while(self.inicio.next.data<x):

                self.inicio = self.inicio.next

            desp=self.inicio.next
            new_nodo.next=desp
            desp.prev=new_nodo
            new_nodo.prev=self.inicio



            self.inicio=aux

def Procurar(lista,x): #O(n)
    if lista.ListaVacia():
        print('Lista Vacia')
    else:
        flag=False
        while(not flag and lista.next!=None):
            if lista.inicio.data==x:
                flag=True
                return lista.inicio
            else:
                lista.inicio = lista.inicio.next


def Eliminar(lista,x):#O(n)

    aux=Procurar(lista,x)
    if aux != None:
        aux.next=aux.prev
    else:
        print('El elemento no se encuentra')
        
def ListasIntercaladas(lista,lista2): #O(n)

    while(lista2.inicio.next!=None):

        lista.Inserir(lista2.inicio)
        lista2.inicio=lista2.inicio.next

    return lista

def ImprimirLista(lista):#O(n)
    while(lista.next!=None):
        print(lista.inicio.data)
        lista.inicio=lista.inicio.next
    print(lista.fin.data)

def DestruirLista(lista):#O(1)
    lista.inicio=lista.fin=None

#EJERCICIO 8
def BusquedaBinariaRec(lista,x):
    n=len(lista)
    if x==lista[n/2]:
        return True
    elif x>lista[n/2]:
        BusquedaBinariaRec(lista[n/2:],n)
    elif x<lista[n/2]:
        BusquedaBinariaRec(lista[: n / 2], n)

#EJERCICIO 9
class NodeABB:
    def __init__(self,data):
        self.data=data
        self.izquierdo=None
        self.derecho=None


class ABB:
    def __init__(self):
        self.raiz=None

    def EsVacio(self):
        if self.raiz==None:
            return True
        else:
            return False

    def TieneHijoIzquierdo(self):
        if self.raiz.izquierdo!=None:
            return True
        else:
            return False

    def TieneHijoDerecho(self):
        if self.raiz.derecho!=None:
            return True
        else:
            return False
    def TieneHijos(self):
        if self.TieneHijoIzquierdo() or self.TieneHijoDerecho():
            return True
        else:
            return False


    def EsHoja(self):
        if self.TieneHijoDerecho() or self.TieneHijoIzquierdo():
            return False
        else:
            return True


def Buscar(arbol,x):
    if arbol.EsVacio():
        print('Arbol Vacio')
    else:

        if arbol.raiz.data==x:
            return arbol.raiz

        elif x < arbol.raiz.data:

            if arbol.raiz.TieneHijoIzquierdo():
                Buscar(arbol.raiz.izquierdo, x)


            else:
                return None



        else:
            if arbol.raiz.TieneHijoDerecho():
               Buscar(arbol.raiz.derecho, x)
            else:
                return None


def BuscarMayor(arbol):

    if arbol.raiz.TieneHijoDerecho():
        BuscarMayor(arbol.raiz.derecho)
    else:
        return arbol.raiz.data

def BuscarMenor(arbol):
    if arbol.raiz.TieneHijoIzquierdo():
        BuscarMenor(arbol.raiz.izquierdo)
    else:
        return arbol.raiz.data





def Retira(arbol,x):
    if arbol.EsVacio():
        print('Arbol Vacio')
    else:
        if Buscar(arbol,x) != None:
            subarb=Buscar(arbol,x)
            if subarb.EsHoja():
                subarb.raiz=None
            else:
                if subarb.raiz.TieneHijoIzquierdo():
                    z=BuscarMayor(subarb.raiz.izquierdo)
                    subarb.raiz.data=z
                    Retira(subarb,z)
                elif subarb.raiz.TieneHijoDerecho():
                    z=BuscarMenor(subarb.raiz.derecho)
                    subarb.raiz.data=z
                    Retira(subarb,z)

def RetirarMayor(arbol):
    if arbol.EsVacio():
        print('Arbol Vacio')
    else:
        x=BuscarMayor(arbol)
        Retira(arbol,x)

def DestruirArbol(arbol):
    if arbol.raiz.TieneHijoDerecho():

        if not arbol.raiz.derecho.TieneHijos():
            arbol.raiz.derecho=None
        else:
            DestruirArbol(arbol.raiz.derecho)


    if arbol.raiz.TieneHijoIzquierdo():

        if not arbol.raiz.izquierdo.TieneHijos():
            arbol.raiz.izquierdo = None
        else:
            DestruirArbol(arbol.raiz.izquierdo)

    arbol.raiz=None




#EJERCICIO 10
#Altura
def Altura(arbol):
    if arbol.EsVacio():
        return 0
    elif arbol.raiz.EsHoja():
        return 1

    else:
       return max(Altura(arbol.raiz.izquierdo)+1,Altura(arbol.raiz.derecho)+1)
#Tamaño
def Tamaño(arbol):
    if arbol.EsVacio():
        return 0
    elif arbol.raiz.EsHoja():
        return 1

    else:








































