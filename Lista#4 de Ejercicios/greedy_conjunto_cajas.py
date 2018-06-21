# *-* encoding:UTF-8 *-*
def subconjunto_cajas(p,K,c,n):
    #p, weight of each box in this case is the same for all of them
    #K, maxim weight that the subset is going to have
    #c, list of the cost of each box
    #n, number of boxes
    peso_max=K
    B=[0]*n# list that's is going to have the result (the boxes with the value of 1)
    '''taking in acount that in this case the optmimal selection es to in each step take the box 
     with major cost, because we need to maximize the cost, so that's why I sort the list of costs (c) first'''
    c.sort(reverse=True)
    i=0

    while (i<=n and p<=peso_max):
        B[i]=1
        peso_max=peso_max-p
        i+=1
    return B
if __name__=='__main__':

    p=5
    K=10
    c=[1,2,5,7,0,10]
    n=6


    print(subconjunto_cajas(p,K,c,n))





