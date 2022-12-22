inputfile = open("day4.txt")

count=0
c2=0
total=0
for i in inputfile:
    total=total+1
    nums1=[]
    nums2=[]
    nums=[]
    x=[]
    y=[]
    z=[]
    x=i.split("-")
    nums.append(int(x[0]))
    y=x[1].split(",")
    nums.append(int(y[0]))
    nums.append(int(y[1]))
    nums.append(int(x[2].replace("\n","")))
    nums1.append(nums[0])
    nums1.append(nums[1])
    nums2.append(nums[2])
    nums2.append(nums[3])
    print(i)
    print(nums1)
    print(nums2)

    if (nums2[0]<=nums1[0] and nums2[1]>=nums1[1]) or (nums2[0]>=nums1[0] and nums2[1]<=nums1[1]):
        count=count+1

        
    if (nums1[0]<=nums2[0]<=nums1[1]) or( nums2[0]<=nums1[0]<=nums2[1]):
        c2=c2+1

print(count)
print(c2)
print(total)
    
