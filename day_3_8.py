N=int(input("请输入数字"))
for i in range(1,N):
    for j in range(1,i+1):
        print("{}x{}={}\t".format(i,j,i*j),end="")
    print()
