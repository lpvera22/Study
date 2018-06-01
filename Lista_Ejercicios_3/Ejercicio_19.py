# *-* encoding:UTF-8 *-*
'''Uma sequência de pontos forma um polígono simples quando não há interseção entre as arestas do polígono. Daí,
a) Dada uma sequencia de n pontos, escreva um algoritmo para testar se o polígono formado pela sequencia de
pontos é simples ou não. Qual a complexidade do seu algoritmo?'''
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return (self.x,self.y)
    def __str__(self):
        return (self.x, self.y)

'''Given three colinear points p, q, r, the function checks if point q lies on line segment 'pr'
bool onSegment(Point p, Point q, Point r)
'''
def onSegment(p,q,r):
    if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)):
        return True
    return False

'''To find orientation of ordered triplet (p, q, r).
 The function returns following values
 0 --> p, q and r are colinear
 1 --> Clockwise
 2 --> Counterclockwise

 '''
def orientation(p,q,r):
    val= (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if (val == 0): return 0; #colinear
    elif val>0: #clock or counterclock wise
        return 1
    else:
        return 2


#The main function that returns true if line segment 'p1q1'  and 'p2q2' intersect.

def doIntersect(p1,q1,p2,q2):
#Find the four orientations needed for general and special cases
    o1=orientation(p1, q1, p2)
    o2=orientation(p1, q1, q2)
    o3=orientation(p2, q2, p1)
    o4=orientation(p2, q2, q1)

    # General case

    if o1!=o2 and o3 !=o4:
        return True

    '''Special Cases
    p1, q1 and p2 are colinear and p2 lies on segment p1q1'''
    if o1==0 and onSegment(p1,p2,q1):
        return True

    '''p1, q1 and q2 are colinear and q2 lies on segment p1q1 '''
    if o2==0 and onSegment(p1,q2,q1):
        return True

    '''p2, q2 and p1 are colinear and p1 lies on segment p2q2'''

    if o3==0 and onSegment(p2,p1,q2):
        return True

    '''p2, q2 and q1 are colinear and q1 lies on segment p2q2'''

    if o4 ==0 and onSegment(p2,q1,q2):
        return True
    ''' Doesn't fall in any of the above cases'''
    return False

def poligono_simple(puntos,n):
    if n==1:
        return False
    else:
        segmentos=[]
        for i in range(n-1):

            segmentos.append((puntos[i],puntos[i+1]))
        segmentos.append((puntos[n-1],puntos[0]))



        for i in range(len(segmentos)):
            count = 0

            for j in range(1,len(segmentos)):
                if i!=j:


                    if doIntersect(segmentos[i][0], segmentos[i][1], segmentos[j][0], segmentos[j][1]):
                        count += 1
                    if count>2:
                        return False
        return True








# p1=Point(1,1)
# q1=Point(2,3)
# p2=Point(3,1)
# q2=Point(3,2)
# p3=Point(1,2)
# lista=[p1,q1,p2,q2,p3]
# print(poligono_simple(lista,5))

p1=Point(1,3)
q1=Point(2,1)
p2=Point(4,2)
q2=Point(3,4)

#print(onSegment(p1,p2,q1))
#
lista=[p1,q1,p2,q2]
print(poligono_simple(lista,4))

#print(doIntersect(p1,q1,p2,q2))






