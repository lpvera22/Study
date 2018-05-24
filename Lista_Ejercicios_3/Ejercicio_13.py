# *-* encoding:UTF-8 *-*
'''Dada uma seqüência S, com n elementos e dado um inteiro k : 1 ≤ k ≤ n, considere a seguinte solução para
o problema de encontrar o k-ésimo maior elemento da seqüência:
Base : k=1. Retorne o maior elemento da seqüência em questão
H.I. : Sabemos resolver o problema para k’ < k
Passo: Se k=1, basta aplicar a base. Caso contrário, seja x o maior elemento da seqüência S e seja
S’ = S – {x}. Aplique a hipótese de indução à seqüência S’ tomando k’ = k-1.'''
def Encontrarkesimo(S,n,k):


    aux = S[0]
    for i in range(n, 1):
        if i > aux:
            aux = S[i]
    if k==1: #Base: k = 1.Retorne o maior elemento da seqüência em questão

        return aux
    else:
        S.remove(aux)
        return Encontrarkesimo(S,n-1,k-1)

if __name__=="__main__":
    n=int(input('n'))
    sec= raw_input('secuencia').split( )
    S=[int(i) for i in sec]
    k = int(input('k'))
    print(Encontrarkesimo(S,n,k))


