import sys

path = "input.txt"
maxX = 100000
maxY = 100000
willPrint = 1023

#coords = [['.' for col in range(maxX)] for row in range(maxY)]
#coords1 = []
#coords2 = []

dict1 = {'0,0': 1}
dict2 = {'0,0': 1}
def printCoords():
    if willPrint == 1:
        print(dict1)
        print(dict2)
    else:
        return()


printCoords()
i = 0
j = 0

counter = 0
with open(path) as f:
    line = f.readline()
    line = line.split(",")
    for l in line:
        if l[0] == 'R':
            l = l[1 : : ]
            for x in range(int(l)):
                    #coords[i][j] = '#'
                    #coords1.append([i,j])
                    dict1[str(i) + ',' + str(j)] = counter
                    counter += 1
                    j += 1
        if l[0] == 'U':
            l = l[1 : : ]
            for x in range(int(l)):
                    #coords[i][j] = "#"
                    #coords1.append([i,j])
                    dict1[str(i) + ',' + str(j)] = counter
                    counter += 1
                    i += 1
        if l[0] == 'D':
            l = l[1 : : ]
            for x in range(int(l)):
                    #coords[i][j] = "#"
                    #coords1.append([i,j])
                    dict1[str(i) + ',' + str(j)] = counter
                    counter += 1
                    i -= 1
        if l[0] == 'L':
            l = l[1 : : ]
            for x in range(int(l)):
                    #coords[i][j] = "#"
                    #coords1.append([i,j])
                    dict1[str(i) + ',' + str(j)] = counter
                    counter += 1
                    j -= 1
    printCoords()
    i = 0
    j = 0
    counter = 0
    line = f.readline()
    line = line.split(",")
    for l in line:
        if l[0] == 'R':
            l = l[1 : : ]
            for x in range(int(l)):
                    #coords[i][j] = '+'
                    #coords2.append([i,j])
                    dict2[str(i) + ',' + str(j)] = counter
                    counter += 1
                    j += 1

        if l[0] == 'U':
            l = l[1 : : ]
            for x in range(int(l)):
                    #coords[i][j] = '+'
                    #coords2.append([i,j])
                    dict2[str(i) + ',' + str(j)] = counter
                    counter += 1
                    i += 1
        if l[0] == 'D':
            l = l[1 : : ]
            for x in range(int(l)):
                    #coords[i][j] = '+'
                    #coords2.append([i,j])
                    dict2[str(i) + ',' + str(j)] = counter
                    counter += 1
                    i -= 1
        if l[0] == 'L':
            l = l[1 : : ]
            for x in range(int(l)):
                    #coords[i][j] = '+'
                    #coords2.append([i,j])
                    dict2[str(i) + ',' + str(j)] = counter
                    counter += 1
                    j -= 1

printCoords()

minDistance = sys.maxsize

# lasketaan etäisyydet
#for i in range(maxX):
    #for j in range(maxY):
        #if coords[i][j] == '0' and i != 0 and j != 0:
            #distance = i + j
            #print("löytyi, etäisyys on: " + str(distance))
            #if distance < minDistance:
                #minDistance = distance
#for i in coords1:
    #for j in coords2:
        #if j == i:
            #distance = j[0] + j[1]
            #print("löytyi, etäisyys on: " + str(distance))
            #if distance < minDistance:
                #minDistance = distance

#for i in coords1:
    #try:
        #coords2.index(i)
        #distance = i[0] + i[1]
        #print("löytyi, etäisyys on: " + str(distance) + " pienin nyt on: " + str(minDistance))
        #if distance < minDistance and distance != 0:
            #minDistance = distance
    #except ValueError:
        #continue

for i in dict1:
    try:
        distance = dict2[i] + dict1[i]
        print("löytyi, etäisyys on: " + str(distance) + " pienin nyt on: " + str(minDistance))
        print("tämä pisteessä; " + str(i))
        if distance < minDistance and distance != 0:
            minDistance = distance
    except KeyError:
        continue
        
print("minimi etäysyys on: " + str(minDistance))
