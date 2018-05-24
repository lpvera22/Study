# *-* encoding:UTF-8 *-*
'''Dado um conjunto S com n elementos, elabore um algoritmo que imprima todos os subconjuntos de S.'''

def Subconjuntos(conjunto):

    subconjuntos = []
    set_size = len(conjunto)
    if set_size > 1:
        subconjuntos += Subconjuntos(conjunto[1:])
        elemento = [conjunto[0]]
        for sub in subconjuntos[:]:
            subconjuntos.append(sub + elemento)
        subconjuntos.append(elemento)
    else:
        subconjuntos += [conjunto]


    return subconjuntos



    


    return subc
if __name__ == '__main__':
    sec = raw_input('A').split()
    S = [int(i) for i in sec]

    #n = int(input('n'))
    print(Subconjuntos(S))


