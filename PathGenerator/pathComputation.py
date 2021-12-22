import json

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
    # userDistanceOption (3 options: 2.4, 5 and 10km)
    
    while(True):
        
        if userDistanceOption == 1:
            # access FW-generated matrix
            dist = 1.2
            ## Searching for distMatrix and retrieve top 3 paths and return
        elif userDistanceOption == 2:
            dist = 2.5
            
        else:
            dist = 5.0

    # iterate floyd warhsall distance matrix
    # find out those distances that meets the userDist
    endLocation

    for loadedVert

    # then we iterate the path matrix
    # return 3 paths sorted by |dist - userDist| -> 0
