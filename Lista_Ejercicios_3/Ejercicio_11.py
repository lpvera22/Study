# *-* encoding:UTF-8 *-*
''''''
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

    def FBalanciamiento(self):
        if self.raiz.esHoja():
            return 0
        elif self.raiz.TieneHijoIzquierdo() and self.raiz.TieneHijoDerecho():
            return (1 + self.FBalanciamiento(self.raiz.izquierdo)-(1 + self.FBalanciamiento(self.raiz.derecho))

        elif self.raiz.TieneHijoIzquierdo():
            return (1 + self.FBalanciamiento(self.raiz.izquierdo))
        else:
            return 0 - self.FBalanciamiento(self.raiz.derecho)


'''def FBalanciamiento(arbol):
    if arbol.raiz.esHoja():
        return 0
    elif arbol.raiz.TieneHijoIzquierdo() and arbol.raiz.TieneHijoDerecho():
           return 1+FBalanciamiento(arbol.raiz.izquierdo)-(1+FBalanciamiento(arbol.raiz.derecho)
    elif  arbol.raiz.TieneHijoIzquierdo():
            return 1+FBalanciamiento(arbol.raiz.izquierdo)
    else:
           return 0-FBalanciamiento(arbol.raiz.derecho)'''
