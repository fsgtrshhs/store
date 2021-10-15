'''
 Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条
任务：打折：随机获得优惠券（9折10，5折5，1折2，面单1.
            单个商品打折9折10，5折5，1折2，面单1）

'''
import  random
#商品
shop=[
#     0      1
    ["刀🔪",999],#0
    ["斧子",200],#1
    ["👍",90000],#2
    ["coco",150],#3
    ["枸杞",900],#4
]
#初始化余额
youhui=[
    ["9",10],
    ["5",5],
    ["1",2],
    ["0",1]
]
money=random.randint(0,99999)


print(money)
#购物车
mycart=[]

i=0
while True:
    print(shop)
    for index ,value in enumerate(shop):
        print(index,":",value)

    chose=(input("请输入商品编号"))
    if chose.isdigit():
        you_huijuan = random.choice(youhui)

        print(you_huijuan)
        i=you_huijuan[0]
        i=int(you_huijuan[0])
        print(i)




        chose=int(chose)
        if chose<len(shop):
            if money>shop[chose][1]:

                mycart.append(shop[chose])

                if int(you_huijuan[1]) > 0:
                    money=money-shop[chose][1]*(0.1*i)


                    print(money)
                    you_huijuan[1]=you_huijuan[1]-1
                if int(you_huijuan[1]==0):
                    money=money-shop[chose][1]
                    print(money)
                # if you_huijuan[i][1]==0:
                #     print("没有优惠卷了")
                #     money=money-shop[chose][1]
                #     print(money)





    #展
    # 示商品










