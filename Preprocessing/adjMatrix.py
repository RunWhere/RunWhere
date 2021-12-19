import json

def initializeMatrix(verticesName, edgeData):
    INF = 999999
    matrix = []
    
    listOfVerticesNames = []

    for vertex in verticesName:
        listOfVerticesNames.append(vertex['name'])

    for srcVertex in range(len(verticesName)):
        matrix.append([])
        for endVertex in range(len(verticesName)):
            if verticesName[srcVertex]['name'] == verticesName[endVertex]['name']:
                matrix[srcVertex].append([verticesName[srcVertex]['name'], verticesName[endVertex]['name'], 0])
            else:
                matrix[srcVertex].append([verticesName[srcVertex]['name'], verticesName[endVertex]['name'], INF])

    
    for i in edgeData:
        
        x = listOfVerticesNames.index(i[1])
        y = listOfVerticesNames.index(i[2])

        matrix[x][y][2] = i[3]
        matrix[y][x][2] = i[3]

    return (listOfVerticesNames, matrix)

def edgeListToAdjMatrix(zone):


    with open("Data/vertices_edges.json") as verticeNames:
        loadedVertices = json.load(verticeNames)

    verticesName = loadedVertices[zone]
    
    with open("Data/edge{}.json".format(zone)) as edgeName:
        loadedEdges  = json.load(edgeName)
        
    graphMatrix = initializeMatrix(verticesName, loadedEdges)
    
    return graphMatrix