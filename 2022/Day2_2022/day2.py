inputfile = open("day2.txt")

score=0
''' part 1
for i in inputfile:
    if (i[0]=="A" and i[2]=="X"):
        score = score+4
    if i[0]=="A" and i[2]=="Y":
        score = score+8
    if i[0]=="A" and i[2]=="Z":
        score = score+3
    if i[0]=="B" and i[2]=="X":
        score = score+1
    if i[0]=="B" and i[2]=="Y":
        score = score+5
    if i[0]=="B" and i[2]=="Z":
        score = score+9
    if i[0]=="C" and i[2]=="X":
        score = score+7
    if i[0]=="C" and i[2]=="Y":
        score = score+2
    if i[0]=="C" and i[2]=="Z":
        score = score+6
'''

#part2

for i in inputfile:
    if (i[0]=="A" and i[2]=="X"):
        score = score+3
    if i[0]=="A" and i[2]=="Y":
        score = score+4
    if i[0]=="A" and i[2]=="Z":
        score = score+8
    if i[0]=="B" and i[2]=="X":
        score = score+1
    if i[0]=="B" and i[2]=="Y":
        score = score+5
    if i[0]=="B" and i[2]=="Z":
        score = score+9
    if i[0]=="C" and i[2]=="X":
        score = score+2
    if i[0]=="C" and i[2]=="Y":
        score = score+6
    if i[0]=="C" and i[2]=="Z":
        score = score+7
print(score)

