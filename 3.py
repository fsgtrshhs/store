year = int(input('请输入年份:'))
if (year % 4 == 0 and year % 100 != 0) or year % 100 == 0:
    print('该年份是闰年')
else:
    print('该年份不是闰年')

