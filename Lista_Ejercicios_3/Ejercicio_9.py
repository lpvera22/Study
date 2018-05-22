# *-* encoding:UTF-8 *-*
'''Dado um conjunto S com n elementos, elabore um algoritmo que imprima todos os subconjuntos de S.'''

def Subconjuntos(S,n):
    subc=set()

    for i in S:
        subc.add(i)
    i=0
    j=1
    while( i<=n-1 and j<=n-1):

        if j<n-1:
            subc.add((S[i],S[j]))
            j=j+1
        elif j==n-1 and i<n-1:
            subc.add((S[i], S[j]))

            i=i+1
            j=i+1
        elif j == n - 1 and i==n-1:
            subc.add((S[i], S[j]))


    return subc
if __name__ == '__main__':
    sec = raw_input('A').split()
    S = [int(i) for i in sec]

    n = int(input('n'))
    print(Subconjuntos(S,n))


