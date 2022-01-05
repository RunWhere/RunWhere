import json

distArray = [2.4, 5, 10]

# def pathGen(currLocationWithZone, userDistanceOption):

#     # currLocationWithZone is an array [currLocation, zone]
#     # open the dist and path matrix files based on zones
#     # currLocationWithZone
    
#     zone = currLocationWithZone[1]
#     currLocation = currLocationWithZone[0]

#     # (might face bugs when migrating to databases)
#     with open("data/%s.json" % (zone + "_DistMatrix.json")) as distMatrix:
#         loadedDistMatrix = json.load(distMatrix)

#     with open("data/%s.json" % (zone + "_PathMatrix.json")) as pathMatrix:
#         loadedPathMatrix = json.load(pathMatrix)
    
#     with open("Data/vertices_edges.json") as verticeNames:
#         loadedVertices = json.load(verticeNames)

#     verticesName = loadedVertices[zone]


    
#     returnTopPaths(currLocation, userDistanceOption, loadedDistMatrix, loadedPathMatrix, verticesName, zone)
    
        
#     # iterate floyd warhsall distance matrix
#     # find out those distances that meets the userDist

#     # then we iterate the path matrix
#     # return 3 paths sorted by |dist - userDist| -> 0

# def optionToDist(userDistanceOption):
#     # userDistanceOption (3 options: 2.4, 5 and 10km)
#     # return half the dist

#     return distArray[userDistanceOption - 1] / 2

# def retrievePath(dist, currLocation, loadedDistMatrix, loadedPathMatrix, verticeNames):
#     listOfPossiblePaths = []
#     listOfVerticesNames = []

#     for vertex in verticeNames:
#         listOfVerticesNames.append(vertex['name'])

#     for idx in range(len(loadedDistMatrix)):

#         # tempStart = currLocation
#         # tempEnd = loadedDistMatrix[idx][0] if loadedDistMatrix[idx][0] != tempStart else loadedDistMatrix[idx][1]


#         tempStart = loadedDistMatrix[idx][0] 
#         tempEnd = loadedDistMatrix[idx][1]


#         if tempStart == currLocation or tempEnd == currLocation:

#             pathResolutionLst = []

#             if tempStart != currLocation:
#                 temp = tempStart
#                 tempStart = tempEnd
#                 tempEnd = temp
    
#             idxStart = listOfVerticesNames.index(tempStart)
#             idxEnd = listOfVerticesNames.index(tempEnd)
#             nxtIdx = idxEnd
#             pathResolutionLst.append(tempEnd)
#             while(True):
#                 nxtIdx = loadedPathMatrix[idxStart][nxtIdx]
#                 pathResolutionLst.append(listOfVerticesNames[nxtIdx])
#                 if nxtIdx == idxStart:
#                     pathResolutionLst.append(tempStart)
#                     break

#             if abs(dist - loadedDistMatrix[idx][2]) <= 0.3:
#                 listOfPossiblePaths.append([pathResolutionLst.reverse(), loadedDistMatrix[idx][2]])
                
#     return listOfPossiblePaths

# def retrieveNextZoneConnector(currLocation, zone, dist, loadedDistMatrix, loadedPathMatrix, verticesName):
    
#     listOfVerticesNames = []
#     for vertex in verticesName:
#         listOfVerticesNames.append(vertex['name'])

#     connectorsStartZones = []

#     with open("Data/connectors.json") as connectors:
#         loadedConectors = json.load(connectors)

#         for i, o in zip(loadedConectors.keys(), loadedConectors):

#             if zone in i: 
#                 # This means the start matches
#                 connectorsStartZones.append(['Zone' + i[-1], o[1]])
                
                
#             elif zone[-1] in i:
#                 # This means the end matches
#                 connectorsStartZones.append([i[::len(i) -1], o[0]])
                
#             else:
#                 continue

#     #     idxStart = listOfVerticesNames.index(tempStart)
#     #     idxEnd = listOfVerticesNames.index(tempEnd)
#     #     loadedConnectors = json.load(connectors)
        
#     # pathsAfterConcat = []
#     # while (dist >= 0):
        
#     #     dist -= loadedDistMatrix[][]
#     #     pass

#     return connectorsStartZones

# def rankPaths(lstAllPaths):
    
    
#     # sort the list based on the dist
#     lstAllPaths.sort(key = lambda x: x[1])

