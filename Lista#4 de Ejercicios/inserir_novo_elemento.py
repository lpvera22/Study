# *-* encoding:UTF-8 *-*
def insercion (sec,r,l,x):
    if len(sec)>0:
        if l-r==1:
            if x<sec[l]:
                sec.insert(l,x)
            else:
                sec.insert(l+1, x)
        else:
            med=(l+r)/2
            if x<sec[med+1]:
                insercion(sec,r,med,x)
            else:
                insercion(sec, med + 1,l ,x)
        return sec


    else:
        return sec





if __name__=='__main__':
    sec=[1,4,5,5]
    x=3
    print(insercion(sec,0,3,x))