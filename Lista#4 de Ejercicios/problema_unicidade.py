# *-* encoding:UTF-8 *-*
def problema_unicidade(sec,n):
    if n>0:
        sec.sort() # com o objetivo que os numeros iguais fiquem juntos
        for i in range(n-1):

            if sec[i]==sec[i+1]:
                return False
        return True
    else:
        return True
def insercion (sec,l,r,x):
    if n>0:
        if l-r==1:
            if x<sec[l]:
                sec.insert()
    else:
        return sec[0]
if __name__=='__main__':
    sec=[1,2,5,5]
    n=4
    print(problema_unicidade(sec,n))