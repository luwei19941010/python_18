#-*-coding:utf-8-*-
# Author:Lu Wei
# 1.明确找到self到底是谁？
#
# 2.self是哪个类创建的，就从此类开始找，自己没有再找父类。

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
'''