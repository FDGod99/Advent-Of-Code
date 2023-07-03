#Taking inputs
inputfile = open("2015/Day2_2015/day2_2015.txt", "r")

#Creating Array from txt file
input_array = []
for i in inputfile:
    input_array.append(i.split("x"))
input_array[-1][-1] = input_array[-1][-1]+"\n"  #last array does not have character \n, so adding it because surfacearea calculating fucntion is dependant on that

#Creating a Function to Calculate the SurfaceArea
def ribbion_length(arr):
    one = int(arr[0])
    two =  int(arr[1])
    three = int(arr[2].split("\\")[0])
    temp = [one,two,three]
    length = min(temp) #assigning minimum value to length
    temp.remove(length)
    width = min(temp) #assigning second minimum value to width
    temp.remove(width)
    height = temp[0] #assigning last value to heigh
    return((2*length)+ (2*width) + (length*width*height))


#Solving the problem
sum = 0
for x in input_array:
    sum = sum + ribbion_length(x)
print(sum)