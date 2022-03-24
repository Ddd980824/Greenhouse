#for循环中break的实例1
l = ["c","java","python","cjavapy"]
for x in l:
    if x == "python":
        break
    print (x)
print("*" * 5)
#for循环中continue的实例1
langs = ["c","java","python","cjavapy"]
for x in langs:
    if x == "python":
        continue
    print (x)
print("*" * 5)
#for循环中break的实例2
name = ['Atom','Luck','kid','Shaw','BIG','Blob']
n = 0
for i in name:
    print(i)
    n = n +1
    if n == 3:
        break
print("*" * 5)
#for循环中continue的实例2
name = ['Atom','Luck','kid','Shaw','BIG','Blob']
n = 0
for i in name:
    n = n +1
    if n == 3:
        continue
    print(i)
print("*" * 5)
#while循环中continue的实例
#while 判断条件(condition)
       #执行语句(statements)...
n = 5
while n > 0:
    if n == 2: #==是判断符号前后两者的逻辑运算符号
        n = n - 1 #=是赋值符号
        continue
    print(n)
    n = n - 1
print("*" * 5)
#while循环中break的实例
n = 0
while True:
    print(n)
    n = n + 1
    if n == 5:
        break
