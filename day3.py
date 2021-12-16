def getPowerConsumption(data):
    gamma = ""
    epsilon = ""
    readings = [0] * 12

    for date in data:
        for i, r in enumerate(date):
            readings[i] += int(r)

    for read in readings:
        if read > len(data) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)

def getLifeSupport(data, isOx):
    for i in range(0, len(data[0])):

        testBit = 0
        for date in data:
            testBit += int(date[i])
        if testBit >= len(data) / 2:
            if isOx: testBit = 1
            else: testBit = 0
        else:
            if isOx: testBit = 0
            else: testBit = 1

        sortedOut = []
        for d, date in enumerate(data):
            if int(date[i]) != testBit:
                sortedOut.append(date)
        for out in sortedOut:
            if len(data) == 1:
                break
            data.remove(out)
    return data[0]

with open("day3input.txt", "r") as input_data:
    data = input_data.read()
    data = data.split()

ox = getLifeSupport(data.copy(), True)
oc = getLifeSupport(data.copy(), False)
power = getPowerConsumption(data)

print("The diagnostics of the submarine come in. You read them:")
print("Power consumption is at: {}".format(power))
print("Life support is at: {}".format(int(ox, 2) * int(oc, 2)))
print("Thats good ... you guess.")


