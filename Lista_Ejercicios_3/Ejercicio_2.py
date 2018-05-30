# *-* encoding:UTF-8 *-*
'''Dada uma sequência com n elementos, elabore um algoritmo para determinar o maior e o menor elemento da
sequência, sendo que o seu algoritmo deve realizar 3/2 n − 2 comparações.'''

def MayorMenor(secuencia,n):
    if n>1:
        if n%2>0:
            secuencia.append(secuencia[n])
            fin=n
        else:
            fin=n-1


        if secuencia[0]>secuencia[1]:
            mayor=secuencia[0]
            menor=secuencia[1]
        else:
            menor=secuencia[0]
            mayor=secuencia[1]



        for i in range(2,fin,2):
            if secuencia[i]>secuencia[i+1]:
                if secuencia[i]>mayor:
                    mayor=secuencia[i]
                if secuencia[i+1]<menor:
                    menor=secuencia[i+1]
            else:
                if secuencia[i]<menor:
                    menor=secuencia[i]
                if secuencia[i+1]>mayor:
                    mayor=secuencia[i+1]
        return mayor,menor



    else:
        return secuencia[0]
if __name__=="__main__":
    n=int(input('n'))
    sec= raw_input('secuencia').split( )
    S=[int(i) for i in sec]
    #k = int(input('k'))
    print(MayorMenor(S,n))





