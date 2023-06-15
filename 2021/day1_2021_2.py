#Taking inputs
inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/2021/day_2021.txt", "r")

#Creating Array from txt file
input_array = []
for i in inputfile:
    input_array.append(int(i))

#Solving the problem
counter = 0
new_array = []
for i in range(len(input_array)-2):
    new_array.append(input_array[i]+input_array[i+2]+input_array[i+1])

for x in range(len(new_array)-1):
    if new_array[x]<new_array[x+1]:
        counter=counter+1
print(counter)
