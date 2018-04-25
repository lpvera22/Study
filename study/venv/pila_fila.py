def empilar(elem,pila):
    pila.append(elem)

def pila_vacia(pila):
    n=pila.__len__()
    if n>0:
        return False
    else:
        return True

def desempilar(pila):
    #n = pila.__len__()
    if pila_vacia(pila)==False:
        pila.pop()
    else:
        print("La pila no tiene elementos")







def enfilar(elem,fila):

    fila.append(elem)

def fila_vacia(fila):
    n=fila.__len__()
    if n>0:
        return False
    else:
        return True

def desenfilar(fila):
    if fila_vacia(fila)==False:
        fila.pop(0)
    else:
        print("La fila no tiene valores")

fila=[1,2,2,4]
for i in fila:
    if fila_vacia(fila)==False:
        desenfilar(fila)
    else:
        end
print(fila)
