# *-* encoding:UTF-8 *-*
def all_pairs_shortest_path(costo,n):
    #costo, adjacency matrix of the graph
    #n, amount of vertexs

    for m in range(n):
        for x in range(n):
            for y in range(n):
                if costo[x][m]+costo[m][y]<costo[x][y]:
                    costo[x][y]=costo[x][m]+costo[m][y]
    return costo
if __name__=='__main__':

    n=5


    cost=[[0,float('inf'),2,1,float('inf')],[float('inf'),0,float('inf'),float('inf'),2],[float('inf'),1,0,float('inf'),1],[float('inf'),3,float('inf'),0,float('inf')],[float('inf'),float('inf'),float('inf'),float('inf'),0]]


    print(all_pairs_shortest_path(cost,n))