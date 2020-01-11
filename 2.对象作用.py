#-*-coding:utf-8-*-
# Author:Lu Wei

class File:
    def read(self):
        with open(self.xxx,mode='r',encoding='utf-8') as f:
            date=f.read()
        return date

    def write(self,content):
        with open(self.xxx, mode='w', encoding='utf-8') as f:
            f.write(content)
#实例化一个对象
obj1=File()
#在对象中写一个xxx='test.log'
obj1.xxx='test.txt'
#通过对象调用类中的read方法，read方法中的self就是obj1
obj1.write('luwei')
print(obj1.read())



obj2=File()



# class Person:
#     def __init__(self):
#         print('执行init')
#
# p1=Person()
#
# class Person:
#     def show (self):
#         temp='我是%s,年龄：%s，性别：%s'%(self.name,self.age,self.gender,)
#         print(temp)
#
# p1=Person()
# p1.name='luwei'
# p1.age=19
# p1.gender='nan'
# p1.show()



# class Person:
#     def __init__(self,name=None,age=None,gender=None):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def show (self):
#         temp='我是%s,年龄：%s，性别：%s'%(self.name,self.age,self.gender,)
#         print(temp)
#
# p1=Person('luwei',123,'aaa')
# p1.show()

class Per:
    def __init__(self,name,psd,mail):
        self.name=name
        self.psd=psd
        self.mail=mail
    def show(self):
        return '%s-%s-%s'%(self.name,self.psd,self.mail)
l=[]
while True:
    username=input('username:')
    if username=='n':
        break
    password=input('password:')
    mail=input('mail:')
    p=Per(username,password,mail)
    l.append(p)


for i  in  l :
    print(i.show())