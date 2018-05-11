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
    def vertadyac(self,v1):
        ady=[]
        for i in range(len(self.vertices)):
            if self.matrizAdya[self.vertices.index(v1)][i]!=0:
                ady.append(self.matrizAdya[self.vertices.index(v1)][i])
        return ady





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

    def DrawGraph(self,prim):
        l_prim=[i[:2] for i in prim]
        graph = nx.Graph()
        plt.axis('off')
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if(self.matrizAdya[i][j] != 0):
                    graph.add_edge(self.vertices[i],self.vertices[j],peso=self.matrizAdya[i][j])
        pos=nx.spring_layout(graph)
        labels = nx.get_edge_attributes(graph,'peso') 
        nx.draw_networkx(graph,pos)
        nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
        nx.draw_networkx_edges(graph,pos,edgelist=l_prim,width=3,edge_color='b')

        plt.show()

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

'''2) Os caminhos mais curtos a partir de um vértice v até todos os outros vértices : 
          a.Algoritmo de Dijkstra'''


def GrafoMatrizAy_Dijkstra(grafo,origen):
    distancia=[float('inf')] *len(grafo.vertices)
    visto=[False] *len(grafo.vertices)
    padre=[None] *len(grafo.vertices)

    distancia[grafo.vertices.index(origen)]=0
    list_aux=[]
    list_aux.append((origen,distancia[grafo.vertices.index(origen)]))

    while len(list_aux)!=0:
        u=list_aux.pop(0)
        visto[u[0]]=True
        ady=grafo.vertadyac(u)
        for i in range(len(ady)):
            #si distancia[v] > distancia[u] + peso (u, v) hacer
            if distancia[ady[i]]> distancia[u]+ grafo.pesoarista(u,ady[i]):

                #distancia[v] = distancia[u] + peso (u, v)
                distancia[ady[i]]=distancia[u]+ grafo.pesoarista(u,ady[i])
                #padre[v] = u
                padre[ady[i]]=u

                #adicionar(cola,(v, distancia[v])
                list_aux.append((ady[i],distancia[ady[i]]))
                list_aux.sort(key=lambda x: x[1])
    return padre,distancia








#3)O caminho mais curto entre todos os pares de vértices :
#a.Algoritmo de Floyd

def GrafoMatrizAy_Floyd(grafo):
    cn=len(grafo.vertices)
    x = [[float('inf')]*cn for i in range(cn)]
    for i in range(cn):
        for j in range(cn):
            if i == j:
                x[i][j] = 0
            elif grafo.matrizAdya[i][j] != 0:
                x[i][j] = grafo.matrizAdya[i][j]
    dt=0
    for k in range(cn):
        for i in range(cn):
            for j in range(cn):
                #print ("k: %d, i: %d , j: %d" %(k,i,j))
                #print x[i][k]
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

    def DrawGraph(self,prim):
        l_prim=[i[:2] for i in prim]
        graph = nx.Graph()
        plt.axis('off')
        for i in self.listaAdy.keys():
            for j in self.listaAdy[i]:
                graph.add_edge(i,j[0],peso=j[1])
        pos=nx.spring_layout(graph)
        labels = nx.get_edge_attributes(graph,'peso') 
        nx.draw_networkx(graph,pos)
        nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
        nx.draw_networkx_edges(graph,pos,edgelist=l_prim,width=3,edge_color='b')

        plt.show()

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
    print grafo.listaAdy
    x = [[float('inf')]*cn for i in range(cn)]
    dt=0

    for i in grafo.listaAdy.keys():
        for j in grafo.listaAdy[i]:
            pos_i = grafo.listaAdy.keys().index(i)
            pos_j = grafo.listaAdy.keys().index(j[0])
            x[pos_i][pos_i] = 0
            x[pos_i][pos_j] = j[1]
    print x
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

    def DrawGraph(self,prim):
        l_prim=[i[:2] for i in prim]
        graph = nx.Graph()
        plt.axis('off')
        cn=len(self.vertices)
        ca=len(self.matriz_inci[0])

        for i in range(ca):
            txt =""
        #print("i: %d" %i)
            for j in range(cn):
                #print("j: %d" %j)
                if self.matriz_inci[j][i]!=0:
                   txt+=str(j)+" "
            graph.add_edge(txt.split()[0],txt.split()[1],peso=self.matriz_inci[cn][i])

        pos=nx.spring_layout(graph)
        labels = nx.get_edge_attributes(graph,'peso') 
        nx.draw_networkx(graph,pos)
        nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
        nx.draw_networkx_edges(graph,pos,edgelist=l_prim,width=3,edge_color='b')

        plt.show()

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
        mst.append((txt.split()[0],txt.split()[1],l_s[count]))
        count+=1
    print mst
    return mst
         
def GrafoMatrizInci_Floyd(grafo):
    cn=len(grafo.vertices)
    x = [[float('inf')]*cn for i in range(cn)]	
    ca=len(grafo.matriz_inci[0])
    
    dt=0
    
    for i in range(ca):
        txt =""
        #print("i: %d" %i)
        for j in range(cn):
            #print("j: %d" %j)
            if grafo.matriz_inci[j][i]!=0:
               txt+=str(j)+" "
               #print ("valor: %d" % grafo.matriz_inci[j][i])
        #print "----"
            x[j][j]=0
        #print txt
        #print grafo.matriz_inci[cn]
        x[int(txt.split()[0])][int(txt.split()[1])] = grafo.matriz_inci[cn][i]	
        x[int(txt.split()[1])][int(txt.split()[0])] = grafo.matriz_inci[cn][i] 

    for k in range(cn):
        for i in range(cn):
            for j in range(cn):
                #int dt = path[i][k] + path[k][j]
                dt=x[i][k]+x[k][j]
                
                if(x[i][j] > dt):
                    x[i][j] = dt
    return x




if __name__=='__main__':
    vert=int(input('Insere a quantidade de vertices '))
    ar = int(input('Insere a quantidade de arestas '))
    #grafo=GrafoMatrizAdya(vert,ar)
    #grafo.printMatrix()
    #print grafo.vertices
    #prim=GrafoMatrizAy_Prim(grafo,1)
    #grafo.DrawGraph(prim)

    #print "*************************************************"
    #grafo_lst = GrafoListaAdy(vert,ar)
    #prim = GrafoListaAdy_Prim(grafo_lst,1)
    #f = GrafoListAdy_Floyd(grafo_lst)
    #grafo_lst.DrawGraph(prim)

    print "**************************************************"
    grafo_inci = MatrizIncidencia(vert,ar)
    prim = GrafoMatrizInci_Prim(grafo_inci,1)
    f =GrafoMatrizInci_Floyd(grafo_inci)
    for i in f:
        print i
    grafo_inci.DrawGraph(prim)




