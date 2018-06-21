# *-* encoding:UTF-8 *-*
def subconjunto_cajas(p,K,c,n):
    #p, weight of each box in this case is the same for all of them
    #K, maxim weight that the subset is going to have
    #c, diccionary of the cost of each box
    #n, number of boxes
    peso_max=K

    #taking in acount that in this case the optmimal selection es to in each step take the box
    # with major cost, because we need to maximize the cost, so that's why I sort the list of costs (c) first
    costo=sorted(c,reverse=True)
    i=0
    for i in costo:
        B[i]=0 # list that's is going to have the result (the boxes with the value of 1)
    while (i<=n and p<=peso_max):
        B[i]=1
        peso_max=peso_max-p
        i+=1
    return B
if __name__=='__main__':
    n = 5
    p=50
    K=100
    c={}
    c1=[50,40,50,10,40]
    for i in range(n):
        c[i]=c1[i]






    print(subconjunto_cajas(p,K,c,n))





