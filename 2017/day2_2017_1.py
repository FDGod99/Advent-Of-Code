#Taking inputs
inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/2017/day2_2017.txt", "r")

#Creating Array from txt file
input_array = []
for i in inputfile:
    input_array.append(i.split("\t"))
for i in input_array:
    i[-1] = i[-1][:-1]
input_array[-1][-1] = '484'


#Function to calculate checksum for each row
def calculate_checksum(arr):
    temp = []
    for temp_ele in arr:
        temp.append(int(temp_ele)) 
    temp.sort() 
    return(temp[-1]-temp[0])

#Solving the problem
final_sum = 0
for x in input_array:
    final_sum = final_sum + calculate_checksum(x)

#Printing Final Result
print(final_sum)
