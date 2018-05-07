#*-* encoding:UTF-8 *-*
import numpy as np
from random import *

#Matriz de adjacência
class GrafoMatrizAdya:
    def __init__(self,vert,aristas):
        self.vertices,self.matrizAdya=self.GenGrafo(vert,aristas)


    def printMatrix(self):
        for i in range(len(self.matrizAdya)):
            for j in range(len(self.matrizAdya)):
                print("%i" % self.matrizAdya[i][j]),
            print


#Metodo generar grafo randomico
    def GenGrafo(self,vert, edges, min_weight=1, max_weight=100):
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

            # end = start = randint(0, vert - 1)
            # while end == start:
            #     end = randint(0, vert - 1)

            return (open_list, matriz)

    #1) Árvore geradora mínima:
    #a. Algoritmo de Prim


def GrafoMatrizAy_Prim(grafo,origen):
    num_vert = len(grafo.vertices)
    cola=[]

    pos = grafo.vertices.index(origen)
    cola.append((pos,pos,0))
    visited = [grafo.vertices[pos]]
    mst=[]
    while (len(cola) != 0):
        print(cola)
        u = cola.pop(0)
        if grafo.vertices[u[1]] not in visited:
            visited.append(grafo.vertices[u[1]])
            mst.append(u)
        for i in range(len(grafo.vertices)):
            if grafo.matrizAdya[u[1]][i]!=0 and grafo.vertices[i] not in visited :
                cola.append((u[1],i,grafo.matrizAdya[u[1]][i]))
        cola = sorted(cola, key=lambda e: e[2])
    print mst


#Lista de adjacência
class GrafoListaAdy:
    def __init__(self,vert,edges):
        self.listaAdy = {}
        lst,m=self.GenGrafo(vert,edges)
        for i in range(len(lst)):
            self.listaAdy[lst[i]]=[]
            for j in range(len(lst)):
                if m[i][j]!=0:
                    self.listaAdy[lst[i]].append((j,m[i][j]))

    def GenGrafo(self,vert, edges, min_weight=1, max_weight=100):
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

def GrafoListaAdy_Prim(grafo, origen):
    print grafo.listaAdy
    num_vert = len(grafo.listaAdy.keys())
    cola = []

    cola.append((origen,origen,0))

    print cola

    visited = [origen]
    print visited
    mst = []
    while (len(cola) != 0):
        u = cola.pop(0)
        print u
        if u[1] not in visited:
            visited.append(u[1])
            mst.append(u)
        for i in grafo.listaAdy[u[1]]:
            #print i
            if i[0] not in visited:
                cola.append((u[1], i[0], i[1]))
        cola = sorted(cola, key=lambda e: e[2])
    print mst

#Matriz de incidência
#class MatrizIncidencia:




if __name__=='__main__':
    vert=int(input('Insere a quantidade de vertices'))
    ar = int(input('Insere a quantidade de arestas'))
   # grafo=GrafoMatrizAdya(vert,ar)
    #grafo.printMatrix()
    #print grafo.vertices
    #prim=GrafoMatrizAy_Prim(grafo,1)


    grafo_lst = GrafoListaAdy(vert,ar)
    GrafoListaAdy_Prim(grafo_lst,1)






