#Taking inputs
inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/2019/day2_2019.txt", "r")

#Creating Array from txt file
def Trial_Run(noun,verb,file):
    input_array = []
    input_array = i in file
    input_array = input_array.split(",")
    input_array = [int(element) for element in input_array]
    input_array[1] = noun
    input_array[2] = verb
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
    return(input_array[0])

for i in range(3,100):
    for j in range(2):
        print(i,i+j)
        if Trial_Run(i,i+j,inputfile)==19690720:
            print("Answer",i,i+j)
            break