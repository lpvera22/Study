#*-* encoding:UTF-8 *-*
import numpy as np
from random import *
import networkx as nx
import matplotlib.pyplot as plt

#Matriz de adjacência
class GrafoMatrizAdya:
    def __init__(self,vert,aristas):
        self.vertices,self.matrizAdya=self.GenGrafo(vert,aristas)


    def printMatrix(self):
        for i in range(len(self.matrizAdya)):
            for j in range(len(self.matrizAdya)):
                print("%i" % self.matrizAdya[i][j]),
            print
    def pesoarista(self,v1,v2):
        return self.matrizAdya[v1][v2]


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
        #print(cola)
        u = cola.pop(0)
        if grafo.vertices[u[1]] not in visited:
            visited.append(grafo.vertices[u[1]])
            mst.append(u)
        for i in range(len(grafo.vertices)):
            if grafo.matrizAdya[u[1]][i]!=0 and grafo.vertices[i] not in visited :
                cola.append((u[1],i,grafo.matrizAdya[u[1]][i]))
        cola = sorted(cola, key=lambda e: e[2])
    print mst
    return mst
#3)O caminho mais curto entre todos os pares de vértices :
#a.Algoritmo de Floyd

def GrafoMatrizAy_Floyd(grafo):

    x=grafo.matrizAdya.copy()
    cn=len(grafo.vertices)
    dt=0
    for i in range(cn):
        x[i][i] = 0
    for k in range(cn):
        for i in range(cn):
            for j in range(cn):
                dt = x[i][k] + x[k][j]
                if (x[i][j] > dt):
                    x[i][j] = dt
    return x


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
        if edges > vert * (vert-1) // 2:
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
    #print grafo.listaAdy
    num_vert = len(grafo.listaAdy.keys())
    cola = []

    cola.append((origen,origen,0))

    #print cola

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
    return mst
#3)O caminho mais curto entre todos os pares de vértices :
#a.Algoritmo de Floyd

def GrafoListAdy_Floyd(grafo):
    cn=len(grafo.listaAdy.keys())
    x=grafo.listaAdy.copy()
    dt=0

    for i in range(cn):
        for j in range(len(x[i].value())):
            if x[i].value()==x[j]:
                x[j]=0
    for k in range(cn):
        for i in range(cn):
            for j in range(cn):
                #int dt = path[i][k] + path[k][j]
                dt=x[i][k]+x[k][j]
                if(x[i][j] > dt):
                    x[i][j] = dt
    return x





#Matriz de incidência
class MatrizIncidencia:
    def __init__(self, vert,edges):
        self.vertices,m=self.GenGrafo(vert,edges)
        for i in m:
            for j in i:
                print j,
            print
		
        print
        
        arestas = 0
        for i in range(len(m)):
            for j in range(i,len(m)):
                arestas += 1 if m[i][j] !=0 else 0
        
        self.matriz_inci = np.zeros((vert+1, arestas),dtype=np.int)
        
        passo = 0
        for i in range(len(m)):
            for j in range(i,len(m)):
                if m[i][j] !=0:
                    self.matriz_inci[-1][passo]=m[i][j]
                    self.matriz_inci[i][passo]=1
                    self.matriz_inci[j][passo]=1
                    passo +=1  
                       
        print self.matriz_inci
    def pesoarista(self,v1,v2):
        n=len(self.vertices)
        peso=0
        for i in range(len(self.m)):
            if self.matriz_inci[i][v1]!=0 and self.matriz_inci[i][v2]!=0:
                peso=self.matriz_inci[i][n+1]
        return peso
    
    def GenGrafo(self,vert, edges, min_weight=1, max_weight=100):
        if edges > ((vert-1) * (vert )) // 2:
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

def GrafoMatrizInci_Prim(grafo, origen):
    non_visited=grafo.vertices[:]

    l=list(grafo.matriz_inci[-1])
    l_s=sorted(list(grafo.matriz_inci[-1]))
    count =0
    mst=[]
    while len(non_visited)!= 0:
        pos = l.index(l_s[count])
        txt=''
        for i in range(len(grafo.vertices)):
            if grafo.matriz_inci[i][pos] == 1:
                if grafo.vertices[i] in non_visited:
                    non_visited.remove(grafo.vertices[i])
                txt+=str(grafo.vertices[i])+' '
                #else:
                 #   txt+=str(grafo.vertices[i])+' '
        print txt
        mst.append((txt.split()[0],txt.split()[1],l_s[count]))
        count+=1
    print mst
    return mst
         
def DrawGraph(grafo,prim):
    l_prim=[i[:2] for i in prim]
    graph = nx.Graph()
    plt.axis('off')
    #graph.add_nodes_from(grafo.vertices)
    for i in range(len(grafo.vertices)):
        for j in range(len(grafo.vertices)):
            if(grafo.matrizAdya[i][j] != 0):
                graph.add_edge(grafo.vertices[i],grafo.vertices[j],peso=grafo.matrizAdya[i][j])
                #pass
    pos=nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph,'peso') 
    nx.draw_networkx(graph,pos)
    nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
    nx.draw_networkx_edges(graph,pos,edgelist=l_prim,width=3,edge_color='b')

    plt.show()

def GrafoMatrizInci_Floyd(grafo):

    cn=len(grafo.vertices)
    ca=len(grafo.m)
    x=[[]]
    dt=0
    for i in range(ca):
        for j in range(cn):
            if grafo.matriz_inci[i][j]!=0:
                cont=cont+1
        if cont==1:
            x[i][i]=0
    for k in range(cn):
        for i in range(cn):
            for j in range(ca):
                dt=grafo.pesoarista(grafo.vertices[i],grafo.vertices[k])+grafo.pesoarista(grafo.vertices[k],grafo.vertices[j])
                if grafo.pesoarista(grafo.vertices[i],grafo.vertices[j])>dt:
                    grafo.pesoarista(grafo.vertices[i],grafo.vertices[j]) =dt














if __name__=='__main__':
    vert=int(input('Insere a quantidade de vertices '))
    ar = int(input('Insere a quantidade de arestas '))
    grafo=GrafoMatrizAdya(vert,ar)
    grafo.printMatrix()
    print grafo.vertices
    prim=GrafoMatrizAy_Prim(grafo,1)
    DrawGraph(grafo,prim)


    #grafo_lst = GrafoListaAdy(vert,ar)
    #GrafoListaAdy_Prim(grafo_lst,1)

    #grafo_inci = MatrizIncidencia(vert,ar)
    #GrafoMatrizInci_Prim(grafo_inci,1)




