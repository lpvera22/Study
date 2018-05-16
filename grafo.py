# *-* encoding:UTF-8 *-*
import numpy as np
from random import *
graphic = True
try:

    import networkx as nx
    import matplotlib.pyplot as plt

except Exception as e:
    print e
    graphic = False
    print("Para apresentar o grafo visualmente é preciso ter instalado a biblioteca networkx e matplotlib de python\
 mas mismo assim os dados seram aprensentados na consola\n")

from time import *

#Metodo para gerar um grafo conexo
def GenGrafo(vert, edges, min_weight=1, max_weight=100):
        if edges > vert * (vert - 1) // 2:
            print("Graph cannot be generated. Too many edges")
            return None
        else:
            matriz = np.zeros((vert, vert), dtype=np.int)
            degree = np.zeros(vert, dtype=np.int)
            num_edges = 0

            lst_vert = [i for i in range(vert)]

            # shuffle(lst_vert)
            open_list = [lst_vert.pop(0)]
            while len(lst_vert) > 0 and num_edges < edges:
                v1 = open_list[randint(0, len(open_list) - 1)]
                v2 = lst_vert.pop(0)

                degree[v1] += 1
                degree[v2] += 1

                matriz[v1][v2] = matriz[v2][v1] = randint(min_weight, max_weight)

                num_edges += 1
                open_list.append(v2)
            while num_edges < edges:
                v1 = v2 = randint(0, vert - 1)
                while degree[v1] == vert - 1:
                    v1 = v2 = randint(0, vert - 1)

                while v2 == v1 or matriz[v1][v2] == True:
                    v2 = randint(0, vert - 1)

                matriz[v1][v2] = matriz[v2][v1] = randint(min_weight, max_weight)

                degree[v1] += 1
                degree[v2] += 1

                num_edges += 1

            return (open_list, matriz)


# Matriz de adjacência
class GrafoMatrizAdya:

    def __init__(self,vert,matriz):
        self.vertices, self.matrizAdya = vert,matriz

    def printMatrix(self):#Metodo para imprimir a matriz de adjacência do grafo
        for i in range(len(self.matrizAdya)):
            for j in range(len(self.matrizAdya)):
                print("%i" % self.matrizAdya[i][j]),
            print

    def pesoarista(self, v1, v2):
        return self.matrizAdya[v1][v2]

    def vertadyac(self, v1):
        ady = []
        for i in range(len(self.vertices)):

            if self.matrizAdya[self.vertices.index(v1)][i] != 0:
                ady.append(i)
        return ady


    def DrawGraph(self, prim): #Metodo para apresentar grafo visualmente
        l_prim = [i[:2] for i in prim]
        graph = nx.Graph()
        plt.axis('off')
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if (self.matrizAdya[i][j] != 0):
                    graph.add_edge(self.vertices[i], self.vertices[j], peso=self.matrizAdya[i][j])
        pos = nx.spring_layout(graph)
        labels = nx.get_edge_attributes(graph, 'peso')
        nx.draw_networkx(graph, pos)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        nx.draw_networkx_edges(graph, pos, edgelist=l_prim, width=3, edge_color='b')

        plt.show()

    # 1) Árvore geradora mínima:
    # a. Algoritmo de Prim
def GrafoMatrizAy_Prim(grafo, origen):

    #definição da fila com prioridade
    cola = []

    #se insere no procesamento o primeiro nodo
    pos = grafo.vertices.index(origen)
    cola.append((pos, pos, 0))
    visited = [grafo.vertices[pos]]

    mst = [] #lista para almacenar os resultados

    #embora a fila não esteja vacia tiro u primer elemento, marco ele como visitado e adiciono na fila us vertices adyacentes a ele
    while (len(cola) != 0):

        u = cola.pop(0)
        if grafo.vertices[u[1]] not in visited:
            visited.append(grafo.vertices[u[1]])
            mst.append(u)

        for i in range(len(grafo.vertices)):# percoro a matriz de adyacencia para pegar u peso da aresta que une os nodos
            if grafo.matrizAdya[u[1]][i] != 0 and grafo.vertices[i] not in visited:
                cola.append((u[1], i, grafo.matrizAdya[u[1]][i]))
        cola = sorted(cola, key=lambda e: e[2])#ordena fila segum peso de aresta
    print("Prim: "+str(mst))
    return mst


'''2) Os caminhos mais curtos a partir de um vértice v até todos os outros vértices :
          a.Algoritmo de Dijkstra'''


