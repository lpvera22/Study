# *-* encoding:UTF-8 *-*

def change_coins(amount,total,den):
    # amount: value of the buying
    # total: total of money that the client pay
    #den: denominations of the coins in this case 1,5,10 and 25


    n=total-amount
    if n>0:
        den.sort(reverse=True)
        change = {}  # change: dictionary for the result
        for i in den:
            change[i] = 0
        j=0
        while(n!=0 and j<=len(den)):
            if n>=den[j]:
                change[j]+=1
                n=n-den[j]

            else:
                j+=1
        return change
    else:
        return 0







if __name__=='__main__':

    amount=input('amount')
    total=input('total')
    den=[1,5,10,25]


    print(change_coins(amount,total,den))
