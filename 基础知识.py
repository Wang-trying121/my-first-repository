"""
while 条件：
    代码
"""
#需求：重复打印五次”“”
'''i = 0
while i < 5:
    print("对的")
    i += 1
    '''
#需求：1~100 累加和
#分析：加法运算重复执行
'''result = 0
i2 = 0
while i2 < 101:
    result = result + i2
    i2 += 1
print(result)
'''

#需求：计算1~100 偶数的累加和
#分析：利用if语句和整除规则
result = 0
'''i2 = 0
while i2 < 101:
   #条件
    if i2 % 2 == 0:
        result = result + i2
        i2 += 1
    else:
        i2 += 1
print(result)
'''
#break 条件
#循环吃五个苹果，到第三个不吃
'''i3 = 0
while i3 <= 5:
    i3 += 1
    print("吃了第%s苹果"%i3)
    if i3 == 3:
        break

print("吃饱了，不吃了")
'''
#continue条件退出当前循环，进而执行下一个循环
#跳过第三个再吃苹果
"""i4 = 1
while i4 < 6:
    if i4 == 3:
        print("吃出一个大虫子")
        i4 += 1       #修改计数器，否则进入死循环
        continue
    print("吃了第%s个苹果" % i4)
    i4 += 1"""
#while循环嵌套
#先循环打印三次，再进行一次，共重复三次
'''i5 = 1
i6 = 1
while i6<6:
    i5 = 1
    while i5 < 6:
        print("我错了")
        i5 += 1
    print("去刷碗")
    i6 += 1
print("好了")'''

#制作九九乘法表
#第一步：打印星号
'''i7 = 1
i8 = 0
while i7 < 6:
    #一行星星开始
    i8 = 0
    while i8 < i7:
        i8 += 1
        print("*",end='')      #如何在一行显示
    print() #默认换行
    i7 += 1'''

#第二步：制作九九乘法表
'''l = 1
r = 1
while r < 10:
    while l <= r: #输出一行
        print("%sx%s=%s"%(l,r,l*r),end="\t") #输出算式  #\t制表符
        l += 1
    r += 1
    l = 1
    print()'''

#for循环
'''str = "王鹏博"
for i in str:
    if i == "鹏":
        print("不打印")
        continue
    print(i)'''

'''#else语法
i = 1
while i < 6:
    print("我错了")
    if i == 3:
        print("不真诚")
        i += 1
        continue   #break退出循环无法启动程序，continue可以    #for 同理
    i += 1
else:
    print("原谅我了")'''


#字符串 """xx""" 三引号可换行，输出字符也换行 #\转译符号，使其作为内容出现 I\'m tom
#字符号输出 1.print('我的名字是%s'%name)   2.print(f'我的名字是{name}')
#input接收到的数据是字符串
#下标 数据按顺序有编号，从0开始 str[下标]
#切片 截取一部分 序列[开始下标,结束下标,步长（默认为1）] 步长为选取间隔，可正可负 左闭右开，默认为0

#修改 replace 替换 字符串.replace(旧,新,替换次数（默认）)
'''myth = "hello world and it and jj and asd"
print(myth.replace('and','kkk'))  #hello world kkk it kkk jj'''
'''myth = "hello world and it and jj and asd"         #字符串是不可变类型
new_myth = myth.replace('and','kkk')
print(new_myth)'''

''''#split()分割 字符串.split(分割字符，次数） 返回一个列表 丢失分隔符
myth = "hello world and it and jj and asd"
print(myth.split('and'))              #['hello world ', ' it ', ' jj ', ' asd']
#join合并字符
new_myth = "...".join(myth)    #h...e...l...l...o... ...w...o...r...l...d... ...a...n...d... ...i...t... ...a...n...d... ...j...j... ...a...n...d... ...a...s...d
print(new_myth)'''

#.capitalize首字母大写  title首字母大写  lower大写转小写  upper小写转大写
#列表
#下标查找数据
'''name_list = ['Tom','Lili','Alice']
print(name_list[2])'''
#index在一定范围内查找数据 name_list.index(查找数据,开始下标,结束下标)
#count统计次数  len 列表长度
#in判断是否存在   print('Lili' in name_list) True ;判断是否不存在 not in
#结尾增加数据 .append(数据） 追加整体作为结尾
'''name_list = ['Tom','Lili','Alice']
name_list.append('xiaoming')
print(name_list) #['Tom', 'Lili', 'Alice', 'xiaoming']'''
#extend 追加数据  insert 指定位置增加数据  列表.insert(下标,数据)
#pop删除指定下标的数据（默认最后） 并返回
#remove（数据）  clear 清空列表
'''name_list = ['Tom','Lili','Alice']
name_list.pop(1)
print(name_list)'''
#copy 复制
'''name_list = ['Tom','Lili','Alice']
list_1 = name_list.copy()
print(list_1)'''
'''name_list = ['Tom','Lili','Alice']
#列表的循环遍历
i = 0
while i <len(name_list):
    print(name_list[i])
    i += 1'''
'''name_list = ['Tom','Lili','Alice']
for i in name_list:
    print(i)'''
#列表嵌套
'''name_list = [['Tom','Lili','Alice'],['xiaoming','xiaohong','xiaogang'],['jia','yi','bing']]
print(name_list[0][1])'''

