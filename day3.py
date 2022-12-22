import math as m
import numpy as np
item=[]
pr=0
inputfile = open("day3.txt")
for i in inputfile:
    list1=[]
    
    list1.append(i[:m.floor((len(i)/2))])
    list1.append(i[(m.floor(len(i)/2))+1:])
    #print(i)
    #print(list)
    a = set(list1[0]).intersection(set(list1[1]))
    s = list(a)
    s.append("1")
    new=s[0]
    if ord(new)>96:
        pr = pr + ord(new) - 96
    elif ord(new)<96:
        pr = pr + ord(new) - 38
    

print(pr)
