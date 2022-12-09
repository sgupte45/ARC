import os



top_plate = "{\n\"fileType\": \"Plan\",\n\"geoFence\": {\n\"circles\": [\n],\n\"polygons\": [\n],\n\"version\": 2\n},\n\"groundStation\": \"QGroundControl\",\n\"mission\": {\n\"cruiseSpeed\": 15,\n\"firmwareType\": 12,\n\"globalPlanAltitudeMode\": 1,\n\"hoverSpeed\": 5,\n\"items\": ["

waypoint = open('waypoint_1.txt') #Change to "with"
lines = waypoint.readlines()
coordinates = [] #for each index, 1 = lat ,2 = long, 3 = alt, 4 = type
lines.remove('\n') #Removing extraneous lines
waypoint.close()

for line in lines:
    split = line.split() #Splits lines by spaces
    coordinates.append([split[0], split[2], split[4], split[5]])




def generate_plan():
    f = open("test7.plan", "x")
    f.write(top_plate)
    f.write(generateObject(coordinates[0], "takeoff", 1))
    f.write(",")
    f.write(generateObject(coordinates[1], "waypoint", 2))
    f.write(",")
    f.write(generateObject(coordinates[2], "loiter", 3))
    f.write(",")
    f.write(generateObject(coordinates[3], "bottom", 0))


#this will generate an mission object type based on the 4th value of the input indices

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

generate_plan()




