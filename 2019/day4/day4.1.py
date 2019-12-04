#It is a six-digit number.
#The value is within the range given in your puzzle input.
#Two adjacent digits are the same (like 22 in 122345).
#Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

#Range for challenge:
minValue = 240298
maxValue = 784956

#minValue = 111111
#maxValue = 222222

def checkPassword( ps ):
    double = False
    increase = True
    oldi = 0
    for i in ps:
        if int(i) < oldi:
            increase = False
            break
        oldi = int(i)

    for i in ps:
        if i == oldi:
            double = True
            break
        oldi = i

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
