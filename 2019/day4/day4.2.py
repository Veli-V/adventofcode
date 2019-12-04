#It is a six-digit number.
#The value is within the range given in your puzzle input.
#Two adjacent digits are the same (like 22 in 122345).
#Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
#An Elf just remembered one more important detail: 
#the two adjacent matching digits are not part of a larger group of matching digits.

#Range for challenge:
minValue = 240298
maxValue = 784956

# 981 is too high

#minValue = 111111
#maxValue = 111129

def checkPassword( ps ):
    double = False
    increase = True
    oldi = 0
    oldii = 0
    for i in ps:
        if int(i) < oldi:
            increase = False
            print("ei ok, koska pienenee: " + str(ps))
            break
        oldi = int(i)

    sameCount = 0
    if increase:
        oldi = 0
        for i in ps:
            for p in ps:
                if i == p:
                    sameCount += 1
            if sameCount == 2:
                double = True
            sameCount = 0

    if double and increase:
        return(True)
    else:
        return(False)


okPasswords = 0
for i in range(minValue, maxValue):
    if checkPassword(str(i)):
        print("salasana ok: " + str(i))
        okPasswords += 1
print("Ok salasanoja oli: " + str(okPasswords))


#ps = ''
#while True:
    #ps = input()
    #if checkPassword(ps):
        #print("salasana ok: " + ps)
    #else:
        #print("salasna ei ok: " +ps)
