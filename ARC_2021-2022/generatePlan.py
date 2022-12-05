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
    wp_type = coordinates[3]
    if (wp_type == 'H'):
        #home code
    elif(wp_type == 'A'):\
        )
    elif(wp_type == 'B')
        #Loiter?
    elif(wp_type == 'C'):
        #other thing?
    else:
        #error
