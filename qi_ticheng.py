i=int(input("净利润："))
arra=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for idx in range(0,6):
    if i>arra[idx]:
        tmp=(i-arra[idx])*rat[idx]
        r=r+tmp
        i=arra[idx]
print(r)