#Taking inputs
inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/2019/day2_2019.txt", "r")

#Creating Array from txt file
input_array = []
for i in inputfile:
    input_array = i
input_array = input_array.split(",")
input_array = [int(element) for element in input_array]
input_array[1] = 12
input_array[2] = 2

#Solving the problem
counter = 0
flag = 0

while flag!=1:
    if input_array[counter]==99:
        flag=1
    elif input_array[counter]==1:
        input_array[input_array[counter+3]] =input_array[input_array[counter+1]]+input_array[input_array[counter+2]]
        counter = counter+4
    elif input_array[counter]==2:
        input_array[input_array[counter+3]] =input_array[input_array[counter+1]]*input_array[input_array[counter+2]]
        counter = counter+4

#Priting required answer
print(input_array[0])