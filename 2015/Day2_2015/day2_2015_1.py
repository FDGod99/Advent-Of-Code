#Taking inputs
inputfile = open("2015/Day2_2015/day2_2015.txt", "r")

#Creating Array from txt file
input_array = []
for i in inputfile:
    input_array.append(i.split("x"))
input_array[-1][-1] = input_array[-1][-1]+"\n"  #last array does not have character \n, so adding it because surfacearea calculating fucntion is dependant on that


#Creating a Function to Calculate the SurfaceArea
def surfacearea(arr):
    length = int(arr[0])
    width =  int(arr[1])
    height = int(arr[2].split("\\")[0])
    return((2*length*width + 2*width*height + 2*height*length)+min([length*width,width*height,height*length]))

#Solving the problem
sum = 0
for x in input_array:
    sum = sum + surfacearea(x)
print(sum)