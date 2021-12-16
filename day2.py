def driveCommand(commandList):
    forward = 0
    depth = 0

    for command in commandList:
        if command[0] == "forward":
            forward += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])

    return forward, depth

def improvedDriveCommand(commandList):
    forward = 0
    depth = 0
    aim = 0

    for command in commandList:
        if command[0] == "forward":
            forward += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])

    return forward, depth

# Parse input.
with open("day2input.txt", "r") as input_data:
    commandList = input_data.read()
    commandList = commandList.split("\n")
    for i, command in enumerate(commandList):
        commandList[i] = command.split()


position = driveCommand(commandList)
positionBetter = improvedDriveCommand(commandList)

print("You drive the submarine deeper into the ocean. After some time you read your position, i is {}.".format(position[0] * position[1]))
print("Damn it, something was wrong, you computed the position again. Now it is: {}.".format(positionBetter[0] * positionBetter[1]))