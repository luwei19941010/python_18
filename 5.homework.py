#-*-coding:utf-8-*-
# Author:Lu Wei
#1.简述编写类和执行类中方法的流程。
'''
class 类：
    def __init__(self,name):
        self.name=name
    def func(self):
        pass
p=类('luwei')
p.func()
'''
#2.简述面向对象三大特性?
'''
1.封装
    1.将同一类型函数归为一类，封装在同一类中。
    2.将数据写入封装在对象中，以方便未来使用。
2.继承
    1.明确self是谁？
    2.self由哪一个类创建，则先去那个类中查看。
3.多态
'''
'''
#3.将以下函数改成类的方式并调用 :
class C:
    def func(a1):
        print(a1)

p=C()
p.func()
'''
#4.面向对象中的self指的是什么?
#self是指对象。

'''
#5.以下代码体现 向对象的 么特点?
#封装，将数据写入封装在对象中
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


obj = Person('武沛齐', 18, '男')
print(obj.name,obj.age,obj.gender)



#6.以下代码体现 向对象的 么特点?
#封装，将功能类似函数（方法）封装在同一个类中。
class Message:
    def email(self):
        """
        发送邮件
        :return:
        """
        pass

    def msg(self):
        """
        发送短信
        :return:
        """
        pass

    def wechat(self):
        """
        发送微信
        :return:
        """
        pass


#7.看代码写结果
class Foo:
    def func(self):#没有返回值
        print('foo.func')

obj = Foo()
result = obj.func()
print(result)


#8.定义个类，其中有计算周长和面积的方法(圆的半径通过参数传递到初始化方法)。

class Circular:
    def __init__(self,R):
        self.r=R
    def Girth(self):
        return 2*self.r*3.14
    def Area(self):
        return  self.r**2* 3.14
C=Circular(10)
print(C.Area())
print(C.Girth())

#9.面向对象中为什么要有继承?
#当多个类需要具有相同的方法功能，为了代码重用性，所以使用继承
#10.Python继承时，查找成员的顺序遵循 么规则?
#先从self是由哪一个类创建，在该类内部查找方法，如果没有则去父类中，在多继承是先从左往右依次。


#11.看代码写结果
class Base1:
    def f1(self):
        print('base1.f1')

    def f2(self):
        print('base1.f2')

    def f3(self):
        print('base1.f3')
        self.f1()

class Base2:
    def f1(self):
        print('base2.f1')

class Foo(Base1, Base2):
    def f0(self):
        print('foo.f0')
        self.f3()

obj = Foo()
obj.f0()
#foo.f0
#base1.f3
#base1.f1



#12.看代码写结果:
class Base:
    def f1(self):
        print('base.f1')

    def f3(self):
        self.f1()
        print('base.f3')


class Foo(Base):
    def f1(self):
        print('foo.f1')

    def f2(self):
        print('foo.f2')
        self.f3()


obj = Foo()
obj.f2()
#foo.f2
#foo.f1
#base.f3

#4.补充代码实现
"""
# 需求
1. while循环提示 户输 : 户名、密码、邮箱(正则满 邮箱格式)
2. 为每个 户创建 个对象，并添加到 表中。
3. 当 表中的添加 3个对象后，跳出循环并以此循环打印所有 户的姓名和邮箱
"""
class Person:
    def __init__(self,user,pwd,email):
        self.user=user
        self.pwd=pwd
        self.email=email
    def show(self):
        return '%s-%s-%s'%(self.user,self.pwd,self.email)
user_list = []
while True:
    user = input('请输入用户名:')
    pwd = input('请输入密码:')
    email = input('请输入邮箱:')
    p=Person(user,pwd,email)
    user_list.append(p)
    if len(user_list)==3:
        break
for i in user_list:
    print(i.show())
'''
#14.补充代码:实现户注册和登录。
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []
    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        while True:
            flag = False
            user = input('请输入用户名:')
            if user.upper() == 'N':
                print('XXXX')
                return
            pwd = input('请输入密码:')
            for i in self.user_list:
                if user == i.name and pwd == i.pwd:
                    flag = True
            if flag:
                print('登录成功')
                return
            else:
                print('登录失败')
    def register(self):
        """
        用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        user = input('请输入用户名:')
        if user.upper()=='N':
            print('XXXX')
            return
        for i in self.user_list:
            if user==i.name:
                print('已存在')
                return
        pwd = input('请输入密码:')
        p=User(user,pwd)
        self.user_list.append(p)
        print('注册成功')
    def run(self):
        """
        主程序
        :return:
        """
        while True:
            func_d = {'1': self.login, '2': self.register}
            print('请选择'.center(30, '&'))
            print("""1.登录
2.注册
                    """)
            user_chioce = input('请选择:')
            func=func_d.get(user_chioce)
            func()

if __name__ == '__main__':
    while True:
        try:
            obj = Account()
            obj.run()
        except Exception as e:
            print('输入失败')
