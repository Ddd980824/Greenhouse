#ndarray.ndim 用于返回数组的维数,等于秩。
#实例
import numpy as np
a = np.arange(24) #numpy.arrange（）函数用于生成一维数组
print (a.ndim) #a 现在只有一个维度
#调整其大小
b = a.reshape(2,4,3) #b有3个维度
print (b.ndim)
#ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即ndim属性（秩）。比如，一个二维数组，其维度表示“行数”和“列数“，
# 也可以用于调整数组大小
#实例
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
#调整数组大小
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)
print(a)
#Numpy 也提供了reshape函数来调整数组的大小
#实例
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)
#ndarray.itemsize以字节的形式返回数组中每一个元素的大小。例如，一个元素类型为float64的数组itemsize属性值为8（float64占用64个bits，
# 每个字节长度为8，所以64/8，占用8个字节），又如，一个元素类型为complex32的数组item属性为4（32/8).
#实例
import numpy as np
#数组的 dtype 为int8（一个字节）
x = np.array([1,2,3,4,5],dtype=np.int8)
print(x.itemsize)
#数组的 dtype 现在为float64（八个字节）
y = np.array([1,2,3,4,5],dtype=np.float64)
print(y.itemsize)
#ndarray.flags 返回nddary对象的内存信息
#实例
import numpy as np
x = np.array([1,2,3,4,5])
print(x.flags)


#nddary.reshape 通常返回的是非拷贝副本，即改变返回后数组的原始怒，原数组对应元素的值也会发生改变。
import  numpy as  np
a = np.array([[1,2,3],[4,5,6]])
print(a)
b = a.reshape(6,)
print(b)
b[0]=100
print(b)
print(a)