#Taking inputs
inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/2021/day_2021.txt", "r")

#Creating Array from txt file
input_array = []
for i in inputfile:
    input_array.append(int(i))

#Solving the problem
counter = 0
for i in range(len(input_array)-1):
    if input_array[i]<input_array[i+1]:
        counter=counter+1
print(counter)
