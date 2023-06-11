#Taking inputs
inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/2019/day1_2019.txt", "r")

#Creating Array from txt file
input_array = []
for i in inputfile:
    input_array.append(int(i))

#Variable to store Fuel Sum
FuelSum = 0

#Function calculating required fuel from mass input
def CalculateFuel(mass):
    return (int(mass/3)-2)

#Calculating mass for each array in  mass element and adding up all
for j in input_array:
    FuelSum = FuelSum + CalculateFuel(j)

#Printing Final answer - Required total fuel
print(FuelSum)

