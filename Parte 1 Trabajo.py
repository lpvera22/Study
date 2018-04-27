#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random
from time import time
#import matplotlib.pyplot as plt

#Arreglo ordenado
class FilaPrioridad:
    def __init__(self,MAX):
        self.fila=np.array([None]*MAX)
        self.MAX=MAX
        self.cantidad=0

    def FilaVacia(self):
        if self.cantidad==0:
            return True
        else:
            return False


    def Inserir(self,elem):

        if self.cantidad<self.MAX:
            self.fila[self.cantidad]=elem
            pos=len(self.fila)-1
            while(self.fila[pos]>self.fila[pos-1] and pos!=0):
                aux=self.fila[pos-1]
                self.fila[pos-1]=self.fila[pos]
                self.fila[pos]=aux
                pos=pos-1
            self.cantidad+=1
            return True
        elif self.FilaVacia():
            self.fila[0]=elem
            self.cantidad+=1

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
        self.fila = np.array([None]*MAX)
        self.MAX = MAX
        self.cantidad = 0

    def FilaVacia(self):
        if self.cantidad == 0:
            return True
        else:
            return False
#Arreglo desordenado
    def InserirD(self, elem):

        if self.cantidad < self.MAX:
            self.fila[self.cantidad] = elem
            self.cantidad+=1

        elif self.FilaVacia():
            self.fila[0] = elem
            self.cantidad+=1

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
            for i in range(pos,self.cantidad-1):
                self.fila[i]=self.fila[i+1]
            self.cantidad-=1




    def VerificarD(self):
        pos=self.BuscarElemMayorPrior()
        return self.fila[pos]

class FilaPrioridadH:
    def __init__(self, MAX):
        self.fila = np.array([None]*MAX)
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


        elif self.cantidad==self.MAX:
            print('Fila llena')
        else:
            self.fila[self.cantidad]=elem
            pos=self.cantidad
            j=pos/2
            while(self.fila[pos]>self.fila[j]):
                self.fila[j],self.fila[pos]=self.fila[pos],self.fila[j]

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
            self.fila[self.cantidad-1]=None
            while(i<=(self.cantidad/2)-1):
                if self.fila[2*i+1]>self.fila[2*i+2]:
                    self.fila[i],self.fila[2*i+1]=self.fila[2*i+1],self.fila[i]

                    i=2*i+1
                else:
                    self.fila[i], self.fila[2 * i + 2] = self.fila[2 * i + 2], self.fila[i]

                    i = 2 * i + 2
                self.cantidad-=1
            return x

    def VerificarH(self):
        return self.fila[0]




if __name__=="__main__":
    tam = 10
    filaD=None
    filaOr=None
    filaheap=None
    print('Inserção')
    for i in range(5):
        tam=tam*10
        print("tamnho:: "+str(tam))

        filaD=FilaPrioridadDesordenado(tam)
        filaOr=FilaPrioridad(tam)
        filaheap=FilaPrioridadH(tam)

        time1=time()
        for i in range(tam):
            filaD.InserirD(random.randint(0,1000))
        timestamp = round(float(time()-time1),4)
        print("FilaD: %f" %timestamp)
        #print (filaD.fila)

        time2 = time()
        for i in range(tam):
           filaOr.Inserir(random.randint(0,1000))
        timestamp2 = round(float(time() - time2),4)
        print("FilaOr: %f" %timestamp2)
       # print(filaOr.fila)

        time3 = time()
        for i in range(tam):
            filaheap.InsertarH(random.randint(0,1000))
        timestamp3 = round(float(time() - time3),4)
        print("Heap: %f" %timestamp3)
        #print(filaheap.fila)
        print("----------")

    # filaheap = FilaPrioridadH(10)
    # filaheap.InsertarH(25)
    # filaheap.InsertarH(65)
    # filaheap.InsertarH(2)
    # filaheap.InsertarH(125)
    # filaheap.InsertarH(84)
    # print(filaheap.fila)
    # filaheap.RemoverH()
    # print(filaheap.fila)
    cant =0
    for i in range(5):
        #cant = random.randint(0,100)
        cant = cant+15
        print ('Remover: ' +str(cant)+' vezes')
        time1 = time()
        for i in range(cant):
            filaD.RemoverD()
        timestamp = round(float(time() - time1), 4)
        print("FilaD: %f" % timestamp)

        time2 = time()
        for i in range(cant):
            filaOr.Remover()
        timestamp1 = round(float(time() - time2), 4)
        print("FilaOr: %f" % timestamp1)

        time3 = time()
        for i in range(cant):
            filaheap.RemoverH()
        timestamp2 = round(float(time() - time3), 4)
        print("Heap: %f" % timestamp2)
        print('-----------------')

        








