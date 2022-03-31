aaa_dict = {"a":100,"b":20,"c":120,"d":10}
print("字典为{}".format(aaa_dict))

#字典转换为列表
aaa_list = list(aaa_dict.items())
print("字典转换为列表:{}".format(aaa_list))

#列表按照第1列排序
aaa_list.sort(key = lambda d:d[1],reverse = True)
print("列表按照第1列排序:{}".format(aaa_list))

#列表按照第0列排序
aaa_list.sort(key = lambda b:b[0],reverse = True)
print("列表按照第0列排序:{}".format(aaa_list))

#sort()函数用于对原列表进行排序
#用法list.sort(cmp = None,key = None,reverse = False)
# cmp -- 可选参数，如果指定了该参数会使用该参数的方法进行排序
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，制定可迭代对象中的一个元素进行排序
# reverse -- 排序规则，reverse = True 降序，reverse = False 升序（默认）
# key = lambda k:k[1] 它指定的排序规则为按列表元素（一个二元组）的第二个子元素（第1列）进行升序排列
#列表的索引是从0开始的