import random
#EJERCICIO 1

'''Supongamos que tenemos una función valor tal que dado un valor de tipo char (una   letra   del   alfabeto)   devuelve
   un   valor   entero   asociado   a   dicho identificador.
Supongamos también   la  existencia  de  un  árbol  de  expresión  T  cuyos nodos  hoja  son  letras  del  alfabeto  y
 cuyos  nodos  interiores  son  los caracteres *, +,-,/.
Diseñar una función que tome como parámetros un nodo y  un  árbol  binario  y  devuelva  el  resultado  entero  de  la
 evaluación  de  la expresión representada.'''
class Nodo:
    def __init__(self,data):
        self.data=data
        self.izquierdo=None
        self.derecho=None


class Arbol:
    def __init__(self):
        self.raiz=None

    def esHoja(self, nodo):
        if nodo.izquierdo==None and nodo.derecho==None:
            return True
        else:
            return False
    def TieneHijos(self,nodo):
        if nodo.izquierdo!=None or nodo.derecho!=None:
            return True
        else:
            return False
    def TieneHijoIzquierdo(nodo):
        if nodo.izquierdo!=None:
            return True
        else:
            return False

    def TieneHijoDerecho(nodo):
        if nodo.derecho!=None:
            return True
        else:
            return False


def funcionValor(a):
    return random.randrange(100)

def evaluarExpresion(arbol,nodo):
    if esHoja(nodo):
        return funcionValor(nodo)
    else:
        if nodo.data=='+':
            return evaluarExpresion(nodo.izquierdo,nodo.izquierdo.raiz) + evaluarExpresion(nodo.derecho,nodo.derecho.raiz)
        if nodo.data=='-':
            return evaluarExpresion(nodo.izquierdo,nodo.izquierdo.raiz) - evaluarExpresion(nodo.derecho,nodo.derecho.raiz)
        if nodo.data=='*':
            return evaluarExpresion(nodo.izquierdo,nodo.izquierdo.raiz) * evaluarExpresion(nodo.derecho,nodo.derecho.raiz)
        if nodo.data=='/':
            return evaluarExpresion(nodo.izquierdo,nodo.izquierdo.raiz) / evaluarExpresion(nodo.derecho,nodo.derecho.raiz)

#EJERCICIO 3
#recursiva
def inorderRecursiva(arbol):
    if esHoja(arbol.raiz):
        return arbol.raiz.data
    else:
        return inorderRecursiva(arbol.raiz.izquierdo)
        print(arbol.raiz.data)
        return inorderRecursiva(arbol.raiz.derecho)

#iterativa
def inorderiterativo(arbol):
    lista=[]
    if esHoja(arbol.raiz):
        lista.append(arbol.raiz.data)
    else:
        while(arbol.raiz.izquierdo!=None):
            lista.append(arbol.raiz.izquierdo.data)



#Escribir una función recursiva que encuentre el número de nodos de un árbol binario.
def cantNodos(arbol):
    if esHoja(arbol.raiz):
        return 1
    else:
        return 1+cantNodos(arbol.raiz.izquierdo)+cantNodos(arbol.raiz.derecho)

#Escribir una función recursiva que encuentre la altura de un árbol binario.
def altura(arbol):










