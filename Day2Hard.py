
toFind = ""
count = 0
for line in open("Day2.txt", 'r'):
    for checkLine in open("Day2.txt", 'r'):
        for i in range (len(line)):
            if(not(line[i]  == checkLine[i])):
                count += 1
        if(count == 1):
            for i in range (len(line)):
                if(line[i] == checkLine[i]):
                    toFind += line[i]
            print(toFind)
        toFind = ""
        count = 0
