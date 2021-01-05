

path = "test1.txt"



asteroids = {}

with open(path) as file:
    j = 0
    for line in file:
        for i in range(len(line)):
            if line[i] == '#':
                asteroids[i,j] = "#"
        j +=  1

print(asteroids)

