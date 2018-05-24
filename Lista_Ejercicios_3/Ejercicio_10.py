# *-* encoding:UTF-8 *-*
'''Dada uma seqüência S = x 1 x 2 .....x n , com n números inteiros tais que para todo i, 0 ≤ x i ≤ 1000, elabore um
algoritmo (usando indução) que determine o número de vezes que cada valor entre 0 e 1000 ocorre na
seqüência. O seu algoritmo deve ter complexidade O(n). Obs: a seqüência S não está ordenada e pode conter
elementos repetidos.'''
def CantRepeti(secuencia,n):
    aux={()}
    aux.add(secuencia[0],1)

    for i in range(n,1):
        if secuencia[i]=

