# *-* encoding:UTF-8 *-*
'''int mem[][];
int lev(T[] A, T[] B) {
int n = length(A), m = length(B);
init(mem, n+1, m+1, -1);
for(i : 0 ... n) {
for(j : 0 ... m) {
if( i == 0 || j == 0 ) {
mem[i][j] = i + j;
} else if( A[i-1] == B[j-1] ) {
mem[i][j] = mem[i - 1][j - 1];
} else {
mem[i][j] = 1 + min(mem[i - 1, j], mem[i, j - 1], mem[i - 1, j - 1]);
}
}
}
return mem[n][m];
}'''

def D(A,B):
    n=len(A)
    m=len(B)
    mem=[[-1]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j ==0:
                mem[i][j]=i+j
            elif A[i-1] == B[j-1]:
                mem[i][j] = mem[i - 1][j - 1]
            else:
                mem[i][j] = 1 + min(mem[i - 1][j], mem[i][j - 1], mem[i - 1][j - 1])
    return mem

A='laura'
B='pelau'
mem=D(A,B)
for i in mem:
    print(i)




