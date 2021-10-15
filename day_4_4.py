a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
for i in range(0,len(a)-1):
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print(a)



