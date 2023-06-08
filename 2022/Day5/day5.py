# Function to reverse first i elements of a given list
def reverse_first_i(lst, i):
    if i < 0 or i > len(lst):
        raise ValueError("i is out of range")
    lst[:i] = reversed(lst[:i])

# Function for part 1
def suffling1(a,b,c):
    temp=[]
    for i in range(a):
        stacks[c-1].insert(0,stacks[b-1][0])
        stacks[b-1].remove(stacks[b-1][0])

# Function for part 2
def suffling2(a,b,c):
    temp=[]
    for i in range(a):
        stacks[c-1].insert(0,stacks[b-1][0])
        stacks[b-1].remove(stacks[b-1][0])
    reverse_first_i(stacks[c-1],a)
        
# Processing data
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

# Calling function to solve part 1
for i in inputvals:
    suffling1(i[0],i[1],i[2])

# Priting answer for part 1
print("Part1:")
for i in stacks:
    print(i[0])
print("\n")

# Processing data again since we changed it in part 1
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

# Calling function to solve part 2
for i in inputvals:
    suffling2(i[0],i[1],i[2])
# Printing Answer to part 2
print("Part2:")
for i in stacks:
    print(i[0])
