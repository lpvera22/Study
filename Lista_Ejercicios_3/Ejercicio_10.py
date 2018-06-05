# *-* encoding:UTF-8 *-*
'''Dada uma seqüência S = x 1 x 2 .....x n , com n números inteiros tais que para todo i, 0 ≤ x i ≤ 1000, elabore um
algoritmo (usando indução) que determine o número de vezes que cada valor entre 0 e 1000 ocorre na
seqüência. O seu algoritmo deve ter complexidade O(n). Obs: a seqüência S não está ordenada e pode conter
elementos repetidos.'''
def CantRepeti(secuencia,n):
    aux = {}
    if n!=1:

        aux={}

        for i in secuencia:
            aux[i]=0

        for i in range(n):
            aux[secuencia[i]]+=1
    else:
        aux[secuencia[0]]=1
    return aux
if __name__ == '__main__':
    sec = raw_input('A').split()
    S = [int(i) for i in sec]

    n = int(input('n'))
    print(CantRepeti(S,n))


