# *-* encoding:UTF-8 *-*
'''LCS(X,Y,n,m){
for(i=1;i<=n;i++) L[i,0] = 0;
for(j=1;j<=m;j++) L[0,j] = 0;
for(i=1;i<=n;i++)
    for(j=1;j<=m;j++)
        if(X[i] ==Y[i])
            L[i,j] = L[i-1, j-1] +1;
        else if(L[i-1,j] >= L[i, j-1] )
            L[i,j] = L[i-1,j];
        else
            L[i,j] = L[i, j-1];
}'''
def LCS(X,Y,n,m):
    L=[[None]*(n+1) for i in range(m+1)]


    for i in range(m+1):
        L[i][0]=[]
    for j in range(n+1):
        L[0][j]=[]


    for i in range(1,m+1):
        for j in range(1,n+1):
            if (X[i-1] == Y[j-1]):

                var=L[i - 1][j - 1][:]
                var.append(X[i-1])
                L[i][j]=var


            else:
                L[i][j]=max(L[i-1][j],L[i][j-1],key=lambda p:len(p))

    return L[i][j]
'''ObtemLCS(L, X, Y, i, j){
    if(i!=0 && j!=0){
        if ( X[i] == Y[j]){
            ObtemLCS(L, X, Y, i-1, j-1);
            cout << X[i];
            }
        else if (L[i,j] == L[i-1,j])
            ObtemLCS (L, X, Y, i-1,  j);
        else ObtemLCS(L, X, Y, i, j-1);
}'''
def ObtemLCS(L,X,Y,i,j):
    if i!=0 and j!=0:
        if X[i-1]==Y[j-1]:
            ObtemLCS(L, X, Y, i - 1, j - 1)
            print X[i-1]
        elif L[i][j] == L[i-1][j]:
            ObtemLCS(L, X, Y, i - 1, j)
        else:
            ObtemLCS(L, X, Y, i, j - 1)


if __name__=="__main__":
    X = 'abcdefg'
    Y = 'hfbcdka'
    n =len(Y)
    m = len(X)

    aux=LCS(X,Y,n,m)
    print(aux)
    #ObtemLCS(aux,X,Y,m,n)


