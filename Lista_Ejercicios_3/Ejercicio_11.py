# *-* encoding:UTF-8 *-*
''''''
class Node:
    def __init__(self,data):
        self.data=data
        self.izquierdo=None
        self.derecho=None

    def esVacio(self):
        if self.raiz==None:
            return True
        else:
            return False
    def

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
        if not self.raiz.TieneHijoIzquierdo() and not self.raiz.TieneHijoDerecho():
            return True
        else:
            return False
    def altura(self):
        if self.esHoja():
            return 1
        elif self.TieneHijoIzquierdo() and not self.TieneHijoDerecho():
            return 1+self.izquierdo.raiz.altura()
        elif self.TieneHijoDerecho() and not self.TieneHijoIzquierdo():
            return 1+self.derecho.raiz.altura()
        else:
            return max(self.izquierdo.raiz.altura(),self.self.derecho.raiz.altura())





class ABB:
    def __init__(self):
        self.raiz=None


    def FBalanciamiento(self,lista):
        if self.raiz.esHoja():#Base: n=1 retorno o  unico elemento com su  factor de balanceamento que é 0 é altura 1
            lista.append((self.raiz.data,0))
            return lista, 1
        elif self.raiz.TieneHijoIzquierdo() and self.raiz.TieneHijoDerecho():
            aux1,aux2=self.FBalanciamiento(self.raiz.izquierdo,lista )
            aux3,aux4=self.FBalanciamiento(self.raiz.derecho,aux1)
            aux3.append(self.raiz.data,aux2-aux4)
            return aux3, max(aux2,aux4)
        elif self.raiz.TieneHijoIzquierdo():
            aux1, aux2 = self.FBalanciamiento(self.raiz.izquierdo, lista)
            aux1.append(self.raiz.data, aux2)
            return aux1, aux2

        else:
            aux3, aux4 = self.FBalanciamiento(self.raiz.derecho, lista)
            aux3.append(self.raiz.data,0-aux4)
            return aux3, aux4


