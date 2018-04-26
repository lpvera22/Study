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






















