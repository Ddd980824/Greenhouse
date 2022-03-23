from datetime import datetime #引用datetime库
now = datetime.now() #获得当前日期和时间信息
print(now)
print(now.strftime("%x")) #输出其中的日期部分 %x表示日期
print(now.strftime("%X")) #输出其中的时间部分 %X表示时间