#案例： 8位老师，3个办公室，随机分配
'''步骤：
1.收集数据 老师名字与办公室数据
2.随机分配 调用random函数
3.打印信息'''
'''import random
teachers = ['A','B','C','D','E','F','G','H']
offices = [[],[],[]]
i = 1
for teacher in teachers:
    num = random.randint(0,2)
    offices[num].extend(teacher)  #随机分组
for office in offices:
    print(f'办公室{i}内有{len(office)}人，分别是：',end='')
    i += 1
    for teach in office:
        print(teach,end='')
    print()'''
#元组：存储不可修改的数据
'''t1 = (1,)
print(type(t1)) #<class 'tuple'>'''
'''t1 = (1)
print(type(t1))   #<class 'int'>''' #元组不支持修改，只支持查找  index查找 count次数 len个数 下标
'''t1 = (5,2,3,3,4,9)
print(t1[0])   #5
print(t1.index(2))   #1
print(t1.count(3))   #2
print(len(t1))       #6'''
#字典 不支持下标，以键对值出现 不在乎顺序

 #创建空字典 dict2 = {}    dict3 = dict()
#增数据
'''dict = {'name':'Tom','age':18,'gender':'男'}
dict['name'] = 'Lucy'
print(dict) #{'name': 'Lucy', 'age': 18, 'gender': '男'}
dict['id'] = 113
print(dict)#{'name': 'Lucy', 'age': 18, 'gender': '男', 'id': 113}'''

#删 del() clear()
'''dict = {'name':'Tom','age':18,'gender':'男'}
del dict['name']
print(dict)         #{'age': 18, 'gender': '男'}
dict.clear()
print(dict)  '''        #{}
#改 k存在即修改，不存在则新增
#查
'''dict = {'name':'Tom','age':18,'gender':'男'}
#print(dict['name'])        #Tom
#print(dict.get('name'))       #Tom
#print(dict.get('id',121))  #121
#print(dict)         #{'name': 'Tom', 'age': 18, 'gender': '男'}
#print(dict.get('id'))         #None key不存在
#print(dict.keys())         #dict_keys(['name', 'age', 'gender'])
#print(dict.values())          #dict_values(['Tom', 18, '男'])
print(dict.items())'''
#遍历
'''dict = {'name':'Tom','age':18,'gender':'男'}
for i in dict.keys():
    print(i,end=' ')  #name age gender 

for i in dict.values():
    print(i,end=' ')  #Tom 18 男'''
'''dict = {'name':'Tom','age':18,'gender':'男'}
for i in dict.items():
    print(i,end=' ') '''#('name', 'Tom') ('age', 18) ('gender', '男')
#拆包动作
'''dict = {'name':'Tom','age':18,'gender':'男'}
for i,m in dict.items():
    print(f'{i}={m}',end = " ") '''  #字典中的键值对可视为有两个元素的元组 #name=Tom age=18 gender=男

#集合 不重复 无序性
#s1 = {1,2,3,2,1,2,3,4}
'''s2 = set('abfjfnfkf')
print(s1) #{1, 2, 3} 有序
print(s2) #{'f', 'a', 'b', 'j', 'n', 'k'} {'b', 'a', 'f', 'j', 'n', 'k'} {'k', 'j', 'n', 'a', 'b', 'f'} 具有无序性
#增
s1.add(9)
print(s1) #{1, 2, 3, 9}
#追加多个数据
s1.update([89,67,55,35,67,86,54])
print(s1) #{1, 2, 3, 67, 35, 9, 86, 55, 54, 89}'''
#删
#删除指定顺序
'''s1.remove(1)
print(s1) #{2, 3}
s1.discard(2)
print(s1) '''#{1,3} 数据不存在时不报错

#查找数据 in  not in
#公用符号 + 合并 * 复制 in  not in
'''str1 = 'aa'
str2 = 'bb'
s1 = [1,2]
s2 = [2,4]
k1 = (22,33,44)
k2 = (23,43,22)
d1 = {1:'ji',2:'ki'}
d2 = {3:'ok',4:'pk'}'''
#print(str1+str2,end = "")
#print(s1+s2,end ="")
#print(k1+k2,end ="")
#print(d1+d2) #报错
#print(str1*3,end ="  ")
#print(s1*3,end ="  ")
#print(k2*3,end ="  ")
#print(d1*3,end ="  ") #报错

#统计个数len() 删除数据del() 返回最大/小值max()min()
'''a = 'hallo'
print(len(a)) #5'''
#range() range(起始，结束,步长)
#使下标和元素一一对应 enumerate()
'''list = ['a','s','d','f','g']
for i,j in enumerate(list):
    print(i,j,end=' ') #0 a 1 s 2 d 3 f 4 g '''

#容器类型转换 tuple()转换为元组 list()转换为列表 set()转换为集合 可以完成列表去重，不支持下标
#列表推导式
#list = [i for i in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#list2 = [i for i in range(10) if i%2 == 0] #[0, 2, 4, 6, 8]

#将两个列表合并为一个字典
'''list1 = ['a','s','d','f']
list2 = [1,2,3,4]
dict = {list2[i]:list1[i] for i in range(len(list1))}
print(dict) #{1: 'a', 2: 's', 3: 'd', 4: 'f'}'''
#提取目标数据
'''dict1 = {'ad':12,'ji':34,'oj':98,'ok':43}
dict2 = {i:f for i,f in dict1.items() if f >=50} #提取大于50的数
print(dict2)'''


