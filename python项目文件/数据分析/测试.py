import pandas as pd
# 读取Excel文件
df = pd.read_excel('学生成绩数据.xlsx')#, usecols = ['姓名','语文','数学','英语','物理','化学','生物'])
# 显示所有列
pd.set_option('display.max_columns', None)
# 不限制显示宽度
pd.set_option('display.width', None)
#数据处理
# df['总成绩'] = df['语文'] + df['数学'] + df['英语'] + df['物理'] + df['化学'] + df['生物']
# #写入数据
# df.to_excel('学生成绩数据_01.xlsx', index=False)
# #检查
# print(df['总成绩'].max())#最高分
# print(df['总成绩'].min())#最低分
# print(df['总成绩'].mean())#平均分


#数据查看—————— head tail describe info shape columns
print(df.head(10))#显示前10行数据
print(df.tail(10))#显示后10行数据
