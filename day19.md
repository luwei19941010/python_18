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

##### 2.1封装

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

实例一：

```
class Plice:
    def __init__(self,name):
        self.name=name
        self.hp=1000
    def qiang(self,other):
        msg='%s打了%s一枪'%(self.name,other.name)
        other.hp=other.hp-100
        print(other.hp,msg)
    def quan(self,other):
        msg='%s打了%s一枪'%(self.name,other.name)
        other.hp=other.hp-50
        print(other.hp,msg)

class Bandit:
    def __init__(self,name):
        self.name=name
        self.hp=500
    def qiang(self,other):
        msg='%s打了%s一枪'%(self.name,other.name)
        other.hp=other.hp-100
        print(other.hp,msg)

lw=Plice('luwei')
yt=Bandit('yaoting')

lw.qiang(yt)
lw.quan(yt)
yt.qiang(lw)
print(lw.hp,yt.hp)
```





##### 2.2继承：



```
#父类（基类）
class Base:
	def f1(self)
		pass
#子类（派生类）
class Foo:
	def f2(self):
		pass
		
#创建一个子类的对象
obj=Foo()
#执行对象.方法时，优先在自己的类中找，如果没有就在父类中找。
obj.f2()
obj.f1()
#创建一个父类的对象
obj.Base()
obj.f1()
```

何时使用继承？当多个类都需要共同方法，则可以使用继承，增加代码重用性。

继承关系的查找方法的顺序。

```

'''
class Base:
    def f1(self):
        print('base.f1')
class Foo(Base):
    def f2(self):
        print('foo.f2')
obj=Foo()
obj.f1()
obj.f2()


class Base:
    def f1(self):
        print('base.f1')
class Foo(Base):
    def f2(self):
        self.f1()
        print('foo.f2')

obj=Foo()
obj.f2()


class Base:
    def f1(self):
        print('base.f1')
class Foo(Base):
    def f2(self):
        self.f1()
        print('foo.f2')
    def f1(self):
        print('foo.f1')

obj=Foo()
obj.f2()

'''
class Base:
    def f1(self):
        print('base.f1')
class Foo(Base):
    def f2(self):
        self.f1()
        print('foo.f2')
    def f1(self):
        print('foo.f1')

obj=Foo()
obj.f2()class Base:
	def f1(self)
```

1.明确找到self到底是谁？

2.self是哪个类创建的，就从此类开始找，自己没有再找父类。

多继承 继承类从左往右找

```
class BaseServer:
    pass

class TCPServer(BaseServer):
    pass

class ThreadingMixIn:
    pass

class ThreadingTCPServer(ThreadingMixIn,TCPServer):
    pass

obj=ThreadingTCPServer()
obj.serve_forever()

查找顺序1.ThreadingTCPServer →2.ThreadingMixIn →3.TCPServer →4.BaseServer
```

##### 2.3多态(多种类型/多种形态)

```
def func(arg)
	v=arg[-1]
	print(v)
```

什么是鸭子模型

```
对于一个函数而言，python对于参数的类型不会限制，那么传入参数就可以是各种类型，在函数如果列如：arg.send方法，那么就是对于传入类型的一个限制（类型必须要有send方法）
这就是鸭子模型，类似于上述的函数我们认为只要呱呱叫的就是鸭子（只要有send方法，就是我们想要的类型）
```



#### 今日总结：

##### 1.面向对象的三大特性：1.封装 2.继承 3.多态

- 封装 1.将同一类方法封装到一个类中。2.将一些数据写入到对象中，以便之后使用

  ```
  class File：
  	def read(self)：
  		pass
  	def write(self)：
  		pass
  ```

  ```
  class Person:
  	def __init__(self,name,age):
  		self.name=name
  		self.age=age
  p=Person('luwei',18)
  
  ```

- 继承

  ```
  class Base:
  	pass
  class Foo(Base):
  	pass
  ```

  - 多继承
  - self到底是谁？
  - self是由哪个类创建，就从这个类开始找。

- 多态

  ```
  def func(arg):#多种类型
  	arg.senc()#必须具有send方法
  ```

  

##### 2.面向对象格式关键词

```
class 类：
	def __init__(self,x):
		self.x=x
	def 方法(self)：
		print(self.x)
#实例化一个对象
v1=类(666)#自动执行__init__方法
v2.方法('alex')
```

##### 3. 三个词：类，对象，方法





##### 4.什么时候使用面向对象

- 函数（业务功能）比较多，可以使用面向对象将函数进行封装归类
- 想要做数据封装时