cm="厘米"
yc="英寸"
while True:
    num=float(input("请输入一个长度："))
    num2=input("输入的是厘米还是英寸：")
    while num2==yc:
        num3=num*2.54
        print(num,"英寸等于",num3,"厘米")
        break
    while num2 == cm:
        num4 = num / 2.54
        print(num, "厘米等于", num4, "英寸")
        break