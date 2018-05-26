# *-* encoding:UTF-8 *-*
'''Dados um vetor ordenado A com n números reais e um número real x, escreva um algoritmo para determinar
se existem A[i] e A[j] tais que x = A[i] +A[j], sendo que o seu algoritmo dever ter complexidade O(n) para este
problema. Dica: O que se pode concluir da comparação de A[1] + A[n] com x?'''

def sumaigualx(A,x,n):
    if n>1:
        i=0
        j=n-1

        while(A[i]!=A[j] and i<=j):
            if A[i]+A[j]>x:
                j=j-1
            elif A[i]+A[j]<x:
                i=i+1
            elif A[i]+A[j]==x:
                print(A[i],A[j])
                i=i+1
                j=j-1
    else:
        return A[0]

if __name__ == '__main__':
    sec = raw_input('A').split()
    A = [int(i) for i in sec]
    x = int(input('x'))
    n = int(input('n'))

    print sumaigualx(A,x,n)

