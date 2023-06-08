#Taking inputs
inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/2015/day1_2015.txt", "r")

#part1
counter = 0
for i in inputfile:
    for j in i:
        if j=='(':
            counter = counter + 1
        elif j==')':
            counter = counter - 1
#print(counter)

#part2
counter = 0
counter2 = 0
for i in inputfile:
    for j in i:
        if counter == -1:
            break
        else:
            counter2 = counter2 + 1
            if j=='(':
                counter = counter + 1
            elif j==')':
                counter = counter - 1

#print(counter2)