#     # return top 3 that meets the dist the user wants
#     return lstAllPaths[:2]



# def returnTopPaths(currLocation, userDistanceOption, loadedDistMatrix, loadedPathMatrix, verticesName, zone):
#     dist = optionToDist(userDistanceOption)
#     listOfPossiblePaths = retrievePath(dist, currLocation, loadedDistMatrix, loadedPathMatrix, verticesName)
#     connectorsStartZones = retrieveNextZoneConnector(currLocation, zone, dist, loadedDistMatrix, loadedPathMatrix, verticesName)
#     # Need another line here
#     return rankPaths(listOfPossiblePaths + pathsAfterConcat)
    



'''
1.

def startEndToPathDist(start, end, zoneName):

    - The start and end should be within the same zone 
    - resolve the points to path by backtracing && lookup the dist matrix 

    currPath = []

    dist = 0

    verticeList = zoneNameToVerticeList(zoneName)
    distMatrix = zoneNameToDistanceMatrix(zoneName)
    pathMatrix = zoneNameToPathMatrix(zoneName)

    try:
        endIndex = verticeIndex(end, verticeList)

        currIndex = verticeIndex(start, verticeList)
    except Exception as e:
        raise KeyError(e + " in " + zoneName)

    currVertice = start

    while currVertice != end:
        currPath.append(verticeList[currIndex]["name"])
        
        tempIndex = pathMatrix[endIndex][currIndex]
        
        try:
            dist += distMatrix[currIndex][tempIndex][2]
        except IndexError:
            raise IndexError("distanceMatrix invalid indexes " + currIndex + " " + tempIndex)
            
        currIndex = tempIndex

        currVertice = verticeList[currIndex]["name"]

    currPath.append(end)

    return (currPath, dist)


def verticeIndex(vertice, zone):
    
    for count, x in enumerate(zone):
        if x["name"] == vertice:
            return count

    raise KeyError("vertice " + vertice + "is not found")


def zoneNameToPathMatrix(zoneName):

    lower = zoneName.lower()

    if lower == "zonea":
        return pathMatrix_A
    elif lower == "zoneb":
        return pathMatrix_B
    elif lower == "zonec":
        return pathMatrix_C
    else:
        raise NameError("Incorrect zone name")


def zoneNameToVerticeList(zoneName):
    
    lower = zoneName.lower()
    
    if lower == "zonea":
        return verticesName_A
    elif lower == "zoneb":
        return verticesName_B
    elif lower == "zonec":
        return verticesName_C
    else:
        raise NameError("Incorrect zone name")

def zoneNameToDistanceMatrix(zoneName):

    lower = zoneName.lower()
    
    if lower == "zonea":
        return distMatrix_A
    elif lower == "zoneb":
        return distMatrix_B
    elif lower == "zonec":
        return distMatrix_C
    else:
        raise NameError("Incorrect zone name")

2.
listPath = []

def checkStartDist(currLocation, userDist, currPath(include dist), zone):

    - if (dist is postiive):
        - Run within Zone (all those that meet the requirement)
            - call the startEndToPathDist, generate a path and connect to currPath
            - then add it to the listPath

        - Run to connector x 2 
            - call the startEndToPathDist (start to connector) which returns the semi-generated path, accumulated path dist
            - run checkStartDist(nextZoneConnector, dist - accumulated path dist, semi-generated path, nextZone)

        
3.
def rankPaths(listPath):

    - rank the paths based on abs(dist - userDist) -> 0 using the pathsDist in listPath
    - return top 3 results

4. (EntryPoint)

'''

# Entry Point

# listPath -> [(Path, dist), (Path, dist), (Path, dist) ...]
listPath = []
with open("Data/ZoneA_DistMatrix.json") as distMatrix:
    distMatrix_A = json.load(distMatrix)
    
with open("Data/ZoneB_DistMatrix.json") as distMatrix:
    distMatrix_B = json.load(distMatrix)

with open("Data/ZoneC_DistMatrix.json") as distMatrix:
    distMatrix_C = json.load(distMatrix)

with open("Data/ZoneA_PathMatrix.json") as pathMatrix:
    pathMatrix_A = json.load(pathMatrix)

with open("Data/ZoneB_PathMatrix.json") as pathMatrix:
    pathMatrix_B = json.load(pathMatrix)

with open("Data/ZoneC_PathMatrix.json") as pathMatrix:
    pathMatrix_C = json.load(pathMatrix)

