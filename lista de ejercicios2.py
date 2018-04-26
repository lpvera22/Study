import math
#Implemente 1as operações de uma lista duplamente encadeada ordenada com célula cabeça.
#  Para cada uma das implementações obtenha a complexidade de tempo.

#Cria lista
class Nodo:
    def __init__(self, d ):
        self.data = d
        self.next = None
        self.prev = None

class LisDuple:
    def __init__(self):
        self.head = None
        self.tail = None

#Verifica se a lista está vazia
#O(2)

    def LisVazia(self):
        if self.head==None and self.tail==None:
            return True
        else:
            return False
#Insere um elemento com chave x na posição correta
#O(n)

    def Inserir(self,x):
        new_node=Nodo(x)
        if self.LisVazia():
            self.head=new_node
            self.tail=new_node
        elif self.head.data>new_node.data:
            aux=self.head
            new_node.next=aux
            self.head=new_node
            self.head.prev=None

        else:
            ap=self.head

            while(ap.data<new_node.data):
                ap=ap.next

            antes=ap.prev
            ap.prev=new_node
            new_node.next=ap
            new_node.prev=antes
            antes.next=new_node




#Procura um elemento com chave x
#O(n)

    def Localiza(self,x):
        aux=self.head
        if self.LisVazia():
            return False
        else:
            while(aux.data!=x or aux.next!=None):
                aux=aux.next
            if aux==self.tail and aux.data!=x:
                return False
            else:
                return True



#Remove um elemento com chave x , caso exista
# O(n)

    def Remover(self,x):
        if self.LisVazia():
            return False
        else:
            if(self.head.data==self.tail.data==x):
                self.head=self.tail=None
            elif self.head.data==x:
                self.head=self.head.next
                self.head.prev=None


            elif self.tail==x:
                self.tail=self.tail.prev
                self.tail.next=None
            else:
                aux1=self.head
                while (aux1.data!=x):
                    aux1=aux1.next
                if aux1==self.tail:
                    return False
                else:
                    antes=aux1.prev
                    despues=aux1.next
                    antes.next=depues
                    despues.prev=antes

            return True


#Intercalar duas listas ordenadas (gerando uma única lista ordenada contendo todos os elementos)
# O(n)
    def Intercalar(self,lista2):
        aux=lista2.head
        while(aux!=lista2.tail):
            self.Inserir(aux.data)




#Imprime os todos os elementos da lista
# O(n)
    def ImprimirLista(self):
        aux=self.head
        while(aux.next!=None or aux==self.tail):
            print(aux.data)
            aux=aux.next

#Destrói a lista
# O(1)
    def DestruirLista(self):
        self.head=self.tail=None


#EJERCICIO 2
#Utilize listas ordenadas para representar conjuntos.
# Considere a restrição que impeça a existência deelementos repetidos.
# Implemente o tipo de dados conjunto com
# as seguinte operações (apresente a complexidade de tempo de cada operação.):



# Adiciona um elemento x num conjunto
#O(n)
    def Adicionar(lista,x):
        if lista.__len__()==0:
            lista.append(x)
        else:
            for i in range(len(lista)):
                if lista[i]>x:
                    lista.insert(i,x)
                    break

#Determina a união de dois conjutos
#O(n)
def Union(conjunto1,conjunto2):

    for i in range(len(conjunto2)):
        Adicionar(conjunto1,conjunto2[i])



#Determina a interseção de dois conjutos
#O(n^2)
def Interseccion(conjunto1,conjunto2):
    inter=[]
    for i in conjunto2:
        for j in conjunto1:
            if i==j:
                Adicionar(inter,i)
    return inter

#Verifica se dois conjutos são iguais
#O(n^2)
def Iguales(conjunto1,conjunto2):
    flag=True
    for i in conjunto2:
        for j in conjunto1:
            if i!=j:
                flag=False
    return flag






#EJERCICIO 4
#Considere uma fila F não vazia, uma pilha P vazia e uma variável x .
# Proponha um algoritmo para inverter a ordem dos itens de F .
# Utilize em sua solução apenas as seguintes operações e testes.
#Operações:
#Empilha( P, x )
#x = Desempilha( P )
#Enfileira( F, x )
#x = Desenfileira( F )
#Vazia( F )
#Vazia(P)

