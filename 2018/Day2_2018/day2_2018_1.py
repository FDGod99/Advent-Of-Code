#Taking inputs
inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/2018/day2_2018.txt", "r")

#Creating Array from txt file
input_array = []
for i in inputfile:
    input_array.append(i)
for i in range(len(input_array)-1):
    input_array[i] = input_array[i][:-1]


#Writing function to give number of letters which appear twice
def appear_only_twice(str):
    temp = list(str)
    my_set = list(set(temp))
    letter = []
    counter_arr = []
    for i in my_set:
        letter.append(i)
        counter_arr.append(temp.count(i))
    return(2 in counter_arr, 3 in counter_arr)

#Solving The Problem
twice_counter = []
thrice_counter = []
for i in input_array:
    temp = [False,False]
    temp = appear_only_twice(i)
    print(temp)
    twice_counter.append(temp[0])
    thrice_counter.append(temp[1])

#Printing the final checkSum
print(twice_counter.count(True)*thrice_counter.count(True))


    



    