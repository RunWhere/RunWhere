import json

distArray = [2.4, 5, 10]

def pathGen(currLocationWithZone, userDistanceOption):

    # currLocationWithZone is an array [currLocation, zone]
    # open the dist and path matrix files based on zones
    # currLocationWithZone
    
    zone = currLocationWithZone[1]
    currLocation = currLocationWithZone[0]

    # (might face bugs when migrating to databases)
    with open("data/%s.json" % (zone + "_DistMatrix.json")) as distMatrix:
        loadedDistMatrix = json.load(distMatrix)

    with open("data/%s.json" % (zone + "_PathMatrix.json")) as pathMatrix:
        loadedPathMatrix = json.load(pathMatrix)
    
    with open("Data/vertices_edges.json") as verticeNames:
        loadedVertices = json.load(verticeNames)

    verticesName = loadedVertices[zone]


    
    returnTopPaths(currLocation, userDistanceOption, loadedDistMatrix, loadedPathMatrix, verticesName, zone)
    
        
    # iterate floyd warhsall distance matrix
    # find out those distances that meets the userDist

    # then we iterate the path matrix
    # return 3 paths sorted by |dist - userDist| -> 0

def optionToDist(userDistanceOption):
    # userDistanceOption (3 options: 2.4, 5 and 10km)
    # return half the dist

    return distArray[userDistanceOption - 1] / 2

def retrievePath(dist, currLocation, loadedDistMatrix, loadedPathMatrix, verticeNames):
    listOfPossiblePaths = []
    listOfPossiblePathsConcat = []
    listOfVerticesNames = []

    for vertex in verticeNames:
        listOfVerticesNames.append(vertex['name'])

    for idx in range(len(loadedDistMatrix)):

        # tempStart = currLocation
        # tempEnd = loadedDistMatrix[idx][0] if loadedDistMatrix[idx][0] != tempStart else loadedDistMatrix[idx][1]


        tempStart = loadedDistMatrix[idx][0] 
        tempEnd = loadedDistMatrix[idx][1]


        if tempStart == currLocation or tempEnd == currLocation:

            pathResolutionLst = []

            if tempStart != currLocation:
                temp = tempStart
                tempStart = tempEnd
                tempEnd = temp
    
            idxStart = listOfVerticesNames.index(tempStart)
            idxEnd = listOfVerticesNames.index(tempEnd)
            nxtIdx = idxEnd
            pathResolutionLst.append(tempEnd)
            while(True):
                nxtIdx = loadedPathMatrix[idxStart][nxtIdx]
                pathResolutionLst.append(listOfVerticesNames[nxtIdx])
                if nxtIdx == idxStart:
                    pathResolutionLst.append(tempStart)
                    break

            if abs(dist - loadedDistMatrix[idx][2]) <= 0.3:
                listOfPossiblePaths.append([pathResolutionLst.reverse(), loadedDistMatrix[idx][2]])
                
                

    return listOfPossiblePaths

def pathConcat(currLocation, zone, dist, loadedDistMatrix, loadedPathMatrix, verticesName):
    
    listOfVerticesNames = []
    for vertex in verticesName:
        listOfVerticesNames.append(vertex['name'])
        
    with open("Data/connectors.json") as connectors:
        loadedConectors = json.load(connectors)

        for i in loadedConectors.keys():

            if zone in i:
                # This means the start matches
                
                
                
            elif zone[-1] in i:
                # This means the end mathces
                
                
            else:
                continue
                

            



        idxStart = listOfVerticesNames.index(tempStart)
        idxEnd = listOfVerticesNames.index(tempEnd)
        loadedConnectors = json.load(connectors)
        
    pathsAfterConcat = []
    while (dist >= 0):
        
        dist -= loadedDistMatrix[][]
        pass

    return pathsAfterConcat

def rankPaths(lstAllPaths):
    
    
    # sort the list based on the dist
    lstAllPaths.sort(key = lambda x: x[1])

    # return top 3 that meets the dist the user wants
    return lstAllPaths[:2]



def returnTopPaths(currLocation, userDistanceOption, loadedDistMatrix, loadedPathMatrix, verticesName, zone):
    dist = optionToDist(userDistanceOption)
    listOfPossiblePaths = retrievePath(dist, currLocation, loadedDistMatrix, loadedPathMatrix, verticesName)
    pathsAfterConcat = pathConcat(currLocation, zone, dist, loadedDistMatrix, loadedPathMatrix, verticesName)
    return rankPaths(listOfPossiblePaths + pathsAfterConcat)
    
