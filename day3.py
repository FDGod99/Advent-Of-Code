import math as m
import numpy as np
item=[]
pr=0
inputfile = open("day3.txt")

#part
# for i in inputfile:
#     list1=[]
    
#     list1.append(i[:m.floor((len(i)/2))])
#     list1.append(i[(m.floor(len(i)/2)):])
#     #print(i)
#     #print(list)
#     a = set(list1[0]).intersection(set(list1[1]))
#     s = list(a)
#     s.append("1")
#     new=s[0]
#     if ord(new)>96:
#         pr = pr + ord(new) - 96
#     elif ord(new)<96:
#         pr = pr + ord(new) - 38
    

# print(pr)

#part2
inputgg=[]
for i in inputfile:
    inputgg.append(i[:-2])

listof3 = []

for i in range(0,len(inputgg),3):
    temp=[]
    temp.append(inputgg[i])
    temp.append(inputgg[i+1])
    temp.append(inputgg[i+2])
    listof3.append(temp)

print(listof3)

common = []
for i in listof3:
    set1 = set(i[0])
    set2 = set(i[1])
    set3 = set(i[2])

    a = set1.intersection(set2)
    b = a.intersection(set3)
    c = list(b)
    c.append("temp")
    common.append(c[0])

print(common)