def GrafoMatrizAy_Dijkstra(grafo, origen):
    distancia=[float('inf')] *len(grafo.vertices)
    visto=[False] *len(grafo.vertices)
    padre=[None] *len(grafo.vertices)

    distancia[grafo.vertices.index(origen)]=0
    list_aux=[]# fila com prioridade
    list_aux.append((origen,distancia[grafo.vertices.index(origen)]))

    while len(list_aux)!=0:
        u=list_aux.pop(0)
        visto[u[0]]=True
        ady=grafo.vertadyac(u[0])

        for i in range(len(ady)):
            #si distancia[v] > distancia[u] + peso (u, v) hacer
            if distancia[ady[i]]> distancia[u[0]]+ grafo.pesoarista(u[0],ady[i]):

                #distancia[v] = distancia[u] + peso (u, v)
                distancia[ady[i]]=distancia[u[0]]+ grafo.pesoarista(u[0],ady[i])
                #padre[v] = u
                padre[ady[i]]=u[0]

                #adicionar(cola,(v, distancia[v])
                list_aux.append((ady[i],distancia[ady[i]]))
                list_aux.sort(key=lambda x: x[1])
    return padre,distancia


def GrafoMatrizAy_Floyd(grafo):
    cn = len(grafo.vertices)
    x = [[float('inf')] * cn for i in range(cn)]
    for i in range(cn):
        for j in range(cn):
            if i == j:
                x[i][j] = 0
            elif grafo.matrizAdya[i][j] != 0:
                x[i][j] = grafo.matrizAdya[i][j]
    dt = 0
    for k in range(cn):
        for i in range(cn):
            for j in range(cn):
                dt = x[i][k] + x[k][j]
                if (x[i][j] > dt):
                    x[i][j] = dt
    return x


# Implementación del algoritmo Kruskal

# Función para generar conuntos
def make_set(v,base,ordi):
    base[v] = v
    ordi[v] = 0


# Implementación de la función de búsqueda
# de manera recursiva
def find(v,base):
    if base[v] != v:
        base[v] = find(base[v],base)
    return base[v]


# Implementación de la unión de conjuntos
def union(u, v,base,ordi):
    v1 = find(u,base)
    v2 = find(v,base)
    if v1 != v2:
        if ordi[v1] > ordi[v2]:
            base[v2] = v1
        else:
            base[v1] = v2
            if ordi[v1] == ordi[v2]:
                ordi[v2] += 1


# Función principal del algoritmo Kruskal

def GrafoMatrizAy_Kruskal(grafo):
    base = dict()
    ordi = dict()
    # A = {conjunto vacío}
    mst = []

    for v in grafo.vertices:
        make_set(v,base,ordi)
    # Ordena la lista G.E en forma no decendente por su peso w
    # En este caso usamos el ordenador dentro de python
    edges=[]
    for i in range(len(grafo.vertices)):
        for j in range(len(grafo.vertices)):
            if grafo.matrizAdya[i][j] !=0:
                edges.append((grafo.vertices[i],grafo.vertices[j],grafo.matrizAdya[i][j]))
    #print edges
    edges.sort(key=lambda x: x[2])

    # Para toda arista(u,v) en G.E
    for e in edges:

        u, v,weight = e
        # Si encontrar-conjunto(u) != encontrar-conjunto(v)
        if find(u,base) != find(v,base):
            # A = A union (u,v)
            union(u, v,base,ordi)
            # Union(u,v)
            mst.append(e)
    return mst


# Lista de adjacência
class GrafoListaAdy:
    def __init__(self,vert,matriz):
        self.listaAdy = {}#diccionario que representa e grafo  as chaves são os nos e os valores são a lista dos adyacentes
        lst, m = vert,matriz

        for i in range(len(lst)):#para transformar  a matriz de adyacencia para o diccionarios
            self.listaAdy[lst[i]] = []
            for j in range(len(lst)):
                if m[i][j] != 0:
                    self.listaAdy[lst[i]].append((j, m[i][j]))



    def DrawGraph(self, prim):
        l_prim = [i[:2] for i in prim]
        graph = nx.Graph()
        plt.axis('off')
        for i in self.listaAdy.keys():
            for j in self.listaAdy[i]:
                graph.add_edge(i, j[0], peso=j[1])
        pos = nx.spring_layout(graph)
        labels = nx.get_edge_attributes(graph, 'peso')
        nx.draw_networkx(graph, pos)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        nx.draw_networkx_edges(graph, pos, edgelist=l_prim, width=3, edge_color='b')

        plt.show()

    def vertadyac(self,u):
        return [i[0] for i in self.listaAdy[u]]

    def pesoarista(self,v1,v2):
        for i in self.listaAdy[v1]:
            if i[0] == v2:
                return i[1]

