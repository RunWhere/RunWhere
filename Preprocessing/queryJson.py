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


testZone('ZoneC')
# print(distance(loaded['ZoneA'][0]['latitude'], loaded['ZoneA'][0]['longitude'], loaded['ZoneA'][1]['latitude'], loaded['ZoneA'][1]['longitude']))