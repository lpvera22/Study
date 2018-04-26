#lista duplamente encadeada
class NodeDup:
    def __init__(self,d,):
        self.data=d
        self.next=None
        self.prev=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev

class LisDuple:
    def __init__(self):
        self.head=None
        self.tail=None
#Cria a lista vazia, Localiza, Insere e Remove
    def LisVazia(self):
        if self.head==None
            return True
        else:
            return False

    def Localiza(self,item):
        aux=self.head
        while aux:
            if aux.data==item :
                return True
            else:
                aux=aux.next
                if aux==self.head:
                    return False




    def Insere_Inicio(self,item):
        new=NodeDup(item)
        if self.LisVazia():
            self.head=self.tail=new
        else:
            new.setNext(self.head)
            self.head.prev=new
            self.head=new

    def Insere_Final(self,item):
        new=NodeDup(item)
        if self.LisVazia():
            self.head=self.tail=new
        else:
            self.tail.setNext(new)
            new.prev=self.tail
            self.tail=new

    def Elimine_Inicio(self):

        if self.LisVazia():
            print("Lista Vacia")
        elif self.head== self.tail:
            self.head=self.tail=None
        else:
            self.head=self.head.next
        self.head.prev=self.tail
        self.tail.next=self.head

    def Elimine_Final(self):
        if self.LisVazia():
            print("Lista Vacia")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail=self.tail.prev
        self.head.prev = self.tail
        self.tail.next = self.head




