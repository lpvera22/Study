# *-* encoding:UTF-8 *-*
'''Dada uma sequência x 1 , x 2 , ...., x n , a multiplicidade de um elemento x é definida como sendo o
número de vezes que este elemento ocorre na sequência. Além disso, um número z é dito a maioria da sequência
se a sua multiplicidade é maior do que n/2. Escreva um algoritmo que determina a maioria (se ela existir) de uma
sequência realizando no máximo 2n-2 comparações.'''

def Maioria(secuencia,n):
    if n==1:
        return secuencia[0]
    else:
        c=secuencia[0]
        m=1
        for i in range(1,n):
            if m==0:
                c=secuencia[i]
                m=1
            else:
                if c==secuencia[i]:
                    m=m+1
                else:
                    m=m-1
        if m==0:
            return None
        else:
            count=0
            for i in range(n):
                if secuencia[i]==c:
                    count+=1
            if count>n/2:
                return c
            else:
                return None




#     aux = {}
#     if n> 1:
#
#         aux = {}
#
#         for i in range(n):
#             aux[secuencia[i]] = 0
#
#         for i in range(n):
#             aux[secuencia[i]] += 1
#         # print aux
#         multi = max(aux.items(),key=lambda p:p[1])
#         return multi if (multi[1]/2)+1 else None
#     else:
#         return secuencia[0]
secuencia=[1,2,3,2,2]
n=5
print (Maioria(secuencia,n))






