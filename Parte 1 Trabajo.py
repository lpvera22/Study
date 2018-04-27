#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import heappush, heappop, nsmallest
import numpy as np
import random
from time import time


# Array ordenado
class FilaPrioridad:
    def __init__(self, MAX):
        self.fila = np.array([None] * MAX)
        self.MAX = MAX
        self.cantidad = 0

    def FilaVacia(self):
        '''Verifica se é vazia olhando se a quantidade é 0'''
        if self.cantidad == 0:
            return True
        else:
            return False

    def Inserir(self, elem):
        '''O elemnto que vai ser adicionado é colocado na última posição e depois é colocado\
         na posição correta fazendo trocas'''
        if self.cantidad < self.MAX:
            self.fila[self.cantidad] = elem
            pos = len(self.fila) - 1
            while (self.fila[pos] > self.fila[pos - 1] and pos != 0):
                aux = self.fila[pos - 1]
                self.fila[pos - 1] = self.fila[pos]
                self.fila[pos] = aux
                pos = pos - 1
            self.cantidad += 1
            return True
        elif self.FilaVacia():
            self.fila[0] = elem
            self.cantidad += 1

        else:
            print('Fila llena')

    def Remover(self):
        '''Elimina o primeiro elemento e move a todos os elementos para o frente'''
        if self.FilaVacia():
            print('Fila Vacia')
        else:
            aux = self.fila[0]
            for i in range(len(self.fila) - 1):
                self.fila[i] = self.fila[i + 1]
            return aux

    def Verificar(self):
        '''Retorna o elemento na posição 0 que o de maior prioridade'''
        return self.fila[0]


# Array desordenado
class FilaPrioridadDesordenado:
    def __init__(self, MAX):
        self.fila = np.array([None] * MAX)
        self.MAX = MAX
        self.cantidad = 0

    def FilaVacia(self):
        '''Verifica se é vazia olhando se a quantidade é 0'''
        if self.cantidad == 0:
            return True
        else:
            return False

    def InserirD(self, elem):
        '''Sempre insere o elemento na última posição'''
        if self.cantidad < self.MAX:
            self.fila[self.cantidad] = elem
            self.cantidad += 1

        elif self.FilaVacia():
            self.fila[0] = elem
            self.cantidad += 1

        else:
            print('Fila llena')

    def BuscarElemMayorPrior(self):
        '''Procura o maior elemento da fila comparando com um pivote'''
        if self.FilaVacia():
            print('Fila Vacia')
        elif len(self.fila) == 1:
            return self.fila[0]
        else:
            aux = self.fila[0]
            pos = 0
            for i in range(len(self.fila)):
                if aux < self.fila[i]:
                    aux = self.fila[i]
                    pos = i
            return pos

    def RemoverD(self):
        '''Procura o maior elemento elimina ele movendo para o frente os restantes elementos\
        desde a posicão dele até o final'''
        if self.FilaVacia():
            print('Fila Vacia')
        else:
            pos = self.BuscarElemMayorPrior()
            for i in range(pos, self.cantidad - 1):
                self.fila[i] = self.fila[i + 1]
            self.cantidad -= 1

    def VerificarD(self):
        '''Procura o elemento de maio prioridade e retorna ele'''
        pos = self.BuscarElemMayorPrior()
        return self.fila[pos]


# Heap
class FilaPrioridadH:
    def __init__(self, MAX):
        self.fila = np.array([None] * MAX)
        self.MAX = MAX
        self.cantidad = 0

    def FilaVacia(self):
        '''Verifica se é vazia olhando se a quantidade é 0'''
        if self.cantidad == 0:
            return True
        else:
            return False

    def InsertarH(self, elem):
        '''Inserta o lemento na ultima posição e coloca ele na posição correta segúm\
        a propiedade do heap'''
        if self.FilaVacia():
            self.fila[0] = elem


        elif self.cantidad == self.MAX:
            print('Fila llena')
        else:
            self.fila[self.cantidad] = elem
            pos = self.cantidad
            j = pos / 2
            while (self.fila[pos] > self.fila[j]):
                self.fila[j], self.fila[pos] = self.fila[pos], self.fila[j]

                pos = j
                j = pos / 2
        self.cantidad += 1

    def RemoverH(self):
        '''Retorna o elemento da posição 0 e troca ele por o último elemento da fila\
        ahi depois ele e colocado na posição correta segúm a propiedade do heap'''
        if self.FilaVacia():
            print('Fila Vacia')
        else:
            x = self.fila[0]
            i = 0
            self.fila[0] = self.fila[self.cantidad - 1]
            self.fila[self.cantidad - 1] = None
            while (i <= (self.cantidad / 2) - 1):
                if self.fila[2 * i + 1] > self.fila[2 * i + 2]:
                    self.fila[i], self.fila[2 * i + 1] = self.fila[2 * i + 1], self.fila[i]

                    i = 2 * i + 1
                else:
                    self.fila[i], self.fila[2 * i + 2] = self.fila[2 * i + 2], self.fila[i]

                    i = 2 * i + 2
                self.cantidad -= 1
            return x

    def VerificarH(self):
        '''Retorna o elemento na posição 0 que o de maior prioridade'''
        return self.fila[0]


if __name__ == "__main__":
    tam = 10
    filaD = None
    filaOr = None
    filaheap = None
    biblioheap = None
    print('***  Inserção  ***')
    for i in range(5):
        tam = tam * 10
        print("tamnho:: " + str(tam))

        filaD = FilaPrioridadDesordenado(tam)
        filaOr = FilaPrioridad(tam)
        filaheap = FilaPrioridadH(tam)
        biblioheap = []

        time1 = time()
        for i in range(tam):
            filaD.InserirD(random.randint(0, 1000))
        timestamp = round(float(time() - time1), 4)
        print("FilaD: %f" % timestamp)

        time2 = time()
        for i in range(tam):
            filaOr.Inserir(random.randint(0, 1000))
        timestamp2 = round(float(time() - time2), 4)
        print("FilaOr: %f" % timestamp2)

        time3 = time()
        for i in range(tam):
            filaheap.InsertarH(random.randint(0, 1000))
        timestamp3 = round(float(time() - time3), 4)
        print("Heap: %f" % timestamp3)

        time4 = time()
        for i in range(tam):
            heappush(biblioheap, random.randint(0, 1000))
        timestamp4 = round(float(time() - time4), 4)
        print("Heapq: %f" % timestamp4)

        print("----------")

    print("***  Remoção  ***")
    cant = 0
    for i in range(5):
        cant = cant + 15
        print ('Remover: ' + str(cant) + ' vezes')
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

        time4 = time()
        for i in range(cant):
            heappop(biblioheap)
        timestamp4 = round(float(time() - time4), 4)
        print("Heapq: %f" % timestamp4)
        print("----------")

    print("***  Verificação  ***")
    time1 = time()
    filaD.VerificarD()
    timestamp = round(float(time() - time1), 4)
    print("FilaD: %f" % timestamp)
    time2 = time()
    filaOr.Verificar()
    timestamp1 = round(float(time() - time2), 4)
    print("FilaOr: %f" % timestamp1)
    time3 = time()
    filaheap.VerificarH()
    timestamp2 = round(float(time() - time3), 4)
    print("Heap: %f" % timestamp2)
    time4 = time()
    nsmallest(1, biblioheap)
    timestamp3 = round(float(time() - time4), 4)
    print("Heapq: %f" % timestamp3)