def GrafoListaAdy_Prim(grafo, origen):
    cola = []

    cola.append((origen, origen, 0))

    visited = [origen]

    mst = []
    while (len(cola) != 0):
        u = cola.pop(0)

        if u[1] not in visited:
            visited.append(u[1])
            mst.append(u)
        for i in grafo.listaAdy[u[1]]:#listaAdya é un diccionario, onde a llave é o vertice e o valor é a lista do vertices adyacentes a ele

            if i[0] not in visited:
                cola.append((u[1], i[0], i[1]))
        cola = sorted(cola, key=lambda e: e[2])
    print ("Prim: "+str(mst))
    return mst


def GrafoListaAdya_Dijkstra(grafo, origen):
    distancia=[float('inf')] *len(grafo.listaAdy.keys())
    visto=[False] *len(grafo.listaAdy.keys())
    padre=[None] *len(grafo.listaAdy.keys())

    distancia[grafo.listaAdy.keys().index(origen)] = 0
    list_aux = []
    list_aux.append((origen, distancia[grafo.listaAdy.keys().index(origen)]))

    while len(list_aux)!=0:
        u=list_aux.pop(0)
        visto[u[0]]=True
        ady = grafo.vertadyac(u[0])
        #print ady

        for i in range(len(ady)):
            #si distancia[v] > distancia[u] + peso (u, v) hacer
            if distancia[ady[i]]> distancia[u[0]]+ grafo.pesoarista(u[0],ady[i]):

                # distancia[v] = distancia[u] + peso (u, v)
                distancia[ady[i]] = distancia[u[0]] + grafo.pesoarista(u[0], ady[i])
                # padre[v] = u
                padre[ady[i]] = u[0]

                # adicionar(cola,(v, distancia[v])
                list_aux.append((ady[i], distancia[ady[i]]))
                list_aux.sort(key=lambda x: x[1])

    return padre, distancia


def GrafoListAdy_Floyd(grafo):
    cn = len(grafo.listaAdy.keys())

    x = [[float('inf')] * cn for i in range(cn)]
    dt = 0

    for i in grafo.listaAdy.keys():
        for j in grafo.listaAdy[i]:
            pos_i = grafo.listaAdy.keys().index(i)
            pos_j = grafo.listaAdy.keys().index(j[0])
            x[pos_i][pos_i] = 0
            x[pos_i][pos_j] = j[1]

    for k in range(cn):
        for i in range(cn):
            for j in range(cn):

                dt = x[i][k] + x[k][j]

                if (x[i][j] > dt):
                    x[i][j] = dt
    return x

# Implementación del algoritmo Kruskal

# Función principal del algoritmo Kruskal

def GrafoListaAdy_Kruskal(grafo):
    base = dict()
    ordi = dict()
    # A = {conjunto vacío}
    mst = []
    for v in grafo.listaAdy.keys():
        make_set(v,base,ordi)
    # Ordena la lista G.E en forma no decendente por su peso w
    # En este caso usamos el ordenador dentro de python
    edges=[]
    for v1,adj in grafo.listaAdy.items():
        for v2, weight in adj:
            edges.append((v1,v2, weight))

    edges.sort(key=lambda x: x[2])

    # Para toda arista(u,v) en G.E
    for e in edges:
        u, v, weight= e
        # Si encontrar-conjunto(u) != encontrar-conjunto(v)
        if find(u,base) != find(v,base):
            # A = A union (u,v)
            union(u, v,base,ordi)
            # Union(u,v)
            mst.append(e)
    return mst





# Matriz de incidência

