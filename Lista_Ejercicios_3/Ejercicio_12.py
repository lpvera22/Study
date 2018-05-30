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


        inicio=0
        fin=n-1

        while (inicio<fin ):
            medio=(fin+inicio)/2
            if matriz[medio][0]<=x :
                if matriz[medio][n-1]>=x:
                    inicio=medio
                    fin=medio

                else:
                    inicio=medio+1
            else:
                fin=medio-1

        fila = inicio
        inicio=0
        fin=n-1
        flag1=True

        while(inicio<=fin ):
            if matriz[fila][(inicio + fin) / 2] == x:
                flag1=False
                return fila, (inicio + fin) / 2

            elif x > matriz[fila][(inicio + fin) / 2]:
                inicio = (fin+inicio)/2+1
            else:
                fin=(inicio+fin)/2-1
        print('Element not found')
if __name__ == "__main__":
    n = int(input('n'))
    m=[]
    for i in range(n):
        sec = raw_input('secuencia').split()
        S = [int(i) for i in sec]
        m.append(S)
    print(m)

    x = int(input('x'))
    print(localizacionX(m,n,x))


























