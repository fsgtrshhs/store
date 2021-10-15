import time

ci=0
while True:
    ci+=1
    num = input("请输入用户名：")
    num2 = input("请输入密码：")
    if num2=="admin" and num=="root":
        print("登录成功")
        break
    elif ci==3:
        time.sleep(100)
        print("输错三次系统锁定")