class MatrizIncidencia:
    def __init__(self, vert, matriz):
        self.vertices, m = vert,matriz



        print("\n")

        arestas = 0
        for i in range(len(m)):#para transformar a matriz de adyacencia en matriz de incidencia
            for j in range(i, len(m)):
                arestas += 1 if m[i][j] != 0 else 0

        self.matriz_inci = np.zeros((len(vert) + 1, arestas), dtype=np.int)

        passo = 0
        for i in range(len(m)):
            for j in range(i, len(m)):
                if m[i][j] != 0:
                    self.matriz_inci[-1][passo] = m[i][j]
                    self.matriz_inci[i][passo] = 1
                    self.matriz_inci[j][passo] = 1
                    passo += 1

        print (self.matriz_inci)

    def pesoarista(self, v1, v2):
        pos_v1= self.vertices.index(v1)
        pos_v2= self.vertices.index(v2)
        #n = len(self.vertices)
        peso = 0
        for i in range(len(self.matriz_inci[0])):
            if self.matriz_inci[pos_v1][i] != 0 and self.matriz_inci[pos_v2][i] != 0:
                peso = self.matriz_inci[-1][i]
        return peso

    def vertadyac(self, v):
        ady = []
        for i in range(len(self.matriz_inci[self.vertices.index(v)])):
            if self.matriz_inci[self.vertices.index(v)][i] != 0:

                aresta_pos = i

                for j in range(len(self.vertices)):
                    if self.matriz_inci[j][aresta_pos] != 0:
                        ady.append(self.vertices[j])
        return ady



    def DrawGraph(self, prim):
        #print prim
        l_prim = [i[:2] for i in prim]
        #print l_prim
        graph = nx.Graph()
        plt.axis('off')
        cn = len(self.vertices)
        ca = len(self.matriz_inci[0])

        for i in range(ca):
            txt = ""
            # print("i: %d" %i)
            for j in range(cn):
                # print("j: %d" %j)
                if self.matriz_inci[j][i] != 0:
                    txt += str(j) + " "
            graph.add_edge(int(txt.split()[0]), int(txt.split()[1]), peso=self.matriz_inci[cn][i])

        pos = nx.spring_layout(graph)
        labels = nx.get_edge_attributes(graph, 'peso')
        nx.draw_networkx(graph, pos)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        nx.draw_networkx_edges(graph, pos, edgelist=l_prim, width=3, edge_color='b')

        plt.show()


def GrafoMatrizInci_Prim(grafo, origen):

    cola = []
    cola.append((origen, origen, 0))
    visited = [origen]
    mst = []
    while (len(cola) != 0):
        u = cola.pop(0)

        if u[1] not in visited:
            visited.append(u[1])
            mst.append(u)
        pos_v1 = grafo.vertices.index(u[1])

        for i in grafo.vertadyac(u[1]):

            if i not in visited:
                pos_v2 = grafo.vertices.index(i)
                for j in range(len(grafo.matriz_inci[0])):

                    if grafo.matriz_inci[pos_v1][j] == grafo.matriz_inci[pos_v2][j] ==1:
                        cola.append((u[1], i, grafo.matriz_inci[-1][j]))
        cola = sorted(cola, key=lambda e: e[2])
    print ("Prim: "+str(mst))
    return mst


def GrafoMatrizInci_Dijkstra(grafo, origen):
    distancia = [float('inf')] * len(grafo.vertices)
    visto = [False] * len(grafo.vertices)
    padre = [None] * len(grafo.vertices)

    distancia[grafo.vertices.index(origen)] = 0
    list_aux = []
    list_aux.append((origen, distancia[grafo.vertices.index(origen)]))

    while len(list_aux) != 0:
        u = list_aux.pop(0)
        visto[u[0]] = True
        ady = grafo.vertadyac(u[0])
        for i in range(len(ady)):
            # si distancia[v] > distancia[u] + peso (u, v) hacer
            if distancia[ady[i]] > distancia[u[0]] + grafo.pesoarista(u[0], ady[i]):
                # distancia[v] = distancia[u] + peso (u, v)
                distancia[ady[i]] = distancia[u[0]] + grafo.pesoarista(u[0], ady[i])
                # padre[v] = u
                padre[ady[i]] = u[0]

                # adicionar(cola,(v, distancia[v])
                list_aux.append((ady[i], distancia[ady[i]]))
                list_aux.sort(key=lambda x: x[1])
    return padre, distancia


def GrafoMatrizInci_Floyd(grafo):
    cn = len(grafo.vertices)
    x = [[float('inf')] * cn for i in range(cn)]
    ca = len(grafo.matriz_inci[0])

    dt = 0

    for i in range(ca):
        txt = ""

        for j in range(cn):

            if grafo.matriz_inci[j][i] != 0:
                txt += str(j) + " "

            x[j][j] = 0

        x[int(txt.split()[0])][int(txt.split()[1])] = grafo.matriz_inci[cn][i]
        x[int(txt.split()[1])][int(txt.split()[0])] = grafo.matriz_inci[cn][i]

    for k in range(cn):
        for i in range(cn):
            for j in range(cn):

                dt = x[i][k] + x[k][j]

                if (x[i][j] > dt):
                    x[i][j] = dt
    return x

# Implementación del algoritmo Kruskal

# Función principal del algoritmo Kruskal

