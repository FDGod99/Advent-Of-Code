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
    for i in temp:
        for j in temp:
            if i%j==0 and i!=j:
                return(i,j)
            
#Solving the problem
sum=0
for x in input_array:
    [a,b] = calculate_checksum(x)
    sum = sum + int(a/b)

print(sum)
