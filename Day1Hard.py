


def getRepeatFreq():
    frequency = 0
    frequencyList = []
    notFound = True
    while(notFound):
        for line in open("Day1.txt", 'r'):
            if line.strip():
                if (line[0] == '+'):
                    frequency += int(line[1:])
                elif (line[0] == '-'):
                    frequency -= int(line[1:])
            if frequency in frequencyList:
                return frequency
            else:
                frequencyList.append(frequency)
                #print(frequencyList)


print(getRepeatFreq())