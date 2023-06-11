#Taking inputs
inputfile = open("/Users/fdgod/Desktop/My Projects/Advent-Of-Code-2022/2019/day1_2019.txt", "r")

#Creating Array from txt file
input_array = []
for i in inputfile:
    input_array.append(int(i))

#Function calculating required fuel from mass input
def CalculateFuel(mass):
    return (int(mass/3)-2)

#Calculating Final fuel required for given mass considering fuel required for fuel and so on
def FinalFuel(mass):
    n = mass
    helper_array = []
    flag = 0
    while flag==0:
        fuel_for_n = CalculateFuel(n)
        helper_array.append(fuel_for_n)
        if CalculateFuel(fuel_for_n)<0:
            flag = 1
        else: n = fuel_for_n
    return(sum(helper_array))

#Calculating fuel for each element in array and adding up all
FuelSum = 0
for x in input_array:
    FuelSum = FuelSum + FinalFuel(x)

#Printing Final answer - Required total fuel
print(FuelSum)