# *-* encoding:UTF-8 *-*
def comprobar_secuencia_ordenada(secuencia,l,r):

    if len(secuencia)!=0:
        if r-l==0 :
            return secuencia[l:r]
        elif r-l==1:
            if secuencia[l]>secuencia[r]:
                return False
            else:
                return secuencia[l:r]
        else:

            while (l<=r):
                if (secuencia[l]>secuencia[l+1]):
                    return False
                else:
                    l=l+1
            return True


    else:
        return 0

if __name__=='__main__':
    secuencia=[1,2,3,4,10,6]
    n=6
    l=0
    r=5
    print(comprobar_secuencia_ordenada(secuencia,l,r))