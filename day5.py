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

inputfile = open('day5.txt')
inputvals=[]
for i in inputfile:
    if i[0]=='m':
        empty=[]
        a = i.split(" ")
        empty.append(int(a[1]))
        empty.append(int(a[3]))
        empty.append(int(a[5]))
        inputvals.append(empty)

print(inputvals)
