# *-* encoding:UTF-8 *-*
def Shortest_path(v,cost,n,f):
    #v initial vertex
    #cost, is the matrix that contains the costs between all the edges
    #n list with the vertexs
    #f is the vertex that I want to reach (final vertex)
    S=[False]*n
    d=[float('inf')]*n#list to return the distance between v and
    P=[-1]*n
    for i in range(n):
        d[i]=cost[v][i]

    S[v]=True


    while S[f]==False:
        u=Minor_d_nao_S(S,d)
        S[u]=True
        if u!=f:

            w=List_Ady_u_S_False(u,S,cost,n)
            for i in w:
                if d[i]>d[u]+cost[u][i]:
                    d[i]=d[u]+cost[u][i]
                    P[i]=u
    camino=[]
    camino.append(f)
    while P[f]!=v and P[f]!= -1:
        camino.insert(0,P[f])
        f=P[f]
    camino.insert(0,v)
    return camino


def Minor_d_nao_S(S,d):

    aux=[]
    for i in range(n):
        if S[i]==False:
            aux.append((i,d[i]))
    aux.sort(key=lambda l:l[1])
    return aux[0][0]
def List_Ady_u_S_False(u,S,cost,n):
    aux=[]
    for i in range(n):
        if cost[u][i] !=float('inf') and cost[u][i] !=0:
            if S[i]==False:
                aux.append(i)
    return aux


if __name__=='__main__':

    n=5
    v=0
    f=2
    cost=[[0,float('inf'),2,1,float('inf')],[float('inf'),0,float('inf'),float('inf'),2],[float('inf'),1,0,float('inf'),1],[float('inf'),3,float('inf'),0,float('inf')],[float('inf'),float('inf'),float('inf'),float('inf'),0]]



    print(Shortest_path(v,cost,n,f))






