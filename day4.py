def checkFirstBingo(allBingos, winnigNumbers):
    for i, number in enumerate(winnigNumbers):

        checkNumbers = set(winnigNumbers[0:i+1])

        for bingo in allBingos:
            for line in bingo:

                lineSet = set(line) - checkNumbers
                if len(lineSet) == 0:
                    return calculateBingo(bingo, checkNumbers, number)


def checkLastBingo(allBingos, winnigNumbers):
    doneBingos = set()

    for i, number in enumerate(winnigNumbers):

        checkNumbers = set(winnigNumbers[0:i+1])

        for k, bingo in enumerate(allBingos):
            if k in doneBingos:
                continue

            for line in bingo:

                lineSet = set(line) - checkNumbers
                if len(lineSet) == 0:
                    doneBingos.add(k)
                    if len(doneBingos) == len(allBingos):
                        return calculateBingo(bingo, checkNumbers, number)


def calculateBingo(bingo, checkNumbers, number):
    sum = 0
    for l, line in enumerate(bingo):

        # To take only the nec
        if l >= 5:
            bingo.pop(l)
            continue

        for d, digit in enumerate(line):
            if digit not in checkNumbers:
               sum += int(bingo[l][d])

    return sum * int(number)

with open("day4input.txt", "r") as input_data:
    data = input_data.read()
    data = data.split("\n")

    # Parsing the winning numbers.
    winningNumbers = data.pop(0)
    winningNumbers = winningNumbers.split(",")
    data.pop(0)

    # Parsing the bingos.
    allBingos = []
    aBingo = []
    for line in data:
        if line != "":
            aBingo.append(line.split())
        else:
            allBingos.append(aBingo)
            aBingo = []

    for i, bingo in enumerate(allBingos):
        extBingo = [[], [], [], [], []]
        for l in range(0, 5):
            for d in range(0, 5):
                extBingo[l].append(bingo[d][l])
        allBingos[i].extend(extBingo)

print(checkFirstBingo(allBingos, winningNumbers))
print(checkLastBingo(allBingos, winningNumbers))