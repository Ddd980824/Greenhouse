import random
games = 10
for i in range(games):
    print("进行第{}场游戏".format(i+1)) #将format（）后面的内容填入大括号中
    result = random.randint(0,1) #result赋值0或者1
    if result == 1: #获胜
        print("朋友圈炫耀战绩")
    else:#results == 0 失败
        print("沉默...")
        print("*"*20)

for i in range(1,3): #给i赋值
    print(i)

for i in range(1,5,2): #从1到5，不包括5，每次增加2
    print(i)
for i in range(3):#从0到3，不包括5，默认每次增加1
    print(i)

import random
result = random.randint(0,3) #result随机赋值0-3之间任意整数，包括0和3
print ("result:",result)