def createField(x, y):
    field = []
    line = ""
    for i in range(0, x):
        line += ". "
    for i in range(0, y):
        field.append(line.split())
    return field

def printField(field):
    for l in field:
        print("".join(l))

def drawVerticalHorizontal(field, data):
    #printField(field)

    for line in data:

        if line[0][0] == line[1][0]:
            start = line[0][1]
            end = line[1][1]
            constant = line[0][0]
        else:
            continue

        if start > end:
            t = end
            end = start
            start = t

        while start != end + 1:
            if field[start][constant] == "|":
                field[start][constant] = "+"
            else:
                field[start][constant] = "|"
            start += 1

    for line in data:

        if line[0][1] == line[1][1]:
            start = line[0][0]
            end = line[1][0]
            constant = line[0][1]
        else:
            continue

        if start > end:
            t = end
            end = start
            start = t

        while start != end + 1:
            if field[constant][start] == ".":
                field[constant][start] = "-"
            else:
                field[constant][start] = "+"
            start += 1

    cross = 0
    for line in field:
        for xy in line:
            if xy == "+":
                cross += 1
    #printField(field)
    return cross


#ef get value

# Parse data
with open("day5input.txt", "r") as input_data:
    data = input_data.read()
    data = data.split("\n")

    maxX = 0
    maxY = 0

    for i, date in enumerate(data):
        aLine = date.split(" -> ")
        for k, xy in enumerate(aLine):
            xy = xy.split(",")
            x = int(xy[0])
            y = int(xy[1])
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
            aLine[k] = [x, y]
        data[i] = aLine


field = createField(maxX + 1, maxY + 1)
print(drawVerticalHorizontal(field, data))