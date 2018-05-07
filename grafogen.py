import numpy as np
from random import *

def printMatrix(m):
	for i in range(len(m)):
		for j in range(len(m)):
			print("%i" % m[i][j]),
		print

def GenGrafo(vertices,edges,min_weight=1, max_weight=100):
    if edges > vertices * (vertices - 1) // 2:
        print("Graph cannot be generated. Too many edges")
        return None
    else:
        matriz = np.zeros((vertices, vertices), dtype=np.int)
        degree = np.zeros(vertices, dtype=np.int)
        num_edges = 0

        lst_vert = [i for i in range(vertices)]

        shuffle(lst_vert)
        open_list = [lst_vert.pop()]
        while len(lst_vert) > 0 and num_edges < edges:
            v1 = open_list[randint(0, len(open_list) - 1)]
            v2 = lst_vert.pop()

            degree[v1] += 1
            degree[v2] += 1

            matriz[v1][v2] = matriz[v2][v1] = randint(min_weight, max_weight)

            num_edges += 1
            open_list.append(v2)
        while num_edges < edges:
            v1 = v2 = randint(0, vertices - 1)
            while degree[v1] == vertices - 1:
                v1 = v2 = randint(0, vertices - 1)

            while v2 == v1 or matriz[v1][v2] == True:
                v2 = randint(0, vertices - 1)

            matriz[v1][v2] = matriz[v2][v1] = randint(min_weight, max_weight)

            degree[v1] += 1
            degree[v2] += 1

            num_edges += 1

        # end = start = randint(0, vertices - 1)
        # while end == start:
        #     end = randint(0, vertices - 1)

        return (lst_vert, matriz)
l,m=GenGrafo(5,5)
printMatrix(m)