import numpy as np
#np.array（）的作用是产生数组
a = np.array([1,2,3])
print(a)
#产生多于一个维度的数组
import numpy as np
b = np.array([[1,2],[3,4]])
print(b)
#最小维度
import numpy as np
c = np.array([1,2,3,4,5],ndmin = 2 )
print(c)
#dtype 参数 dtype 数组元素的数据类型，可选
import numpy as np
d = np.array([1,2,3],dtype = complex) #dtype = complex 定义为复数数组
print (d)