# *-* encoding:UTF-8 *-*
'''Dada uma sequência de números inteiros, elabore um algoritmo para obter a mediana da sequência. A
complexidade do seu algoritmo, no melhor caso, deve ser θ (n) e, no pior caso, θ (n^2 ).'''

def Mediana(secuencia):

    n=len(secuencia)

    if n==2:
        suma=float(secuencia[0])+float(secuencia[1])
        media=float(suma/2)
        return media
    elif n==1:
        return secuencia[0]
    else:

        for i in range (n):

            for j in range(n):
                if secuencia[j]<secuencia[i]:
                    secuencia[i],secuencia[j]=secuencia[j],secuencia[i]

        if n % 2 != 0:
            return secuencia[n / 2]
        else:
            suma=(float(secuencia[(n / 2)-1])+float(secuencia[n/2]))
            media=float(suma/2)
            return media
if __name__=='__main__':
    sec = raw_input('secuencia').split()
    secuencia = [int(i) for i in sec]

    print Mediana(secuencia)





