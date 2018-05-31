# *-* encoding:UTF-8 *-*
class punto:
    def __init__(self, x, y):
        self.y=y
        self.x=x
    def __str__(self):
        return (self.x,self.y)
def puntos_mismo_lado_recta(lista,n):
    '''ax+by+c= 0 onde a = (y2–y1) b= (x1–x2) e c=–(x1y2–y1x2)'''

    if n==1:
        a=0-lista[0].y
        b=0
        c=-(lista[0].x*0-lista[0].y*lista[0].x)
        print('%dx+%dy+%d'%(a,b,c))
    else:
        min=lista[0]
        for i in range(1,n):
            if lista[i].x<min.x:
                min=lista[i]
        a = 0 - min.y
        b = 0
        c = -(min.x * 0 - min.y * min.x)
        print('%dx+%dy+%d' % (a, b, c))
#inc b
def puntos_mismo_lado_recta_casco(lista,n,listacasco):
    if n==1:
        a=0-lista[0].y
        b=0
        c=-(lista[0].x*0-lista[0].y*lista[0].x)
        print('%dx+%dy+%d'%(a,b,c))
    else:

        min1=listacasco[0]
        min2 = min(listacasco[1], listacasco[len(listacasco) - 1], key=lambda p: p.x)

        for i in range(1,len(listacasco)):
            if listacasco[i].x<min1.x:
                min1=listacasco[i]

                if i==len(listacasco)-1:
                    min2=min(listacasco[len(listacasco)-2],listacasco[0],key=lambda p:p.x)
                else:
                    min2=min(listacasco[i-1],listacasco[i+1],key=lambda p:p.x)

        '''ax+by+c= 0 onde a = (y2–y1) b= (x1–x2) e c=–(x1y2–y1x2)'''
        a = min2.y-min1.y
        b = min1.x-min2.x
        c = -(min1.x * min2.y - min1.y * min2.x)
        print('%dx+%dy+%d' % (a, b, c))








if __name__=="__main__":
    n = int(input('n'))
    m = []
    casco=[]
    for i in range(n):
        sec = raw_input('coordenadas').split()
        #S = [int(i) for i in sec]
        tmp=punto(int(sec[0]),int(sec[1]))

        m.append(tmp)
    flag=True
    while flag:
        try:
            txt = raw_input('casco').split()

            #S = [int(i) for i in sec]
            tmp=punto(int(txt[0]),int(txt[1]))

            casco.append(tmp)
        except Exception as e:
           # print(e)
            flag=False

   # print(casco)
    puntos_mismo_lado_recta_casco(m,n,casco)

