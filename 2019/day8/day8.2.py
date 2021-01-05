

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
talsirivi = []
for i in range(0, height*width):
    print(i)
    for l in layers:
        print(l)
        if l[i] != '2':
            talsirivi.append(l[i])
            break

    
print(talsirivi)
#talsirivi = "100100110010010111100110010100100101001000010100101100010010100100010010010101001111010010010001111010100100101001010000100101001010010011001111010010"

for i in range(height):
    for j in range(width):
        #print(talsirivi[i*width+j], end='')
        if talsirivi[i*width+j] == '0':
            print(' ', end='')
        elif talsirivi[i*width+j] == '1':
            print('#', end='')
        else:
            print('. ', end='')
    print()


   ###  ## ###     #    #
 ## # ## # ###  #### ####
   ## ##### # #   ##   ##
 ## # ###### ## #### ####
 ## # ## ### ## #### ####
   ###  #### ##    # ####

