import os
from itertools import permutations
import math

top_plate = "{\n\"fileType\": \"Plan\",\n\"geoFence\": {\n\"circles\": [\n],\n\"polygons\": [\n],\n\"version\": 2\n},\n\"groundStation\": \"QGroundControl\",\n\"mission\": {\n\"cruiseSpeed\": 15,\n\"firmwareType\": 12,\n\"globalPlanAltitudeMode\": 1,\n\"hoverSpeed\": 5,\n\"items\": ["

waypoint = open('WORK.txt') #Change to "with"
lines = waypoint.readlines()
coordinates = [] #for each index, 1 = lat ,2 = long, 3 = alt, 4 = type
lines.remove('\n') #Removing extraneous lines
waypoint.close()

for line in lines:
    split = line.split() #Splits lines by spaces
    coordinates.append([split[0], split[2], split[4], split[5]])

# Finds index of home coordinate
def search_home():
    for x in coordinates:
        if coordinates[coordinates.index(x)][3] == 'H':
            return coordinates[coordinates.index(x)]

home_set = search_home() # Remove apostrophes from this

# O(n!) time complexity...  potentially use a different algo.
def optimize_path():
    # First, create a set of all possible paths
    # Then , Calculate net distance for each path
    # Finally, Compare net distance between each thing
    path = [[]]
    k = 0
    hx = float(home_set[0])
    hy = float(home_set[1])
    # Next part is a bit sketchy
    # xy = [[coordinates[1][0], coordinates[1][1]], [coordinates[2][0], coordinates[2][1]], [coordinates[3][0], coordinates[3][1]], [coordinates[4][0], coordinates[4][1]]]
    xy = [coordinates[1], coordinates[2], coordinates[3], coordinates[4]]

    #xy = coordinates
    points = permutations([xy[0], xy[1], xy[2], xy[3]], 4)
    for p in list(points):
        # is there a way to shorten the following mess... After some reasearch this is probably the easiest way
        px0 = float(p[0][0].replace("'", ""))
        py0 = float(p[0][1].replace("'", ""))
        px1 = float(p[1][0].replace("'", ""))
        py1 = float(p[1][1].replace("'", ""))
        px2 = float(p[2][0].replace("'", ""))
        py2 = float(p[2][1].replace("'", ""))
        px3 = float(p[3][0].replace("'", ""))
        py3 = float(p[3][1].replace("'", ""))
        # Comparing distances
        distance = math.dist([hx, hy], [px0, py0]) + math.dist([px0, py0], [px1, py1]) + math.dist([px1, py1], [px2, py2]) + math.dist([px2, py2], [px3, py3]) + math.dist([px3, py3], [hx, hy])
        if (distance < k) or (k == 0):
            k = distance
            path = p
    # Changing tuple to list so that it is mutable
    lpath = [path[0], path[1], path[2], path[3]]
    lpath.insert(0, home_set)
    lpath.append(home_set)

    return lpath


# Variable containing better coordinate list
fast_path = optimize_path()


# Loop through each waypoint, add waypoint text file based on type
def generate_plan(file):
    f = open(file, "x")
    f.write(top_plate)
    i = 0
    for y in list(fast_path):
        i += 1
        if y == fast_path[0] and i == 1: # Maybe 1?
            f.write(generateObject(y, "takeoff", i))
        elif y[3] == 'A' or y[3] == 'B':
            f.write(generateObject(y, "waypoint", i))
        elif y[3] == 'C':
            f.write(generateObject(y, "loiter", i))
        elif y[3] == 'H' and i > 1:
            break
        f.write(",")
    f.write(generateObject(fast_path[0], "bottom", 0))


# This will generate an mission object type based on the 4th value of the input indices
def generateObject(coordinates, action, id): #CHANGE DOJUMPID FOR EACH THING
    wp_type = coordinates[3] #maybe no remove for this one?
    altitude = coordinates[2].replace("'", "")
    latitude = coordinates[0].replace("'", "")
    longitude = coordinates[1].replace("'", "")
    if(action == "loiter"): #Loiter object; what are the parameters                                                                                            This doJumpId thing has to be iterated for each object we create; param 1 is time, idk what the others
        return "{\"AMSLAltAboveTerrain\": 50,\n\"Altitude\": " + str(altitude) + ",\n\"AltitudeMode\": 1,\n\"autoContinue\": true,\n\"command\": 19, \n\"doJumpId\":" + str(id) + ",\n\"frame\": 3,\n\"params\": [\n30,\n1,\n50,\n1,\n" + str(latitude) +",\n" + str(longitude) +",\n" + str(altitude) + "\n],\n\"type\": \"SimpleItem\"\n}"
    elif(action == "waypoint"): #Generic Waypoint
        return "{\"AMSLAltAboveTerrain\": 50,\n\"Altitude\": " + str(altitude) + ",\n\"AltitudeMode\": 1,\n\"autoContinue\": true,\n\"command\": 16, \n\"doJumpId\":" + str(id) + ",\n\"frame\": 3,\n\"params\": [\n0,\n0,\n0,\nnull,\n" + str(latitude) + ",\n" + str(longitude) + ",\n" + str(altitude) + "\n],\n\"type\": \"SimpleItem\"\n}"
    elif(action == "takeoff"): # Waypoint when taking off
        return "{\"AMSLAltAboveTerrain\": 50,\n\"Altitude\": " + str(altitude) + ",\n\"AltitudeMode\": 1,\n\"autoContinue\": true,\n\"command\": 22, \n\"doJumpId\":" + str(id) + ",\n\"frame\": 3,\n\"params\": [\n0,\n0,\n0,\nnull,\n" + str(latitude) + ",\n" + str(longitude) + ",\n" + str(altitude) + "\n],\n\"type\": \"SimpleItem\"\n}"
    elif(action == "servo"): #Use servo to drop egg or something; change off of placeholder at some point
        return "Placeholder"
    elif (action == "bottom"):#Last object in .plan file; necessary to land         
        return "{\"autoContinue\": true,\n\"command\": 20,\n\"doJumpId\": 7,\n\"frame\": 2,\n\"params\": [\n0,\n0,\n0,\n0,\n0,\n0,\n0\n],\n\"type\": \"SimpleItem\"\n}\n],\n\"plannedHomePosition\":[\n" + str(latitude) + ",\n" + str(longitude) + ",\n102.72507599995788\n],\n\"vehicleType\": 2,\n\"version\": 2\n},\n\"rallyPoints\": {\n\"points\": [\n],\n\"version\": 2\n},\n\"version\": 1\n}"
    else:
        return "ERROR: INVALID INPUT"

generate_plan("THISWILLWORK.plan")




