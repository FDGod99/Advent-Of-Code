#Taking inputs
inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/2018/day1_2018.txt", "r")

#part1
new = []
for i in inputfile:
    new.append(int(i))

# ans = 0
# for j in new:
#     ans = ans + j

# print(ans)


#part2
new = new*100
#print(new)
#ar1 = [+3, +3, +4, -2, -4]
#ar1 = ar1+ar1
summ=0
sumans = [0]
for i in new:
    summ = summ + i
    sumans.append(summ)


helper=[]
for x in sumans:
    if x in helper:
        print(x)
        break
    else:
        helper.append(x)     

#print(helper)