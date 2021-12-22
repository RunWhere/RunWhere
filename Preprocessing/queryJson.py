from adjMatrix import *
from floydWarshall import *
import json
from math import asin, cos, radians, sin, sqrt


fileName = ['edgeZoneA_complete_edges', 'edgeZoneB_complete_edges', 'edgeZoneC_complete_edges']
    
def distance(lat1, lon1, lat2, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)

# Step 1 -> Form complete graph for each zone
# store all of the complete graph in an edgelist
# edgeListZoneA = [
#     ["ZoneA","Faculty of Engineering","Temasek Lab",dist],
# ]

'''
def completeGraphEdgeGen(zoneX, jsonData):
    zoneX <- jsonData['zoneX']
    completeEdgeZoneX = [][]
    ## Filter duplicated edges
    for i in range(0,len(zoneX)): # all the vertices
        for k in range(i + 1, len(zoneX)):
            tempDist <- distance(zoneX[i].lat, zoneX[i].lon, zoneX[k].lat, zoneX[k].lon)
            completeEdgeZoneX.append([zoneX, zoneX[i].name, zoneX[k].name, tempDist])

    return completeEdgeZoneX
'''

def completeGraphEdgeGen(zone, jsonData):
    zoneX = jsonData[str(zone)]
    completeEdgeZoneX = []

    # all the vertices
    for i in range(0,len(zoneX)):

        ## Filter duplicated edges
        for k in range(i + 1, len(zoneX)):

            tempDist = distance(zoneX[i]['latitude'], zoneX[i]['longitude'], zoneX[k]['latitude'], zoneX[k]['longitude'])
            completeEdgeZoneX.append([zone, zoneX[i]['name'], zoneX[k]['name'], tempDist])

    return completeEdgeZoneX

def createFile(zoneX, edgeZoneX):
    with open("Data/{}.json".format(zoneX), 'w') as outfile:
        json.dump(edgeZoneX, outfile, indent=4)


def exportEdge():

    with open("Data/verticles_edges.json") as data:
        loaded = json.load(data)
        
    edgeZoneA = completeGraphEdgeGen('ZoneA',loaded)
    edgeZoneB = completeGraphEdgeGen('ZoneB',loaded)
    edgeZoneC = completeGraphEdgeGen('ZoneC',loaded)
    
    edgeData = [edgeZoneA, edgeZoneB, edgeZoneC]

    for i in range(len(fileName)):
        createFile(fileName[i], edgeData[i])
    
def exportDistPathMatrix():

    zones = ["ZoneA", "ZoneB", "ZoneC"]
    
    for i in zones:
        distPath = floydWarshall(testAdjMatrix(i)[1])
        distFileName = i + "_DistMatrix" # ZoneA_DistMatrix.json
        pathFileName = i + "_PathMatrix" # ZoneA_PathMatrix.json
        createFile(distFileName, distPath[0])
        createFile(pathFileName, distPath[1])


def testEdgeExistence():
    
    # Running the test to see if there is edges being produced
    for i in range(len(fileName)):
        with open("Data/{}.json".format(fileName[i])) as testfile:
            loaded = json.load(testfile)

        for i in loaded:
            print(i)

def testAdjMatrix(zone):
    graphMatrix = edgeListToAdjMatrix(zone)
    return graphMatrix

def testFloydWarshall(zone):

    distPath = floydWarshall(testAdjMatrix(zone)[1])

    # print(distPath[0])
    print(distPath[1])

    return 1

def preprocessing():
    exportEdge()
    testEdgeExistence()

# preprocessing()
# testAdjMatrix("ZoneA")
# testFloydWarshall("ZoneA")
# exportDistPathMatrix()
#  (Greedy BFS) for 3 options (2.4km, 5km and 10km)
# preprocessing for 2.4, 5 and 10
# # distance space o(V^2) * 3
# # path array space o(v^2) * 3