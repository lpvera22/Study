import sys #, getopt
import numpy as np
from random import *

if len(sys.argv) != 6:
	print("Usage: generate.py <num_vertices> <num_edges> <MIN_WEIGHT> <MAX_WEIGHT> <output_file>")
	exit(-1)

#seed(int(sys.argv[6]))
def printMatrix(m):
	for i in range(vertices):
		for j in range(vertices):
			print("%i" % graph[i][j],end=" ")
		print()


vertices = int(sys.argv[1])
edges = int(sys.argv[2])

if edges > vertices*(vertices-1)//2:
	print("Graph cannot be generated. Too many edges")
	exit(-2)

MIN_WEIGHT = int(sys.argv[3])
MAX_WEIGHT = int(sys.argv[4])
output_file = str(sys.argv[5])

graph = np.zeros((vertices,vertices),dtype=np.bool)

weights = np.zeros((vertices,vertices))

degree = np.zeros(vertices,dtype=np.int)

open_set = np.zeros((vertices),dtype=np.bool)

num_edges = 0

list_vertices = [i for i in range(vertices)]

shuffle(list_vertices)
open_list = [list_vertices.pop()]

while len(list_vertices) > 0 and num_edges < edges:
	v1 = open_list[randint(0,len(open_list)-1)]
	v2 = list_vertices.pop()

	degree[v1] += 1
	degree[v2] += 1

	graph[v1][v2] = graph[v2][v1] = True
	weights[v1][v2] = weights[v2][v1] = randint(MIN_WEIGHT,MAX_WEIGHT)
	
	num_edges += 1
	open_list.append(v2)

while num_edges < edges:
	v1 = v2 = randint(0,vertices-1)
	while degree[v1] == vertices-1:
		v1 = v2 = randint(0,vertices-1)

	while v2 == v1 or graph[v1][v2] == True:
		v2 = randint(0,vertices-1)
		
	graph[v1][v2] = graph[v2][v1] = True
	weights[v1][v2] = weights[v2][v1] = randint(MIN_WEIGHT,MAX_WEIGHT)

	degree[v1] += 1
	degree[v2] += 1

	num_edges += 1

end = start = randint(0,vertices-1)
while end == start:
	end = randint(0,vertices-1)


o_file = open(output_file,'w')

o_file.write("%d %d\n" % (vertices,edges))
for i in range(0,vertices-1):
	for j in range(i+1,vertices):
		if graph[i][j]:
			o_file.write("%d %d %d\n" % (i+1,j+1,weights[i][j]))

o_file.write("%d %d" % (start+1,end+1))