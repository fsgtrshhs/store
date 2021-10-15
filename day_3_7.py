num = 7
for x in range(-num,0):
    for y in range(-num,num):
       # print(x,y)
        if abs(x)+abs(y) <= num -1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
for i in range(num):
    print('  ',end = '')
    print("*",end= ' ')
