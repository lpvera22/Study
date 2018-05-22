# *-* encoding:UTF-8 *-*
'''Dada uma sequência de números inteiros x 1 , x 2 , ...., x n ordenada em ordem crescente e dado um valor
inteiro k, elabore um algoritmo para determinar o menor inteiro na sequência maior do que k. Caso este valor
não exista, o algoritmo deve informar este fato. Obs: k pode não estar na sequência. A complexidade do
algoritmo considerando o número de comparações realizadas deve ser θ (logn).'''
from PyQt4.uic.Compiler.qtproxies import i18n_void_func


def MenorEnteroMayorSecuencia(secuencia,n,k):
    if k==secuencia[n]:
        print 'Impossible to return the element'
    elif k ==secuencia[n/2]:
        return secuencia[n/2+1]

    elif k > secuencia[n/2]:
        return MenorEnteroMayorSecuencia(secuencia[n/2:n],n/2,k)
    elif k < secuencia[n/2]:
        return MenorEnteroMayorSecuencia(secuencia[0:n/2], n / 2, k)
    else:
        print('Element not found')

if __name__=="__main__":
    n=int(input('n'))
    sec= raw_input('secuencia').split( )
    secuencia=[int(i) for i in sec]






    k=int(input('k'))
print(MenorEnteroMayorSecuencia(secuencia,n-1,k))








