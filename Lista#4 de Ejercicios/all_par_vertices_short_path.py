# *-* encoding:UTF-8 *-*
def all_pairs_shortest_path(costo,n):
    #costo, adjacency matrix of the graph
    #n, amount of vertex

    camino_vi_vj= [[None]*n for i in range(n)]# matrix that it's going to return the paths
    for i in range(n):
        for j in range(n):
            if costo[i][j]!=float('inf'):
                camino_vi_vj[i][j]=i

    for m in range(n):
        for x in range(n):
            for y in range(n):
                if costo[x][m]+costo[m][y]<costo[x][y]:
                    costo[x][y]=costo[x][m]+costo[m][y]
                    camino_vi_vj[x][y]=m
    return camino_vi_vj
if __name__=='__main__':

    n=5


    cost=[[0,float('inf'),2,1,float('inf')],[float('inf'),0,float('inf'),float('inf'),2],[float('inf'),1,0,float('inf'),1],[float('inf'),3,float('inf'),0,float('inf')],[float('inf'),float('inf'),float('inf'),float('inf'),0]]


    x=all_pairs_shortest_path(cost,n)

    for i in x:
        for j in i:
            print j,
        print ('\n')