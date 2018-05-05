#Matriz de adjacência
class GrafoMatrizAdya:
    def __init__(self):
        self.vertices=None
        self.aristas=None
        self.matrizAdya=[[]]

    #1) Árvore geradora mínima:
    #a. Algoritmo de Prim
def GrafoMatrizAy_Prim(grafo,origen):

    listaVisitados = []
    grafoResultante = {}
    listaOrdenada = []

    # 2.- AGREGAR EL NODO ORIGEN A LA LISTA DE VISITADOS
    listaVisitados.append(origen)

    # 3.- AGREGAR SUS ADYACENTES A LA LISTA ORDENADA
    for i in grafo.matrizAdya[origen][i]:
        if grafo.matrizAdya[origen][i]!=None:
            listaOrdenada.append((origen, i, grafo.matrizAdya[origen][i]))

    '''ORDENAMIENTO INSERT PARA LA LISTA'''
    pos = 0
    act = 0
    listAux = []
    for i in range(len(listaOrdenada)):
        listAux = listaOrdenada[i]
        act = listaOrdenada[i][2]
        pos = i
        while pos > 0 and listaOrdenada[pos - 1][2] > act:
            listaOrdenada[pos] = listaOrdenada[pos - 1]
            pos = pos - 1
    listaOrdenada[pos] = listAux

    # 4.- MIENTRAS LA LISTA ORDENADA NO ESTE VACIA, HACER:
    while listaOrdenada:
        # 5.-TOMAR VERTICE DE LA LISTA ORDENADA Y ELIMINARLO
        vertice = listaOrdenada.pop(0)
        d = vertice[1]
        # 6.-SI EL DESTINO NO ESTA EN LA LISTA DE VISITADOS
        if d not in listaVisitados:
            # 7.- AGREGAR A LA LISTA DE VISITADOS EN NODO DESTINO
            listaVisitados.append(d)
            # 8.- AGREGAR A LA LISTA ORDENADA LOS ADYACENTES DEL NODO DESTINO
            # "d" QUE NO HAN SIDO VISITADOS
            for key, lista in grafo[d]:
                if key not in listaVisitados:
                    listaOrdenada.append((d, key, lista))
            #####ORDENAMIENTO APLICADO A LA LISTA :
            listaOrdenada = [(c, a, b) for a, b, c in listaOrdenada]
            listaOrdenada.sort()
            listaOrdenada = [(a, b, c) for c, a, b in listaOrdenada]

            # 9.-AGREGAR VERTICE AL GRAFO RESULTANTE

            origen = vertice[0]
            destino = vertice[1]
            peso = vertice[2]

            if origen in grafoResultante:
                if destino in grafoResultante:
                    lista = grafoResultante[origen]
                    grafoResultante[origen] = lista + [(destino, peso)]
                    lista = grafoResultante[destino]
                    lista.append((origen, peso))
                    grafoResultante[destino] = lista
                else:
                    grafoResultante[destino] = [(origen, peso)]
                    lista = grafoResultante[origen]
                    lista.append((destino, peso))
                    grafoResultante[origen] = lista
            elif destino in grafoResultante:
                grafoResultante[origen] = [(destino, peso)]
                lista = grafoResultante[destino]
                lista.append((origen, peso))
                grafoResultante[destino] = lista
            else:
                grafoResultante[destino] = [(origen, peso)]
                grafoResultante[origen] = [(destino, peso)]



#Lista de adjacência
class GrafoListaAdy:
    def __init__(self):
        self.vertices=None
        self.listaAdy={}

#Matriz de incidência
#class MatrizIncidencia:



