zongchengji={"罗恩":[ 23 ,35 ,44],
            "哈利" :[60, 77 ,68 ,88, 90],
            "赫敏": [97 ,99 ,89 ,91, 95, 90],
            "马尔福" :[100, 85 ,90]}
num2=0
num=""
geren_chengji=0
geren_chengji1=0
while True:

    num=input("请输入姓名")
    geren_chengji=zongchengji[num]
    for j in geren_chengji:


        geren_chengji1+=j

    print(num,"的总成绩:",geren_chengji1)

    geren_chengji1=0





