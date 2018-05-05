class GrafoListaAd:
    def __init__(self):
        self.listaVer = {}
        self.numerovertices = 0





    def AgregarVertice(self,v):
        #new_v=Vertices(v)
        self.listaVer[v]=[]

    def EliminarVertice(self,v):
        if self.ExisteVerticeEnGrafo(v):
            del self.listaVer[v]
        else:
            print('Error')


    def EliminarArista(self,v1,v2):

        if self.ExisteVerticeEnGrafo(v1) and self.ExisteVerticeEnGrafo(v2):
            self.listaVer[v1].remove(v2)
            self.listaVer[v2].remove(v1)
        else:
            print('Error')




    def ExisteVerticeEnGrafo(self,v):
        if v in self.listaVer:
            return True
        else:
            return False



    def AdicionarArista(self,v1,v2):

        if not self.ExisteVerticeEnGrafo(v1) and not self.ExisteVerticeEnGrafo(v2):
            self.AgregarVertice(v1)
            self.AgregarVertice(v2)

        elif not self.ExisteVerticeEnGrafo(v1) and self.ExisteVerticeEnGrafo(v2):
            self.AgregarVertice(v1)

        else:
            self.AgregarVertice(v2)

        self.listaVer[v1].append(v2)
        self.listaVer[v2].append(v1)







#class Vertices:
    #def __init__(self, key):
        #self.key = key
        #self.ConectadoA = []

