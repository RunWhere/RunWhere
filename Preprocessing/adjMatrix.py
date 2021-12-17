import json

def initializeMatrix(verticesName, edgeData):
    INF = 999999
    matrix = []
    
    for srcVertex in range(len(verticesName)):
        matrix.append([])
        for endVertex in range(len(verticesName)):
            if verticesName[srcVertex]['name'] == verticesName[endVertex]['name']:
                matrix[srcVertex].append([verticesName[srcVertex]['name'], verticesName[endVertex]['name'], 0])
            else:
                matrix[srcVertex].append([verticesName[srcVertex]['name'], verticesName[endVertex]['name'], INF])
    

    # for srcVertex in range(len(data)):
    #     for endVertex in range(len(data)):
    #         matrix.append(data[srcVertex])
    return matrix

def edgeListToAdjMatrix(zone):
    

    with open("Data/vertices_edges.json") as verticeNames:
        loadedVertices = json.load(verticeNames)

    verticesName = loadedVertices['ZoneA']
    
    with open("Data/edge{}.json".format(zone)) as edgeName:
        loadedEdges  = json.loadedEdges(edgeName)
        
    print(verticesName)
    print(loadedEdges)
    
    graphMatrix = initializeMatrix(verticesName, loadedEdges)
    
    return graphMatrix