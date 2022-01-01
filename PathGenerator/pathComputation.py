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

def startEndToPathDist(start, end):

    - The start and end should be within the same zone 
    - resolve the points to path by backtracing && lookup the dist matrix 

    return currPath,  dist


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

listPath = []
Load connector, dist, path and vertices' names json files

call checkStartDist(currLocation, userDist, currPath=[], zone)
call rankPaths(listPath) and output the result
'''