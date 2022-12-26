one=['R','C','H']
two=['F','S','L','H','J','B']
three=['Q','T','J','H','D','M','R']
four=['J','B','Z','H','R','G','S']
five=['B','C','D','T','Z','F','P','R']
six=['G','C','H','T']
seven=['L','W','P','B','Z','V','N','S']
eight=['C','G','Q','J','R']
nine=['S','F','P','H','R','T','D','L']
stacks = [one,two,three,four,five,six,seven,eight,nine]

inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/Day5/day5.txt")
inputvals=[]
for i in inputfile:
    if i[0]=='m':
        empty=[]
        a = i.split(" ")
        empty.append(int(a[1]))
        empty.append(int(a[3]))
        empty.append(int(a[5]))
        inputvals.append(empty)
        

for i in inputvals:
    print(inputvals)

def reverse_first_i(lst, i):
    # Check if the value of i is within the valid range
    if i < 0 or i > len(lst):
        raise ValueError("i is out of range")

    # Reverse the first i elements of the list
    lst[:i] = reversed(lst[:i])

# stacks = [['n','z'],['d','c','m'],['p']]
# inputvals = [[1,2,1],[3,1,3],[2,2,1],[1,1,2]]

def suffling(a,b,c):
    temp=[]
    for i in range(a):
        stacks[c-1].insert(0,stacks[b-1][0])
        stacks[b-1].remove(stacks[b-1][0])
    reverse_first_i(stacks[c-1],a)
        


def part2(a,b,c):
    for i in range(a):
        temp=[]
        temp.insert(0,stacks[b-1][0])
        stacks[b-1].remove(stacks[b-1][0])
    
    stacks[c-1] = temp + stacks[c-1]


for i in inputvals:
    suffling(i[0],i[1],i[2])

# for i in inputvals:
#     part2(i[0],i[1],i[2])

print(stacks)
for i in stacks:
    print(i[0])