with open("Data/vertices_edges.json") as verticeNames:
    loadedVertices = json.load(verticeNames)

    verticesName_A = loadedVertices["ZoneA"]
    verticesName_B = loadedVertices["ZoneB"]
    verticesName_C = loadedVertices["ZoneC"]

with open("Data/connectors.json") as connector:
    loadedConnector = json.load(connector)

    connector_A = loadedConnector["ZoneA"]
    connector_B = loadedConnector["ZoneB"]
    connector_C = loadedConnector["ZoneC"]


def main(currLocation, userDistOption, zone):

    userDist = distArray[userDistOption - 1] / 2

    '''
    
    Load connector, dist, path and vertices' names json files

    call checkStartDist(currLocation, userDist, currPath=[], zone)
    call rankPaths(listPath) and output the result
    
    '''
    checkStartDistSameZone(currLocation, zone, distMatrix)
    checkStartDist(currLocation, userDist, zone)
    topPaths = rankPaths()

    print(topPaths)
    
# Function 2


def checkStartDistSameZone(currLocation, zone, distMatrix):
        # Within same zone get all the paths with either than same start or end point as the user that pass the check
        '''
        - Run within Zone (all those that meet the requirement)
            - call the startEndToPathDist, generate a path and connect to currPath
            - then add it to the listPath
        '''
        for idx in range(len(distMatrix)):

            tempStart = distMatrix[idx][0] 
            tempEnd = distMatrix[idx][1]

            if tempStart == currLocation or tempEnd == currLocation:

                if tempStart != currLocation:
                    temp = tempStart
                    tempStart = tempEnd
                    tempEnd = temp
        
            tempPath, tempDist = startEndToPathDist(tempStart, tempEnd, zone)

            listPath.append([tempPath, tempDist])
        
    
def checkStartDist(currLocation, userDist, zone, currPath = [], totalDist = 0):
    
    # Connector Resolution
    '''
    - Run to connector x 2 
        - call the startEndToPathDist (start to connector) which returns the semi-generated path, accumulated path dist
        - run checkStartDist(nextZoneConnector, dist - accumulated path dist, semi-generated path, nextZone)
    '''
    
    if (userDist > 0):

        # For connectors resolution
        # Get the 2 different connectors for the current zone

        currConnector = connector_A
        nextCon1 = "ZoneB"
        nextCon2 = "ZoneC"

        if zone == "ZoneB":
            currConnector = connector_B
            nextCon1 = "zoneA"
            nextCon2 = "ZoneC"
            
        elif zone == "ZoneC":
            currConnector = connector_C
            nextCon1 = "ZoneA"
            nextCon2 = "ZoneB"

       
        # resolve the endpoint for the next 2 connector
        endPoint1 = currConnector[0][nextCon1][1]
        endPoint2 = currConnector[0][nextCon2][1]
        
        
        tempPath1, tempDist1 = startEndToPathDist(currLocation, endPoint1, zone)
        tempPath2, tempDist2 = startEndToPathDist(currLocation, endPoint2, zone)

        try:
            updatedTempPath1 = currPath + tempPath1[1::]
            
        except Exception as e:
            raise e + ", In checkStartDist updatedTempPath1 failed ..."
        try:
            updatedTempPath2 = currPath + tempPath2[1::]
        except Exception as e:
            raise e + ", In checkStartDist updatedTempPath2 failed ..."
        
        totalDist += tempDist1
        checkStartDist(endPoint1, userDist - tempDist1, nextCon1, updatedTempPath1, totalDist)
        
        totalDist = totalDist - tempDist1 + tempDist2
        checkStartDist(endPoint2, userDist - tempDist2, nextCon2, updatedTempPath2, totalDist)

        
    else:
        try:
            listPath.append([currPath, totalDist])
        except Exception as e:
            raise e + ", In return call of the recursive base case"
            
        
        
    


# funtion 3

def rankPaths(listPath, userDist):
    def get_dist(path):
        return abs(path[1] - userDist)

    listPath.sort(key=get_dist)

    topPaths = listPath[:3]

    return topPaths

# function 4
## to mirror the ranked paths

def completePaths(rankedPaths):
    ## rankedPath = [[[path], dist], [[path], dist]]  
    completePath = []
    for i in rankedPaths:

        # i[0] is the path, i[1] 
        completePath.append([i[0] + i[0][::-1][1::], i[1] * 2])
    return completePath