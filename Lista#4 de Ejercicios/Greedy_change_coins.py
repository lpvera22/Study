# *-* encoding:UTF-8 *-*

def Greedy_change_coins(amount,total,den):
    # amount: value of the buying
    # total: total of money that the client pay
    #den: denominations of the coins in this case 1,5,10 and 25

    change = {}  # instead of a list the function is going to return a dictionary having as keys the denominations
    amount_to_change = total-amount

    if total-amount>0: #in case there is some change to return

        den.sort(reverse=True)#just making sure that are sorted in decreasing order
        for i in den:
            change[i]=0

        if amount_to_change>25:
            change[25]+=1
            amount_to_change=amount_to_change-25
            Greedy_change_coins(amount,total-25,den)
        elif amount_to_change>10:
            change[10] += 1
            amount_to_change = amount_to_change - 10
            Greedy_change_coins(amount, total - 10,den)
        elif amount_to_change>5:
            change[5] += 1
            amount_to_change = amount_to_change - 5
            Greedy_change_coins(amount, total - 5,den)
        else:
            change[1] += 1
            amount_to_change = amount_to_change - 1
            Greedy_change_coins(amount, total - 1,den)

    else:
        return change

if __name__ == '__main__':

    amount=int(input('amount'))
    total = int(input('total'))
    den=[1,5,10,25]

    print(Greedy_change_coins(amount,total,den))









