#Pandas Series 类似表格中的一个列（column），类似于一维数组，也可以保存任何数据类型。
#Series由索引（index）和列组成，函数如下：pandas.Series(data,index,dtype,name,copy)
#data:一组数据（ndarray类型）；index：数据索引标签，如果不指定，默认从0开始。dtype：数据类型，默认会自己判断；name：设置名称；copy：拷贝数据，默认为False
#实例1：
import pandas as pd
a = [1,2,3]
myvar = pd.Series(a)
print(myvar)
#实例2：根据索引值读取数据,没有制定索引，则索引值就从0开始
import pandas as pd
a = [1,2,3]
myvar = pd.Series(a)
print(myvar[1])
#实例3：制定索引值
import pandas as pd
a = ["Google","Runoob","Wiki"]
myvar = pd.Series(a,index = ["x","y","z"])
print(myvar)
#实例4：根据索引值读取数据
import pandas as pd
a = ["Google","Runoob","Wiki"]
myvar = pd.Series(a,index = ["x","y","z"])
print(myvar["y"])
#实例5：可以使用Key/value对象，类似字典来创建Series：
import  pandas as pd
sites = {1:"Google",2:"Runoob",3:"Wiki"}
myvar = pd.Series(sites)
print(myvar)
#实例6：如果只需要字典中的一部分数据，只需要制定需要数据的索引即可
import  pandas as pd
sites = {1:"Google",2:"Runoob",3:"Wiki"}
myvar = pd.Series(sites,index = [1,2])
print(myvar)
#实例7：设置Series名称参数：
import  pandas as pd
sites = {1:"Google",2:"Runoob",3:"Wiki"}
myvar = pd.Series(sites,index = [1,2],name = "RUNOOB-Series-Test")
print(myvar)