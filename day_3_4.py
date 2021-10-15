num1=float(input("第一条边：",))
num2=float(input("第二条边：",))
num3=float(input("第三条边：",))
if num1+num2>num3 and num1+num3>num2 and num3+num2>num1:
    print("能构成三角形")
    if num1==num3==num2:
        print("能构成等边+三角形")
    if num1==num3 or num1==num2 or num3==num2:
        print("能构成等腰三角形")
    if num1*num1+num2*num2==num3*num3 or num1*num1+num3*num3==num2*num2 or num2*num2+num3*num3==num1*num1:
        print("能构成直角三角形")
    else:
        print("能构成普通三角形")
else:
    print("不能构成三角形")