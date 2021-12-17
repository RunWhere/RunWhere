INF = 99999

def floydWarshall(graph):

    # do the triple for loop
    '''
    for (int k = 0; k < V; k++) // remember, k first
        for (int i = 0; i < V; i++) // before i
            for (int j = 0; j < V; j++) // then j
                D[i][j] = Math.min(D[i][j], D[i][k]+D[k][j]);
    '''

    pathMatrix = []
    dist = []

    numVertices = len(graph)
    for k in range(numVertices):
        for i in range(numVertices):
            for j in range(numVertices):

                continue

    return (pathMatrix, dist)