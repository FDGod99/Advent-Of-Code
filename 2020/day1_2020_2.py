#Taking inputs
inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/2020/day1_2020.txt", "r")

#Creating Array from txt file
input_array = []
for i in inputfile:
    input_array.append(int(i))

#Solving the problem
for i in range(len(input_array)):
    for j in range(len(input_array)):
        for k in range(len(input_array)):
            if input_array[i]+input_array[j]+input_array[k]== 2020:
                print(input_array[i]*input_array[j]*input_array[k])
                break

        