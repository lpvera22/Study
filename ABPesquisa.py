class Node:
    def __init__(self,key):
        self.key=key
        self.derecho=None
        self.izquierdo=None

class ABPesquisa:
    def __init__(self):
        self.raiz=None

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
    def EsVacio(self):
        if self.raiz==None:
            return True
        else:
            return False

def EsHoja(node):
    if not node.TieneHijoIzquierdo() and not node.TieneHijoDerecho():
        return True
    else:
        return False



def Buscar(arbol, key):
    if not arbol.EsVacio():

        if arbol.raiz.key==key:
            return arbol.raiz
        else :
            if key < arbol.raiz.key:
                if arbol.raiz.TieneHijoIzquierdo() :

                    Buscar(arbol.raiz.izquierdo,key)
                else:
                    return None

            elif key > arbol.raiz.key:
                if arbol.raiz.TieneHijoDerecho():
                    Buscar(arbol.raiz.derecho, key)
                else:
                    return None
    else:
        return None

def BuscarNoRec(arbol,key):
    if not arbol.EsVacio():

        while (arbol.raiz!=None and arbol.raiz.key!=key):


            if key > arbol.raiz.key:
                arbol =arbol.raiz.derecho
            elif key < arbol.raiz.key:
                arbol = arbol.raiz.izquierdo

        return arbol
    else:
        print('Arbol Vacio')



def Inserir(arbol,key):
    new_node = Node(key)
    if arbol.EsVacio():
        arbol.raiz = new_node
    else:

        if key > arbol.raiz.key:

            Inserir(arbol.raiz.derecho,key)

        elif key < arbol.raiz.key:


            Inserir(arbol.raiz.izquierdo, key)

def InserirNoRec(arbol,key):

    new_node=Node(key)

    while ( not EsHoja(arbol.raiz)):
        if key > arbol.raiz.key:
            arbol=arbol.raiz.derecho
        elif key < arbol.raiz.key:
            arbol=arbol.raiz.izquierdo
        else:
            return None
    if key > arbol.raiz.key:
        arbol.raiz.derecho=new_node
    else:
        arbol.raiz.izquierdo=new_node







def Eliminar(arbol,node):
    pass





