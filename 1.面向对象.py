#-*-coding:utf-8-*-
# Author:Lu Wei

class  Acount:
    #方法
    def login(self):
        print('登录')
    def logout(self):
        print('退出')

#调用类中方法
#1.创建类
x=Acount()#创建了一个类的对象
#2.使用对象调用类中方法
x.login()
x.logout()