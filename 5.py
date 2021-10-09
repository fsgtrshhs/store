tard = input('请输入成绩')
tard = int(tard)
if tard >= 90:
    print('A')
if tard < 90 and tard >=80:
    print('B')
if tard <80 and tard >=70:
    print('C')
if tard <70 and tard >=60:
    print('D')
if tard <60:
    print('E')