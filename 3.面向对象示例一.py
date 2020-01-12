#-*-coding:utf-8-*-
# Author:Lu Wei

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