class pila:
    def __init__(self):
        self.pila=[]
    def Empilha( self, x ):
        self.pila.append(x)
    def Desempilha(self):
        x=self.pila.pop()
        return x


class fila:
    def __init__(self):
        self.fila = []

    def Enfileira(self,x):
        self.fila.append(x)

    def Desenfileira(self):
        x=self.fila.pop(0)
        return x


def invertir(f):
    pila1=pila()
    while(Vacia(f)==False):
        pila1.Empilha(f.Desenfileira())

    while(Vacia(pila1)==False):
        f.Enfileira(pila1.Desempilha())

    return f



#EJERCICIO 5

'''Faça um programa para verificar a validade de uma expressão aritmética com
 relação à consistência dos delimitadores {, [ e (. Mais precisamente, o programa 
 deve conter uma função que receba uma  string contendo a expressão a ser
  analisada e verique o casamento entre estes delimitadores. Caso exista alguma 
  inconsistência, a função deve imprimir o delimitador que causou esta inconsistência e
sua posição na expressão.

Por exemplo, dada a expressão: {a − [b ∗ ((c − d)] + x} o programa deve imprimir:
delimitador ] na posicao 13 inválido
delimitador } na posicao 16 inválido
Para a expressão (((a + b) ∗ (c − d)) ∗ k))/w deve imprimir
delimitador ) na posicao 18 inválido
Para a expressão {[x + y] ∗ w − (a/b)} deve imprimir:
Expressao correta
OBS: para facilitar o tratamento (leitura dos elementos), 
suponha que a expressão seja formada por literais (variáveis) 
com apenas um caracter, pelos operadores +, -, * e / e pelos delimitadores (, ), [, ],
{ e }. Além disso, suponha que estes elementos NÃO sejam separados por espaços em branco.'''
def Vacia(p):
    if len(p)==0:
        return True
    else:
        return False
def expresionaritmetica(expresion):
    ex=expresion
    pila=[]
    error=0
    cont=0
    for i in range(len(ex)):
        if ex[i]=='(' or ex[i]=='[' or ex[i]=='{':
            pila.append(ex[i])
        elif ex[i]==')':
            if Vacia(pila):
                print('delimitador %s na posicao  %d invalido' % (ex[i], i + 1))
                error = error + 1
            elif pila.pop()!='(':
                error=error+1
                print('delimitador %s na posicao  %d invalido'%(ex[i],i+1))

        elif ex[i] == ']':
            if Vacia(pila):
                error = error + 1
                print('delimitador %s na posicao  %d invalido' % (ex[i], i + 1))
            elif pila.pop() != '[':
                error = error + 1
                print('delimitador %s na posicao  %d invalido' % (ex[i], i+1))
        elif ex[i] == '}':
            if Vacia(pila):
                error = error + 1
                print('delimitador %s na posicao  %d invalido' % (ex[i], i + 1))
            elif pila.pop() != '{':
                error = error + 1
                print('delimitador %s na posicao  %d invalido' % (ex[i], i+1))

    if error==0 and cont==0:

        print('Expresion Correcta')
    elif Vacia(pila)==False and error==0:
        print('Falta el cierre del delimitador %s'% pila.pop())



expre=input()
expresionaritmetica(expre)








#EJERCICIO 7
'''Empilhamento decrescente. Uma empilhadeira carrega caixas de 7, 5, 3 toneladas.
 Há três pilhas A , B , C . A pilha A é onde se encontram todas as caixas que chegam 
 no depósito. Com um detalhe: caixas maiores não podem ser empilhadas sobre caixas menores. 
 Elabore um algoritmo chamado ChegaNoDeposito (Pilha &P, Caixa x) que efetue o controle das 
 caixas, de forma que caso uma caixa de maior peso do que uma que já está em A deva ser empilhada,
  então, todas as caixas que estão em A são movidas para as pilhas auxiliares B 
  (contendo somente caixa de 5 toneladas) e C (contendo somente caixas de 3 toneladas) até que 
  se possa empilhar a nova caixa. Depois, todas as caixas são movidas de volta para a pilha A . Implemente e utilize os procedimentos com os seguintes protótipos:
int vazia (Pilha P);
int cheia (Pilha P);
void empilhar (Pilha &P, Caixa x);
void desempilhar (Pilha &P);
Caixa topo (Pilha P);
Apresente a complexidade de tempo dos procedimentos.'''

