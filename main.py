'''
  1.随机点名
  2.随机生成处罚遍数
    技术选型：
        容器类型：int str double boolean
            元组：(1,5,7,4)  不允许做任何修改
            列表：[1,5,7,8,10,41]  可以做任何操作
            字典:{}
    列表的几个方式：
        append()
        remove  pop(index)
        直接赋值
        直接打印即可
        len()取长度
优化代码：循环 键盘输入一个数字，判断为1那么生成人名，判断为2 那么生成遍数 判断为q or Q 退出
'''
import random
list=["吴承恩","汉弗莱","刘醒","兰尼斯特","流星花园","舒克","汉弗莱1"]
ran=random.randint(0,len(list)-1)
ran1=random.randint(0,90)
while True:
    num=input("请输入1或2，或者Q、q退出:")
    if num.isdigit():
        num=int(num)
        while num==1 or num==2 :
            if num ==1:
                print(list[ran])
                break

            elif num==2:
                print(ran1)
                break

    elif type(num) !=int:
        num=str(num)
        break








