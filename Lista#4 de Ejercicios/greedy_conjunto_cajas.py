# *-* encoding:UTF-8 *-*
def subconjunto_cajas(p,K,c,n):
    #p, weight of each box in this case is the same for all of them
    #K, maxim weight that the subset is going to have
    #c, diccionary of the cost of each box
    #n, number of boxes
    peso_max=K
    #taking in acount that in this case the optmimal selection es to in each step take the box
    # with major cost, because we need to maximize the cost, so that's why I sort dictionary
    costo=sorted(c,key=c.get,reverse=True)

    i=0
    aux=[]
    while (i<=n and p<=peso_max):
        aux.append((costo[i],c[i]))

        peso_max=peso_max-p
        i+=1
    return aux
if __name__=='__main__':
    n = 5
    p=2
    K=5
    c={}
    c1=[50,40,50,10,40]
    for i in range(n):
        c[i]=c1[i]






    print(subconjunto_cajas(p,K,c,n))





