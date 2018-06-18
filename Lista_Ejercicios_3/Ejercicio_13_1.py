# *-* encoding:UTF-8 *-*
'''Dada uma seqüência S, com n elementos e dado um inteiro k : 1 ≤ k ≤ n, considere a seguinte solução para
o problema de encontrar o k-ésimo maior elemento da seqüência:
Base : k=1. Retorne o maior elemento da seqüência em questão
H.I. : Sabemos resolver o problema para k’ < k
Passo: Se k=1, basta aplicar a base. Caso contrário, seja x o maior elemento da seqüência S e seja
S’ = S – {x}. Aplique a hipótese de indução à seqüência S’ tomando k’ = k-1.'''
def Encontrarkesimo(X,n,k):
    if k<1 or k>n:
        print('Error')
    else:
        S=sub_s(0,n-1,k,X)
        print S
def sub_s(l,r,k,X):
    if l==r:
        return X[l]
    else:
        X,medio=Partition(X,l,r)
        if r-medio+1>=k:
            return sub_s(medio, r, k, X)
        else:
            return sub_s(l,medio-1,k-(r-medio+1),X)

def Partition(X,left,right):
    l=left
    r=right
    pivot=X[r]
    while l<r:
        while (X[r] >= pivot and r >= l):
            r = r - 1
        while( X[l]<pivot and l<=r):
            l+=1

        if l<r:
            X[l],X[r]=X[r],X[l]
    medio=l
    X[right],X[medio]=X[medio],X[right]
    return X,medio



    # aux = S[0]
    # for i in range(n, 1):
    #     if i > aux:
    #         aux = S[i]
    # if k==1: #Base: k = 1.Retorne o maior elemento da seqüência em questão
    #
    #     return aux
    # else:
    #     S.remove(aux)
    #     return Encontrarkesimo(S,n-1,k-1)

if __name__=="__main__":
    n=int(input('n'))
    sec= raw_input('secuencia').split( )
    S=[int(i) for i in sec]
    k = int(input('k'))
    Encontrarkesimo(S,n,k)


