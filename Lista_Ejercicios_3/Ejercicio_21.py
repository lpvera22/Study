# *-* encoding:UTF-8 *-*
def cross(o,a,b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def puntos_colineales(lista):
    if len(lista)==2:
        return True
    else:
        var=True
        for i in range(len(lista)-2):
            if cross(lista[i],lista[i+1],lista[i+2])!=0:
                var=False
        return var
lista=[(2,2),(1,1),(3,1),(4,4),(5,5)]
print(puntos_colineales(lista))
