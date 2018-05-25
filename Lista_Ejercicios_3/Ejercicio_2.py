# *-* encoding:UTF-8 *-*
'''Dada uma sequência com n elementos, elabore um algoritmo para determinar o maior e o menor elemento da
sequência, sendo que o seu algoritmo deve realizar 3/2 n − 2 comparações.'''

def MayorMenor(secuencia,n):
    if n>1:
        if secuencia[0]>secuencia[1]:
            mayor=secuencia[0]
            menor=secuencia[1]
        else:
            menor=secuencia[1]
            mayor=secuencia[0]
        i=2
        for i in range(2,n):
            if secuencia[i]>mayor:
                mayor=secuencia[i]
            elif secuencia[i]<menor:
                menor=secuencia[i]
        return mayor,menor

    else:
        return secuencia[0]
if __name__=="__main__":
    n=int(input('n'))
    sec= raw_input('secuencia').split( )
    S=[int(i) for i in sec]
    #k = int(input('k'))
    print(MayorMenor(S,n))





