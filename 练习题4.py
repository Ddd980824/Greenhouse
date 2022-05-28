#题目：输入某年某月某日，判断这一天是这一年的第几天？
#程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
year = int(input('year:\n')) #'\n'是换行  int表示整型数字类型
month = int(input('month:\n'))
day = int(input('day:\n'))
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334) #把每月前几个月的天数相加
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print('data error')
sum += day #sum累加day得到新sum
leap= 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)): #闰年：1.年份能被400整除 2.年份能被4整除但不能被100整除
    leap= 1
if (leap== 1) and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)
print('这是第 %d 天.' % sum)