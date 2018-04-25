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

    def Inserir(x):#O(n)
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
        
def ListasIntercaladas(lista,lista2):

    while(lista2.inicio.next!=None):

        lista.Inserir(lista.inicio)
        lista.inicio=lista.inicio.next

    return lista2



def ImprimirLista(lista):#O(n)

    while(lista.inicio.next!=None):
        print(lista.inicio.data)
        lista.inicio =lista.inicio.next

def DestruirLista(lista):#O(1)

    lista.inicio=lista.fin=None

#EJERCICIO 2


def InsertarListaOrd(lista,x):#O(n)
    if len(lista)>=0:
        lista.append(x)
        i=len(lista)
        while(i<=0):
            if lista[i]<lista[i-1]:
                aux=lista[i]
                lista[i]=lista[i-1]
                lista[i-1]=aux
                i=i-1
            else: i=i-1


    else:
        lista.append(x)
def UnionConjuntos(conjunto1,conjunto2):#O(n^2)


    for i in conjunto1:
        if i not in conjunto2:
            conjunto2.append(i)

    return conjunto2

def Interseccion(conjunto1, conjunto2):#O(n^2)
    conjuntoInterseccion=[]
    for i in conjunto1:
        for j in conjunto2:
            if i==j:
                conjuntoInterseccion.append(i)
    return conjuntoInterseccion

def ConjuntosIguales(conjunto1, conjunto2):
    flag=True
    for i in conjunto1:
        for j in conjunto2:
            if i!=j:
                flag=False
    if not flag:
        return False
    else:
        return True

#EJERCICIO  4
class Fila:
    def __init__(self):
        self.fila=[]
        self.fin = len(self.lista)

    def EsVacia(self):
        if self.fin < 0:
            return True
        else:
            return False
class Pila:
    def __init__(self):
        self.pila=[]
        self.tope=len(self.pila)

    def EsVacia(self):
        if self.tope < 0:
            return True
        else:
            return False

def Empilar(P,x):
    P.pila.append(x)

def Desempilar(P):
    return P.pila.pop()

def Enfilar(F,x):
    F.fila.append(x)

def Desenfilar(F):
    aux=F.fila[F.fin]
    return F.fila[aux]

def Invertir(F):
    pila=Pila()
    while(F.fin>=0):
        i=Desenfilar(F.fila)
        Empilar(pila,i)
    while(pila.tope>=0)
        i=Desempilar(pila)
































