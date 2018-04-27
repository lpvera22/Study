import numpy as np
import random
from time import time
#Arreglo ordenado
class FilaPrioridad:
    def __init__(self,MAX):
        self.fila=np.zeros(MAX,dtype=int)
        self.MAX=MAX

    def FilaVacia(self):
        if len(self.fila)==0:
            return True
        else:
            return False


    def Inserir(self,elem):
        if len(self.fila)<self.MAX:
            self.fila[len(self.fila)]=elem
            pos=len(self.fila)-1
            while(self.fila[pos]>self.fila[pos-1] and pos!=0):
                aux=self.fila[pos-1]
                self.fila[pos-1]=self.fila[pos]
                self.fila[pos]=aux
                pos=pos-1
            return True
        elif self.FilaVacia():
            self.fila[0]=elem

        else:
            print('Fila llena')
    def Remover(self):
        if self.FilaVacia():
            print('Fila Vacia')
        else:
            aux=self.fila[0]
            for i in range(len(self.fila)-1):
                self.fila[i]=self.fila[i+1]
            return aux

    def Verificar(self):
        return self.fila[0]

class FilaPrioridadDesordenado:
    def __init__(self, MAX):
        self.fila = np.zeros(MAX, dtype=int)
        self.MAX = MAX

    def FilaVacia(self):
        if len(self.fila) == 0:
            return True
        else:
            return False
#Arreglo desordenado
    def InserirD(self, elem):
        if len(self.fila) < self.MAX:
            self.fila[len(self.fila)] = elem

        elif self.FilaVacia():
            self.fila[0] = elem

        else:
            print('Fila llena')

    def BuscarElemMayorPrior(self):
        if self.FilaVacia():
            print('Fila Vacia')
        elif len(self.fila)==1:
            return self.fila[0]
        else:
            aux=self.fila[0]
            pos=0
            for i in range(len(self.fila)):
                if aux<self.fila[i]:
                    aux=self.fila[i]
                    pos=i
            return pos

    def RemoverD(self):
        if self.FilaVacia():
            print('Fila Vacia')
        else:
            pos=self.BuscarElemMayorPrior()
            for i in range(pos,len(self.fila)):
                self.fila[i]=self.fila[i+1]





    def VerificarD(self):
        pos=self.BuscarElemMayorPrior()
        return self.fila[pos]

class FilaPrioridadH:
    def __init__(self, MAX):
        self.fila = np.zeros(MAX, dtype=int)
        self.MAX = MAX
        self.cantidad=0

    def FilaVacia(self):
        if self.cantidad == 0:
            return True
        else:
            return False
#Heap
    def InsertarH(self,elem):
        if self.FilaVacia():
            self.fila[0]=elem
        elif len(self.fila)==self.MAX:
            print('Fila llena')
        else:
            self.fila[len(self.fila)]=elem
            pos=len(self.fila)
            j=pos/2
            while(self.fila[pos-1]>self.fila[j-1]):
                self.fila[j-1],self.fila[pos-1]=self.fila[pos-1],self.fila[j-1]

                pos=j
                j=pos/2
        self.cantidad+=1

    def RemoverH(self):
        if self.FilaVacia():
            print('Fila Vacia')
        else:
            x=self.fila[0]
            i=0
            self.fila[0]=self.fila[self.cantidad-1]
            self.fila[self.cantidad-1]=0
            while(i<=(self.cantidad/2)-1):
                if self.fila[2*i+1]>self.fila[2*i+2]:
                    self.fila[i],self.fila[2*i+1]=self.fila[2*i+1],self.fila[i]

                    i=2*i+1
                else:
                    self.fila[i], self.fila[2 * i + 2] = self.fila[2 * i + 2], self.fila[i]

                    i = 2 * i + 2

            return x

    def VerificarH(self):
        return self.fila[0]




if __name__=="__main__":

    filaD=FilaPrioridadDesordenado(100)
    filaOr=FilaPrioridad(100)
    filaheap=FilaPrioridadH(100)

    time1=time()
    for i in range(100):
        filaD.InserirD(random.randint())
    print(time()-time1)

    time2 = time()
    for i in range(100):
        filaOr.Inserir(random.randint())
    print(time() - time2)

    time3 = time()
    for i in range(100):
        filaheap.InsertarH(random.randint())
    print(time() - time3)







        








