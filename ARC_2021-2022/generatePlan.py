import os

waypoint = open('waypoint_1.txt') #Change to "with"
lines = waypoint.readlines()
coordinates = [] #for each index, 1 = lat ,2 = long, 3 = alt, 4 = type
lines.remove('\n') #Removing extraneous lines

top_plate = ""
bottom_plate = ""


for line in lines:
    split = line.split() #Splits lines by spaces
    coordinates.append([split[0], split[2], split[4], split[5]])

# home_coordinates =

print(coordinates)


#this will generate an mission object type based on the 4th value of the input indices

def generateObject(coordinates, action): #CHANGE DOJUMPID FOR EACH THING
    wp_type = coordinates[3] #maybe no remove for this one?
    altitude = coordinates[2].remove('\'')
    latitude = coordinates[0].remove('\'')
    longitude = coordinates[1].remove('\'')
    if(action == "loiter"): #Loiter object; what are the parameters                                                                                            This doJumpId thing has to be iterated for each object we create; param 1 is time, idk what the others
        return "{\"AMSLAltAboveTerrain\": null,\n\"Altitude\": " + altitude + ",\n\"AltitudeMode\": 1,\n\"autoContinue\": true,\n\"command\": 19, \n\"doJumpId\": 2,\n\"frame\": 3,\n\"params\": [\n30,\n1,\n50,\n1,\n" + latitude +",\n" + longitude +",\n" + altitude + "\n],\n\"type\": \"SimpleItem\"\n},"
    elif(action == "waypoint"): #Generic Waypoint
        return "{\"AMSLAltAboveTerrain\": null,\n\"Altitude\": " + altitude + ",\n\"AltitudeMode\": 1,\n\"autoContinue\": true,\n\"command\": 16, \n\"doJumpId\": 2,\n\"frame\": 3,\n\"params\": [\n0,\n0,\n0,\nnull,\n" + latitude + ",\n" + longitude + ",\n" + altitude + "\n],\n\"type\": \"SimpleItem\"\n},"
    elif(action == "takeoff"): # Waypoint when taking off
        return "{\"AMSLAltAboveTerrain\": null,\n\"Altitude\": " + altitude + ",\n\"AltitudeMode\": 1,\n\"autoContinue\": true,\n\"command\": 22, \n\"doJumpId\": 2,\n\"frame\": 3,\n\"params\": [\n0,\n0,\n0,\nnull,\n" + latitude + ",\n" + longitude + ",\n" + altitude + "\n],\n\"type\": \"SimpleItem\"\n},"



print(generateObject(coordinates[1]))
