# *-* encoding:UTF-8 *-*
'''a) Dada uma sequência ordenada em ordem crescente com n números inteiros distintos todos entre 1 e n+1,
elabore um algoritmo que determine o número que está faltando na sequência. A complexidade do seu
algoritmo deve ser O(log n), considerando o número de vezes que os ele9mentos da sequência são acessados,
isto é, o seu algoritmo pode realizar no máximo O(log n) acessos à sequência.
b) Considerando esta função de complexidade, responda se o seu algoritmo é Θ (log n). Justifique.'''

def ElementMissing(secuencia,n):
    tam=n+1
    if tam==2 :
        if secuencia[1]-secuencia[0]!=1:
            return secuencia[0]+1

        else:
            return None

    else:
        val=(secuencia[n]-secuencia[0])/2+secuencia[0]
        if secuencia[tam/2]!=val:
            return ElementMissing(secuencia[0:(tam/2)+1],tam/2)
        else:
            return ElementMissing(secuencia[(tam/2):tam],n/2)

if __name__=="__main__":
    n=int(input('n'))
    sec= raw_input('secuencia').split( )
    S=[int(i) for i in sec]
    #k = int(input('k'))
    print(ElementMissing(S,n))



