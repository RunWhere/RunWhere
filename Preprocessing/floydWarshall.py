INF = 999999

# https://www.techiedelight.com/pairs-shortest-paths-floyd-warshall-algorithm/
# Function to run the Floyd–Warshall algorithm
def floydWarshall(adjMatrix):
    
    # total number of vertices in the `adjMatrix`
    n = len(adjMatrix)
 
    # cost and path matrix stores shortest path
    # (shortest cost/shortest route) information
 
    # initially, cost would be the same as the weight of an edge
    dist = adjMatrix.copy()
    path = [[None for x in range(n)] for y in range(n)]
 
    
    # initialize cost and path
    for v in range(n):
        for u in range(n):
            # if v == u:
            #     path[v][u] = 0
            # print(dist[v])
            # print(dist[v][u][2])
            if dist[v][u][2] != INF or v == u:
                path[v][u] = v
            else: 
                path[v][u] = -1
 
    # run Floyd–Warshall
    for k in range(n):
        for v in range(n):
            for u in range(n):
                # If vertex `k` is on the shortest path from `v` to `u`,
                # then update the value of cost[v][u] and path[v][u]
                if dist[v][k][2] != INF and dist[k][u][2] != INF and (dist[v][k][2] + dist[k][u][2] < dist[v][u][2]):
                    dist[v][u][2] = dist[v][k][2] + dist[k][u][2]
                    path[v][u] = path[k][u]

    return (dist, path)