num=int(input("请输入个数："))

if num==54321:
    num1=int(input("请输入一个数："))
    while num1!=0:
        print(num1%10)
        num1=num1//10
        print(num1)
