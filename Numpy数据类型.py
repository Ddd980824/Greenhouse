#numpy .dtype((object,align,copy)
#object-要转换为的数据类型对象 align-如果为true，填充字段使其类似C的结构体 copy-赋值dtype对象，如果为false，则是对内置数据对象的引用
#实例1
import numpy as np
#使用标量类型
dt = np.dtype(np.int32)
print(dt)
#实例2
import numpy as np
#int8,int16,int32,int64 四种数据类型可以使用字符串‘i1’，‘i2’，‘i4','i8'代替
dt= np.dtype('i4')
print(dt)
#实例3
import numpy as np
#字节顺序标注
dt= np.dtype('<i4')
print(dt)
#下面示例展示结构化数据类型的使用，类型字段和对应的实际类型将被创建
#实例4
#首先创建结构化数据类型
import numpy as np
dt = np.dtype([('age',np.int8)])
print(dt)
#实例5
#将数据类型应用于ndarray对象
import numpy as np
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)
#实例6
#类型字段名可以用于存取实际的age列
import numpy as np
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a['age'])
#下面的示例定义一个结构化数据类型student，包括字符串字段name，整数字段age，及浮点字段marks，并将这个dtype应用到ndarray对象
#实例7
import numpy as np
student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student)
#实例8
import numpy as np
student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
a = np.array([('abc',21,50),('xyz',18,75)],dtype = student)
print(a)