

path = "input.txt"
height = 6
width = 25
inputFile = open(path)
line = inputFile.readline()

print(line)

def countResult(layer):
    ones = 0
    twos = 0
    zeros = 0
    for c in layer:
        if c == '1':
            ones += 1
        elif c == '2':
            twos += 1
        elif c == '0':
            zeros += 1
    print("Ones:Twos:zeros " + str(ones) + ":" + str(twos) + ":" + str(zeros))
    return zeros, ones * twos


layers = []

for i in range(0, len(line)-1, width*height):
    layer = line[i:i+(width*height)]
    layers.append(layer)

mostZeros, biggestResult = height*width, 0
talsirivi = ""
for l in layers:
    print(l)
    zeros, result = countResult(l)
    if zeros < mostZeros:
        mostZeros = zeros
        biggestResult = result
        talsirivi = l

print("Tulos: " + str(biggestResult))
print(talsirivi)


