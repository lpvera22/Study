# *-* encoding:UTF-8 *-*

'''Considere a matriz A, de dimensão nxn, onde o elemento da linha i e da coluna j é denotado por A ij .
Sabendo que
A ij < A ik , para todo i e j < k
A ij < A kj para todo j e i < k
elabore um algoritmo que, dado elemento x, determine a localização de x na matriz A. O seu algoritmo deve
realizar O(n) comparações no pior caso.'''

def localizacionX(matriz,n,x):
    if n==1:
        if matriz[n-1][n-1]==x:
            print(n-1,n-1)
        else:
            print('Element not found')
    else:

        if matriz[n/2][0]>x:
            fin=n/2
            inicio=0

        else:
            inicio=n/2
            fin=n

        while (inicio<=fin):
            if matriz[inicio][0]<x and matriz[inicio][n]>x:
                fila=inicio

               flag=False
            else:inicio=inicio+1
        if matriz[fila][n/2]==x:
            return fila,n/2
        elif x>matriz[fila][n/2]:
            inicio=n/2
            fin=n
        else: inicio=0
        fin=n/2
        while(inicio<=fin):
            if matriz[fila][inicio]==x:
                return fila,inicio
            else
                inicio=inicio+1





















