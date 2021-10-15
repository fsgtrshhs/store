
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]]
num=0
num1=0
nan_shu=0
nv_shu=0
pin_shu=0
pin_nian=0
names.append(["刘备", 45, "男", 220, "alibaba", 500, 30])
for i in range(len(names)):

    for j in range(7):
        if j==1:
            names[i][j] = int(names[i][j])
            num1 += names[i][j]
            pin_nian=num1/4

        if j == 2:
            if names[i][j] == "男":
                nan_shu += 1
            if names[i][j] == "女":
                nv_shu += 1
        if j==5:
            num += names[i][j]
            pin_shu=num/4
print("平均工资是：",pin_shu)
print("平均年龄是",pin_nian)
print("添加新员工之后",names)
print("男人数：",nan_shu,"女人数:",nv_shu)

