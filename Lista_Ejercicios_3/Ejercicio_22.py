# *-* encoding:UTF-8 *-*
class punto:
    def __init__(self, x, y):
        self.y=y
        self.x=x
class poly:
    def __init__(self,vert):
        self.vert=[]
        for i in vert:
            tmp=punto(i[0],i[1])
            self.vert.append(tmp)
    def isConvex(self):
        if len(self.vert)<3:
            return False
        sign=False
        n=len(self.vert)
        for i in range(n):
            dx1=self.vert[(i+2)%n].x-self.vert[(i+1)%n].x
            dy1 = self.vert[(i + 2) % n].y - self.vert[(i + 1) % n].y
            dx2 = self.vert[i].x - self.vert[(i + 1) % n].x
            dy2 = self.vert[i].y - self.vert[(i + 1) % n].y
            zcrossproduct = dx1 * dy2 - dy1 * dx2

            if (i == 0):
                sign = zcrossproduct > 0
            elif sign != (zcrossproduct > 0):
                return False
        return True



if __name__=="__main__":
    n = int(input('n'))
    m = []
    for i in range(n):
        sec = raw_input('coordenadas').split()
        #S = [int(i) for i in sec]
        m.append((int(sec[0]),int(sec[1])))
    print(m)
    pol=poly(m)
   # x = int(input('x'))
    print(pol.isConvex())