def ChegaNoDeposito(p,caja):
    # Implementar metodo topo, empilar y los demas
    #O(n^2)
    if caja>topo(p):
        aux=p.pop
        if aux==5:
            empilar(b,aux)
        elif aux==3:
            empilar(c,aux)
        ChegaNoDeposito(p,caja)
    else:
        empilar(p,caja)
        while(Vacia(c)==False):
            Empilar(p,c.pop())
        while (Vacia(b) == False):
            Empilar(p,b.pop())





#EJERCICIO 8
'''Escreva a operação de busca binária em um arranjo ordenado. Escreva duas versões da busca
 binária, uma recursiva e outra iterativa.'''
#recursiva
def busqueda_binaria(arreglo,elemento):
    n=len(arreglo)
    if arreglo[n/2]==elemento:
        return True
    elif arreglo[n/2]>elemento:
        return busqueda_binaria(arreglo[n/2:],elemento)
    elif arreglo[n/2]<elemento:
        return busqueda_binaria(arreglo[:n / 2], elemento)

    else:
        return False



#iterativa
def busqueda_binaria(arreglo, elemento):
    n = len(arreglo)
    izq=0
    der=n-1
    while izq<=der:
        medio=(izq+der)/2
        if arreglo[medio]==elemento:
            return True
        elif arreglo[medio]>elemento:
            der=medio-1
        else:
            izq=medio+1
    return False


#EJERCICIO 9
#Implemente as seguintes operações de árvores binárias de pesquisa.\n'

 #(a) Retira: remove item da árvore


class Arbol:
    def __init__(self, esMenorFunction=lambda x, y: x < y):
        self.raiz = None
        self.esMenor = esMenorFunction


class NodoBinario:
    def __init__(self, elemento, padre):
        self.elemento = elemento
        self.izquierda = None
        self.derecha = None
        self.padre = padre


def eliminar(arbol, element):
    eliminarNodo(arbol, buscarNodo(arbol.raiz, element, arbol.esMenor))


def eliminarNodo(arbol, nodo):
    if not tieneHijos(nodo):
        eliminarSinHijos(arbol, nodo)
    elif tieneAmbosHijos(nodo):
        eliminarConAmbosHijos(arbol, nodo)
    elif tieneHijoDerecho(nodo):
        eliminarCon1Hijo(arbol, nodo, nodo.derecha)
    else:
        eliminarCon1Hijo(arbol, nodo, nodo.izquierda)


def tieneHijoDerecho(nodo): return nodo.derecha != None


def tieneHijoIzquierdo(nodo): return nodo.izquierda != None


def tieneHijos(nodo): return tieneHijoDerecho(nodo) or tieneHijoIzquierdo(nodo)


def tieneAmbosHijos(nodo): return tieneHijoDerecho(nodo) and tieneHijoIzquierdo(nodo)


def esHijoIzquierdo(nodo): return nodo.padre.izquierda == nodo


def esRaiz(nodo): return nodo.padre == None


def eliminarSinHijos(arbol, nodo):
    if esRaiz(nodo):
        arbol.raiz = None
    elif esHijoIzquierdo(nodo):
        nodo.padre.izquierda = None
    else:
        nodo.padre.derecha = None


def eliminarCon1Hijo(arbol, nodo, hijo):
    if esRaiz(nodo):
        arbol.raiz = hijo
        arbol.raiz.padre = None
    elif esHijoIzquierdo(nodo):
        nodo.padre.izquierda = hijo
        hijo.padre = nodo.padre
    else:
        nodo.padre.derecha = hijo
        hijo.padre = nodo.padre


def eliminarConAmbosHijos(arbol, nodo):
    menorHijoRamaDerecha = buscarNodoMenorValor(nodo.derecha)
    eliminarNodo(arbol, menorHijoRamaDerecha)
    nodo.elemento = menorHijoRamaDerecha.elemento


def buscarNodoMenorValor(nodo):
    return nodo if nodo.izquierda == None else buscarNodoMenorValor(nodo.izquierda)


