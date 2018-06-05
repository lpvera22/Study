# *-* encoding:UTF-8 *-*
'''Dada uma sequência x 1 , x 2 , ...., x n , a multiplicidade de um elemento x é definida como sendo o
número de vezes que este elemento ocorre na sequência. Além disso, um número z é dito a maioria da sequência
se a sua multiplicidade é maior do que n/2. Escreva um algoritmo que determina a maioria (se ela existir) de uma
sequência realizando no máximo 2n-2 comparações.'''

def Maioria(secuencia,n):
    aux = {}
    if n> 1:

        aux = {}

        for i in range(n):
            aux[secuencia[i]] = 0

        for i in range(n):
            aux[secuencia[i]] += 1
        # print aux
        multi = max(aux.items(),key=lambda p:p[1])
        return multi if (multi[1]/2)+1 else None
    else:
        return secuencia[0]
secuencia=[1,2,2,2,3]
n=5
print (Maioria(secuencia,n))






