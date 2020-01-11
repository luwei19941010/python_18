### day19

#### 今日内容

- 面向对象基础用法
- 好处和应用场景
- 面向对象的三大特性
  - 封装
    - 把同一类的方法封装在一个对象中。
    - 把一些数据封装到对象中，方便以后获取。
  - 多态
  - 继承

#### 内容详细

##### 1.面向对象基本格式

```
class 类名：
	def 方法名(self,name):
		print(name)
		return 123
	def 方法名(self,name):
		print(name)
		return 123
	def 方法名(self,name):
		print(name)
		return 123
		
#调用类中的方法
#1.创建类的对象
obj=类名()
#2.通过对象调用类的方法
result=obj.方法名('luwei')
print(result)
```

应用场景：遇到很多函数，需要给函数做归类和划分

##### 2.对象作用

存储一些值，以后方便自己使用。

```
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
```



```
class Person:
    def show (self):
        temp='我是%s,年龄：%s，性别：%s'%(self.name,self.age,self.gender,)
        print(temp)
        
#类()实例化对象。
p1=Person()
p1.name='luwei'
p1.age=19
p1.gender='nan'
p1.show()
```

```
class Person:
    def __init__(self):
        print('执行init')
#类()实例化对象，自动执行此类中的__init__方法
p1=Person()

class Person:
    def __init__(self,name=None,age=None,gender=None):#初始化方法，给对象内部做初始化
        self.name=name
        self.age=age
        self.gender=gender
    #将数据分装在对象中，方便之后调用。
    def show (self):
        temp='我是%s,年龄：%s，性别：%s'%(self.name,self.age,self.gender,)
        print(temp)

p1=Person('luwei',123,'aaa')
p1.show()

###########将数据封装到对象做初始化。
```

##### 总结：

如果写代码时，函数比较多比较乱

1.可以将函数归类到同一个类中

2.函数如果有一个反复使用的公共值，则可以放到对象中。

```
#1.循环让用户输入，用户名/密码/邮箱，输入完成之后再进行数据打印
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
```