def buscarNodo(nodo, elemento, funcionEsMenor):
    if nodo.elemento == elemento:
        return nodo
    elif funcionEsMenor(elemento, nodo.elemento):
        return buscarNodo(nodo.izquierda, elemento, funcionEsMenor)
    else:
        return buscarNodo(nodo.derecha, elemento, funcionEsMenor)








#(b) Retira maior: remove maior item da árvore

def BuscaMayor(arbol):
    if not tieneHijoDerecho(arbol.raiz):
        return arbol.raiz.elemento
    else:
        return BuscaMayor(arbol.raiz.derecha)

def eliminarMayor(arbol):
    eliminar(arbol,BuscaMayor(arbol))
 #(c) Destrói: remove todos os nós da árvore e libera a memória

def DestruirArbol(arbol):
    if tieneHijoDerecho(arbol.raiz):

        if not tieneHijos(arbol.raiz.derecha):
            arbol.raiz.derecha=None
        else:
            DestruirArbol(arbol.raiz.derecha)


    if tieneHijoIzquierdo(arbol.raiz):

        if not tieneHijos(arbol.raiz.izquierda):
            arbol.raiz.izquierda = None
        else:
            DestruirArbol(arbol.raiz.izquierda)
    arbol.raiz=None









 #EJERCICIO 10
 #Altura


def altura(arbol):
    if arbol == None:
        return 0
    return 1 + maximaProfundidadDeHijo(arbol)


def maximaProfundidadDeHijo(arbol):
    return max([profundidad(arbol.izquierda), profundidad(arbol.derecha)])

def profundidad(arbol):
    return profundidadDeNodo(arbol.raiz)

def profundidadDeNodo(nodo):
    if nodo == None:
        return 0
    return 1 + max([profundidadDeNodo(nodo.izquierda), profundidadDeNodo(nodo.derecha) ])


#Tamano(numero de nodos en el arbol):
def Tamano(arbol):

    if not tieneHijos(arbol.raiz):
        return 1

    else:
        var=0
        if tieneHijoIzquierdo(arbol.raiz):
            var+=Tamano(arbol.raiz.izquierda)
        if tieneHijoDerecho(arbol.raiz):
            var+=Tamano(arbol.raiz.derecha)


        return var+1




#Cantidad de hojas
def cantHojas(arbol):
    if not tieneHijos(arbol.raiz):
        return 1
    else:
        var=0
        if tieneHijoIzquierdo(arbol.raiz):
            var += cantHojas(arbol.raiz.izquierda)
        if tieneHijoDerecho(arbol.raiz):
            var += cantHojas(arbol.raiz.derecha)

        return var
#numero de nodos internos

def nodosInternos(arbol):
    if not tieneHijos(arbol.raiz):
        return 0

    else:
        var=0
        if tieneHijoIzquierdo(arbol.raiz):
            var+=nodosInternos(arbol.raiz.izquierda)
        if tieneHijoDerecho(arbol.raiz):
            var+=nodosInternos(arbol.raiz.derecha)


        return var+1


#EJERCICIO 12
def imprimir1(arbol,nivel):
    s='%'+str(nivel)+'s'
    print(s %arbol.raiz.elemento)
    if not tieneHijoIzquierdo(arbol.raiz):
        s='%'+str(nivel+3)+'s'
        print(s %' ' )
    else:
        imprimir1(arbol.raiz.izquierda,nivel+3)

    if not tieneHijoDerecho(arbol.raiz):
        s='%'+str(nivel+3)+'s'
        print(s %' ' )
    else:
        imprimir1(arbol.raiz.derecha,nivel+3)



def imprimir2(arbol, nivel):
    print('('+srt(arbol.raiz.elemento),end='')
    if not tieneHijoIzquierdo(arbol.raiz):
        print('()',end='')
    else:
        imprimir1(arbol.raiz.izquierda, nivel + 3)

    if not tieneHijoDerecho(arbol.raiz):
        print('()',end='')
    else:
        imprimir1(arbol.raiz.derecha, nivel + 3)
    print(')')




#EJERCICIO 13
def mayorllavemenor(arbol,k):
    nod=buscarNodo(arbol.raiz,k)
    if nod==None:
        raise Exception('Llave no existe en el arbol')
    else:
        BuscaMayor(nod.raiz.izquierda)

