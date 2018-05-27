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

    def FBalanciamiento(self,lista):
        if self.raiz.esHoja():
            lista.append((self.raiz.data,0))
            return lista, 1
        elif self.raiz.TieneHijoIzquierdo() and self.raiz.TieneHijoDerecho():
            aux1,aux2=self.FBalanciamiento(self.raiz.izquierdo,lista )
            aux3,aux4=self.FBalanciamiento(self.raiz.derecho,aux1)
            aux1.append(self.raiz,aux2-aux4)
            return aux1, max(aux2,aux4)
        elif self.raiz.TieneHijoIzquierdo():
            aux1, aux2 = self.FBalanciamiento(self.raiz.izquierdo, lista)
            aux1.append(self.raiz, aux2)
            return aux1, aux2

        else:
            aux3, aux4 = self.FBalanciamiento(self.raiz.derecho, lista)
            aux3.append(self.raiz,0-aux4)
            return aux3, aux4


