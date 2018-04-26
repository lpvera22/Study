class Fila:
    def __init__(self,max):
        self.items=[]
        self.inicio=-1
        self.fin=-1
        self.max=max

    def Vacia(self):
        if cant==0:
            return True
        else:
            return False

    def Llena(self):
        if self.items[self.max]==max-1:
            return True
        else:
            return False




    def enfilar(self,elem):
        if self.Llena():
            return False
        else:
            if self.fin==self.max-1:
                self.fin==0
            else:
                self.fin=self.fin+1

            self.items.insert(self.fin, elem)








fila=[1,2,3,4,5]
pila=[]
def invertirorden(pila,fila):
    for i in fila:
        x=i
        pila.append(x)

    for i in pila:
        x=pila.pop()
        fila.append

