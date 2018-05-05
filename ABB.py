class Node:
    def __init__(self,data):
        self.data=data
        self.izquierdo=None
        self.derecho=None

class ABB:
    def __init__(self):
        self.raiz=None
    def esVacio(self):
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
        if self.raiz.derecho != None:
            return True
        else:
            return False

    def esHoja(self):
        if not self.TieneHijoIzquierdo() and not self.TieneHijoDerecho():
            return True
        else:
            return False



    def inserir(self,data):

        new_node=Node(data)
        if self.esVacio():
            self.raiz = new_node
        else:
            if new_node.data < self.raiz.data:

                if self.TieneHijoIzquierdo():
                    return self.raiz.izquierdo.inserir(data)
                else:
                    self.raiz.izquierdo=new_node
            elif new_node.data > self.raiz.data:
                if self.TieneHijoDerecho():
                    return self.raiz.derecho.inserir(data)
                else:
                    self.raiz.derecho = new_node

def BuscarNodo(arbol,nodo):
    if arbol.esVacio():
        print('Arbol vacio')
    else:
        if arbol.raiz.data==nodo.data:
            return True
        elif nodo.data>arbol.raiz.data:
            if arbol.Tiene
            return BuscarNodo(arbol.raiz.derecho, nodo)
        elif