def GrafoMatrizInci_Kruskal(grafo):
    base = dict()
    ordi = dict()
    # A = {conjunto vacío}
    mst = []
    for v in grafo.vertices:
        make_set(v,base,ordi)
    # Ordena la lista G.E en forma no decendente por su peso w
    # En este caso usamos el ordenador dentro de python
    edges=[]
    for i in range(len(grafo.matriz_inci[0])):
        txt=''
        for j in range(len(grafo.vertices)):
            if grafo.matriz_inci[j][i] == 1:
                 txt += str(grafo.vertices[j]) + ' '

        edges.append((int(txt.split()[0]),int(txt.split()[1]),grafo.matriz_inci[-1][i]))
    edges.sort(key=lambda x: x[2])

    # Para toda arista(u,v) en G.E
    for e in edges:
        u, v,weight = e
        # Si encontrar-conjunto(u) != encontrar-conjunto(v)
        if find(u,base) != find(v,base):
            # A = A union (u,v)
            union(u, v,base,ordi)
            # Union(u,v)
            mst.append(e)
    return mst

if __name__ == '__main__':
    vert=int(input('Insere a quantidade de vertices '))
    ar = int(input('Insere a quantidade de arestas '))

    vert, matriz = GenGrafo(vert,ar)
    edges =0
    for i in range(len(vert)):
        for j in range(i,len(vert)):
            edges+= 1 if matriz[i][j] != 0 else 0
    print "Numero de Arestas: "+str(edges)

    grafo=GrafoMatrizAdya(vert,matriz)
   # grafo.printMatrix()
    print grafo.vertices
    p_ini_time = time()
    prim=GrafoMatrizAy_Prim(grafo,1)
    print("Tempo do Prim: %.4f \n" % (time()-p_ini_time))
    time_ini_floyd = time()
    floyd = GrafoMatrizAy_Floyd(grafo)
    print("Tempo do Floyd: %.4f \n" % (time()-time_ini_floyd))
    for i in floyd:
        print i
    time_ini_djk=time()
    p,d = GrafoMatrizAy_Dijkstra(grafo, 2)
    print("Tempo do Dijkstra: %.4f \n" % (time()-time_ini_djk))
    print "distancia: "+str(d)
    print "padre: "+str(p)
    time_ini_k=time()
    mst = GrafoMatrizAy_Kruskal(grafo)
    print("Tempo do Kruskal: %.4f \n" % (time()-time_ini_k))
    print "kruskal: "+str(mst)
    #grafo.DrawGraph(prim)

    print "*************************************************"
    grafo_lst = GrafoListaAdy(vert,matriz)
    print grafo_lst.listaAdy
    p_ini_time = time()
    prim = GrafoListaAdy_Prim(grafo_lst,1)
    print("Tempo do Prim: %.4f \n"%(time()-p_ini_time))
    time_ini_floyd = time()
    f = GrafoListAdy_Floyd(grafo_lst)
    print("Tempo do Floyd: %.4f \n" % (time()-time_ini_floyd))
    for i in f:
        print i
    time_ini_djk = time()
    p,d =GrafoListaAdya_Dijkstra(grafo_lst, 2)
    print("Tempo do Dijkstra: %.4f \n" % (time()-time_ini_djk))
    print "distancia: "+str(d)
    print "padre: "+str(p)
    time_ini_k =time()
    mst = GrafoListaAdy_Kruskal(grafo_lst)
    print("Tempo do Kruskal: %.4f \n" % (time()-time_ini_k))
    print "kruskal: "+str(mst)
    #grafo_lst.DrawGraph(prim)

    print "**************************************************"
    grafo_inci = MatrizIncidencia(vert,matriz)
    p_ini_time = time()
    prim = GrafoMatrizInci_Prim(grafo_inci,1)
    print("Tempo do Prim: %.4f \n"%(time()-p_ini_time))
    time_ini_floyd=time()
    f =GrafoMatrizInci_Floyd(grafo_inci)
    print("Tempo do Floyd: %.4f \n" % (time()-time_ini_floyd))
    for i in f:
        print i
    time_ini_djk=time()
    p,d =GrafoMatrizInci_Dijkstra(grafo_inci, 2)
    print("Tempo do Dijkstra: %.4f \n" % (time()-time_ini_djk))
    print "distancia: "+str(d)
    time_ini_k = time()
    print "padre: "+str(p)
    mst = GrafoMatrizInci_Kruskal(grafo_inci)
    print("Tempo do Kruskal: %.4f \n" % (time()-time_ini_k))
    print "kruskal: "+str(mst)
    if graphic:
        grafo_inci.DrawGraph(mst)
