# *-* encoding:UTF-8 *-*

def change_coins(amount,total,den):
    # amount: value of the buying
    # total: total of money that the client pay
    #den: denominations of the coins in this case 1,5,10 and 25


    F=[]# list for returning the result
    F.append(0)
    n=total-amount
    aux=[]
    change={}
    for i in range(1,n+1):
        temp=float('inf')
        j=1
        while j<=len(den)-1 and i>=den[j]:
            temp=min(F[i-den[j]],temp)

            j+=1
        aux.append(den[j-1])


        F.insert(i,temp+1)

    if aux[n-1]*F[n]==n:
        change[aux[n-1]]=F[n]
    while (aux[n-1]*F[n]!=n or n!=0):
        if aux[n-1]*F[n]<n or aux[n-1]*F[n]>n :
            change[aux[n - 1]] = F[n]
            n=n-1






    return F,aux, change

if __name__=='__main__':

    amount=input('amount')
    total=input('total')
    den=[0,1,5,10,25]

    print change_coins(amount,total,den)
