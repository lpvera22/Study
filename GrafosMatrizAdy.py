class GrafoMatrizAdy:
    def __init__(self):
        self.matrizAdy=[]

    def SonAdyacentes(self,v1,v2):
        if self.matrizAdy[v1][v2] !=0:
            return True
        else:
            return False

def GrafosIsoformos(g1,g2):
    if len(g1)==len(g2):
        for i in range(len(g1)):
            for j in range(len(g1)):
                if g1[i][j]!=g2[i][j]:

                    return False
        return True
    else:
        return False



