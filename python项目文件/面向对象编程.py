'''法一
#定义“类”的语法
class 类名： 类名要用驼峰命名法
    pass
#创建对象
对象名 = 类名()
对象名.属性名 = 属性值1
对象名.属性名 = 属性值2
'''
# class Student:    #定义类
#     pass
#
# s1 = Student()   #创建对象
# s1.name = '小明' #为对象添加属性
# s1.age = 15
# s1.gender = '男'
# print(s1.__dict__) #用于以字典形式储存对象的属性

'''法二
定义类
class 类名：
    def __init__(self,参数列表): 函数在类中成为方法
        self.属性名 = 参数值
        self.属性名 = 参数值    
定义对象
对象名 = 类名(参数列表)    
'''
# #定义类
# class Student:
#     def __init__(self,s_name,s_age,s_gender):
#         self.s_name = s_name
#         self.s_age = s_age
#         self.s_gender = s_gender
#         print('Student初始化完毕')
# #定义对象
# s1 = Student('小明',15,'男')
# print(s1.__dict__)

# class Student:
#      def __init__(self,names,age,gender):
#          self.names = names
#          self.age = age
#          self.gender = gender
#          print('Student初始化完毕')
#      def testing(self):
#          print('正在考试中')
#      def student_grade(self,math,english,physic):  #补入等号可以设置默认值
#          self.math = math
#          self.english = english
#          self.physic = physic
#          grades = math + english + physic
#          return grades
# s1 = Student('小明',15,'男')
# student_grade = s1.student_grade(132,144,98)
# s1.testing()
# print(f'学生{s1.names}的成绩为{student_grade}')

'''魔法方法
改变作用与对象的符号含义'''
# class Student:
#      def __init__(self,names,age,gender):
#          self.names = names
#          self.age = age
#          self.gender = gender
#          print('Student初始化完毕')
#      def testing(self):
#          print('正在考试中')
#      def student_grade(self,math,english,physic):  #补入等号可以设置默认值
#          self.math = math
#          self.english = english
#          self.physic = physic
#          grades = math + english + physic
#          return grades
#      def __str__(self): #魔法方法，改变对象名的含义
#          return f"{self.names}"
#      def __eq__(self,other): #改变“等于”的含义
#          return self.age == other.age
#      def __lt__(self,other): #改变“xx”的含义  #__lt__小于 __le__小于等于 __gt__大于 __ge__大于等于
#          return  self.age < other.age
#
# s1 = Student('小明',15,'男')
# s2 = Student('小华',16,'男')
# student_grade1 = s1.student_grade(132,144,98)
# print(s1)
# print(s1 == s2)
# print(s1 < s2)

#实例属性与类属性
# class Student:
#      tax = 1.12 #类属性所有实力共用，类名.属性
#      age = 19
#      def __init__(self,names,age,gender):
#          self.names = names
#          self.age = age
#          self.gender = gender
#          print('Student初始化完毕')
#      def testing(self):
#          print('正在考试中')
#      def student_grade(self,math,english,physic):  #补入等号可以设置默认值
#          self.math = math
#          self.english = english
#          self.physic = physic
#          grades = math + english + physic
#          return grades
#      def __str__(self): #魔法方法，改变对象名的含义
#          return f"{self.names}"
#      def __eq__(self,other): #改变“等于”的含义
#          return self.age == other.age
#      def __lt__(self,other): #改变“xx”的含义  #__lt__小于 __le__小于等于 __gt__大于 __ge__大于等于
#          return  self.age < other.age
#
# s1 = Student('小明',15,'男')
# s2 = Student('小华',16,'男')
# student_grade1 = s1.student_grade(132,144,98)
# print(s1)
# print(s1 == s2)
# print(s1 < s2)
# #调用类属性时，以 实例.属性 的方式调用，先查找实例，再查找类
# print(Student.age) #19
# print(s1.age) #15
# print(s1.tax)#1.12

#具体实践：成绩操作系统
'''1.录入 2.修改 3.删除 4.查询 5.展示'''

#准备类
class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f"{self.name}:语文{self.chinese}|数学{self.math}|英语{self.english}"
    def change(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

class Edu:
    def __init__(self):
        self.name_list = []
    def add(self):
        name = input("请输入学生姓名：")
        for s in self.name_list:
            if s.name == name:
                print("已录入该学生信息")
                return
        try:
            chinese = int(input("请输入语文成绩："))
            math = int(input("请输入数学成绩："))
            english = int(input("请输入英语成绩："))
        except ValueError:
            print("成绩必须输入数字！录入失败")
            return
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.name_list.append(stu)
            print("学生添加成功")
            print(stu)
            return
        else:
            print("输入错误,请输入1~100之间的数字")
            return

    def change(self):
        name = input("请输入学生姓名：")
        for s in self.name_list:
            if s.name == name:
                print("已录入该学生信息,现在开始修改")
                try:
                    chinese = int(input("请输入语文成绩："))
                    math = int(input("请输入数学成绩："))
                    english = int(input("请输入英语成绩："))
                except ValueError:
                    print("成绩必须输入数字！录入失败")
                    return
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.change(chinese,math,english)
                    print("修改完成")
                    print(s)

                else:
                    print("输入错误")
                return
        print("无信息")





    def kill(self):
        name = input("请输入学生姓名：")
        for s in self.name_list:
            if s.name == name:
                self.name_list.remove(s)
                print("已删除该学生信息")
                return
        print("未查询到该信息")
        return

    def show(self):
        name = input("请输入学生姓名：")
        for s in self.name_list:
            if s.name == name:
                print(s)
                return

        print("未查询到该信息")
    def show_all(self):
        for s in self.name_list:
            print(s)

    def run(self):

        print("***************************************")
        print("欢迎登入成绩系统")
        print("***************************************")
        while True:
            print("请选择您的操作：1.录入 2.修改 3.删除 4.查询 5.展示 6.退出")
            choice = input()
            match choice:
                case "1":
                    self.add()
                case "2":
                    self.change()
                case "3":
                    self.kill()
                case "4":
                    self.show()
                case "5":
                    self.show_all()
                case "6":
                    print("bye")
                    break
                case _:
                    print("请重新输入")


hhh = Edu()
hhh.run()