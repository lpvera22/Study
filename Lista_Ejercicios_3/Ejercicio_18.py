# *-* encoding:UTF-8 *-*
def convex_hull(points):


    # Ordena os pontos de menos a maior pelo exio x.

    points = sorted(set(points))

    # Base: qando tenha 0 o só um punto retorna a lista.
    if len(points) <= 1:
        return points


    #cross retorna se os pontos O A B estão na orden de anti-horaria retornando um valor positivo se estam na
    #  orden horaria retorna o valor negativo e 0 se os pontos son colineares
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Construyendo o casco convexo mais baixo
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Construyendo o casco convexo da acima
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)


    #Juntando os dois cascos convexos
    return lower[:-1] + upper[:-1]
points=[(1,1),(2,2),(3,3),(3,1),(1,3)]
print(convex_hull(points))
