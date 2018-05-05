class GrafoMatrizAdy:
    def __init__(self):
        self.matrizAd=[[]]
        self.vertices=[]

def BL(grafos):
    v=[False]*len(grafos.vertices)
    F=[]
    resultado=[]
    F.append(grafos.vertices[0])
    while len(F) !=0:
        temp=F.pop(0)
        resultado.append(temp)
        v[grafos.vertices.index(temp)]=True
        for i in range(len(grafos.matrizAd[grafos.vertices.index(temp)])):
            if grafos.matrizAd[grafos.vertices.index(temp)][i]==1 and v[grafos.vertices.index(i)]!=True :
                F.insert(i)
    return resultado

def BP(grafos,v,resultado,vertice):
   v[grafos.vertices.index(vertice)]=True
   resultado.append(vertice)
   for i in range(len(grafos.matrizAd[grafos.vertices.index(vertice)])):
       if grafos.matrizAd[grafos.vertices.index(vertice)][i]==1 and v[grafos.vertices.index(i)]!=True:
           BP(grafos,v,resultado,grafos.vertices[i])











    def Imprimir(self):

