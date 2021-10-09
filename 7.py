import random
import time
jinbi=5000
guess=15
an=3
randint = random.randint(1, 30)  # 随机产生的数字
while True:
    print(randint)
    num=input("请输入一个数字")
    if jinbi==0:
        break
    if guess==0:
        break
    if an==0:
        time.sleep(10)
        an += 3
    if num.isdigit():
        num=int(num)
        if num == randint:
            jinbi+=3000
            an-=1
            print("恭喜猜对了，获得3000金币，还有",jinbi,"金币")
            continue
        elif num >randint:
            jinbi -= 500
            guess-=1
            an-=1
            print("猜大了，扣除500金币，还有",jinbi,"金币")
            continue
        elif num <randint:
            jinbi -= 500
            guess-=1
            an-=1
            print("猜小了，扣除500金币，还有",jinbi,"金币",'还剩'+str(guess-1)+'的次数')
            continue
    else:
        jinbi -= 500
        guess-=1
        an-=1
        print("别瞎输入,扣除500金币，还有",jinbi,"金币")