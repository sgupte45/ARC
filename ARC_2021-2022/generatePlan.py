import os

waypoint = open('waypoint_1.txt')
lines = waypoint.readlines()
coordinates = [] #for each index, 1 = lat ,2 = long, 3 = alt, 4 = type
lines.remove('\n') #Removing extraneous lines


for line in lines:
    split = line.split() #Splits lines by spaces
    coordinates.append([split[0], split[2], split[4], split[5]])

print(coordinates)




#this will generate an mission object type based on the 4th value of the input indices

def generateObject(coordinates): #maybe add a switch case for each mission object type
    wp_type = coordinates[3] #maybe no remove for this one?
    altitude = coordinates[2].remove('\'')
    latitude = coordinates[0].remove('\'')
    longitude = coordinates[1].remove('\'')
    if(wp_type == 'A'): #Loiter object
        return "{\"AMSLAltAboveTerrain\": null,\n\"Altitude\": " + altitude + ",\n\"AltitudeMode\": 1,\n\"autoContinue\": true,\n\"command\": 19, \n\"doJumpId\": 2,\n\"frame\": 3,\n\"params\": [\n30,\n1,\n50,\n1,\n" + latitude +",\n" + longitude +",\n3.048\n],\n\"type\": \"SimpleItem\"\n},"


print(generateObject(coordinates[1]))
