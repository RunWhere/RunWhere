import json
from math import asin, cos, radians, sin, sqrt

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
    
with open("Data/verticles_edges.json") as data:
    loaded = json.load(data)

def testZone(zone):
    for i in loaded[zone]:
        print(i['name'])
        print(i['latitude'])
        print(i['longitude'])


# Step 1 -> Form complete graph for each zone
# store all of the complete graph in an edgelist
# edgeListZoneA = [
#     ["ZoneA","Faculty of Engineering","Temasek Lab",dist],
# ]
# Step 2
# We select edges. + (BFS)

# step 3 (Run Floyd Warshall)
## distance space o(V^2) * 3
## path array space o(v^2) * 3

row = [
    [["Faculty of Engineering",0],["Temasek Lab", 0.18]], 
    [["Faculty of Engineering",0.18],["Temasek Lab", 0]]
]

with open("Data/test.json", 'w') as outfile:
    print(json.dump(row, outfile))


# testZone('ZoneC')
# print(distance(loaded['ZoneA'][0]['latitude'], loaded['ZoneA'][0]['longitude'], loaded['ZoneA'][1]['latitude'], loaded['ZoneA'][1]['longitude']))