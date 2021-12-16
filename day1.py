
# Standard radar of the submarine, for part a of the puzzle.
def radar(sweepReport):
    isIncreasedTimes = 0
    #sweepReport = sweepReport.split("\n")
    lastSweep = sweepReport.pop(0)
    for currentSweep in sweepReport:
        if int(currentSweep) > int(lastSweep):
            isIncreasedTimes += 1
        lastSweep = currentSweep
    return isIncreasedTimes;

# The improved radar of the submarine, for part b of the puzzle.
def improvedRadar(sweepReport):
    isIncreasedTimes = 0
    #sweepReport = sweepReport.split("\n")

    lastSweep = sweepReport[0] + sweepReport[1] + sweepReport[2]
    sweepReport.pop(0)
    l = len(sweepReport)

    for i, currentSweep in enumerate(sweepReport):

        # Catch index error
        if i + 2 == l:
            break

        computeSweep = sweepReport[i] + sweepReport[i + 1] + sweepReport[i + 2]
        if computeSweep > lastSweep:
            isIncreasedTimes += 1
        lastSweep = computeSweep

    return isIncreasedTimes

# Parse input.
with open("day1input.txt", "r") as input_data:
    sweepReport = input_data.read()
    sweepReport = sweepReport.split("\n")
    for i, sweep in enumerate(sweepReport):
        sweepReport[i] = int(sweep)

print("You read the radar. The sea floor depth increased {} times".format(radar(sweepReport)))
print("Oh, no! The improved radar shows a higher value: the floor depth increased {} times.".format(improvedRadar(sweepReport)))