# *-* encoding:UTF-8 *-*
def punto_encima(l1,l2,p1):

    d=(l2[1]-l1[1])*p1[0]+(l1[0]-l2[0])*p1[1]+(l2[0]*l1[1]-l2[1]*l1[0])
    if d<=0:
        return True
    else:
        return False


def Simple_Polygon(points):
    if len(points)==1:
        return points[0]
    else:
        points.sort(key=lambda p:p[0])
        polygon=[]
        stack=[]
        for i in points:
            if punto_encima(points[0],points[-1],i):
                polygon.append(i)
            else:
                stack.append(i)

        while(len(stack)!=0):
            polygon.append(stack.pop())
        return polygon


#print(punto_encima((1,1),(2,3),(3,1)))
points=[(1,1),(2,3),(1,2),(3,1),(3,3)]
print(Simple_Polygon(points))