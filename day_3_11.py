m=1
n=0
list=[]
for i in range(1,21):
    m*=i
    list.append(m)
    n+=m


print()
print(n)
print(sum(list))