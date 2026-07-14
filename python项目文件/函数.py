#函数的设置 def 函数名():
#函数的调用 函数名()
#形参与实参
def plus(a,b):   #形参
    '''求和函数 两个变量求和'''
    result = a+b
    print(result)
#return 返回函数值 退出当前函数
def plus2(a,b):
    '''
    求和函数 两个变量求和
    :param a: 参数1
    :param b: 参数2
    :return: 和
    '''
    return a+b
#说明文档
help(plus2) #求和函数 两个变量求和 #高级使用：中间回车