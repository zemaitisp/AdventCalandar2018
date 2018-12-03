
frequency = 0

for line in open("Day1.txt", 'r'):
    if line.strip():
        if(line[0] == '+'):
            frequency += int(line[1:])
        elif(line[0] == '-'):
            frequency -= int(line[1:])

print(frequency)