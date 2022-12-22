inputfile = open("day1.txt", "r")
mylist=[]
list2=[]
for i in inputfile:
    if i!="\n":
        list2.append(int(i[:-1]))
    else:
        mylist.append(list2)
        list2=[]
#print(mylist)
total = []
for item in mylist:
    total.append(sum(item))

#print(total)
top=[]
top.append(max(total))
total.remove(max(total))
top.append(max(total))
total.remove(max(total))
top.append(max(total))

print(top)

print(sum(top))
