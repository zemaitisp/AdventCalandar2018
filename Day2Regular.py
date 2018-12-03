twoLetters = 0
threeLetters = 0
count = 0
foundTwo = True
foundThree = True

for line in open("Day2.txt", 'r'):
    if line.strip():
        for letter in line:
            count = line.count(letter)
            if(count == 2 and foundTwo):
                foundTwo = False
                twoLetters += 1
            if(count == 3 and foundThree):
                foundThree = False
                threeLetters += 1
            count = 0
    foundThree = True
    foundTwo = True

print(twoLetters * threeLetters)
