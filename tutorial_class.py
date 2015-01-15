__author__ = 'Administrator'

def scope_test():
    def do_local():
        spam = 'local spam'
    def do_nonlocal():
        spam ='nonlocal spam'
    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spame'
    do_local()
    print('After  local assignment: ',spam)
    do_nonlocal()
    print('After nonlocal assignment: ',spam)
    do_global()
    print('After global assignment: ', spam)

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'Hello world'

class Complex:
    """
     complex type
    """
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart

#指定一个函数在给类
def f1(self,x,y):
    return min(x,x+y)

class C1:
    f = f1
    def g(self):
        return 'Hello world'
    h = g

class Bag:
    """ Bag test"""
    def __init__(self):
        self.data = []
    def add(self,x):
        self.data.append(x)
    def addtwice(self,x):
        self.data.append(x)
        self.data.append(x)

# pascal 的 record
# 用空的类定义表示结构体
class Employee:
    pass

#exception
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

class Reverse:
    """ Iterator for looping  over sequence backwards"""
    def __init__(self,data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

if __name__ == '__main__':
    #域和命名空间的例子
    scope_test()
    print('In global scope: ', spam)

    x = MyClass()
    str = x.f()
    print(x.f())
    print(str)
    print(x.i,x.__doc__)

    xf = x.f
    print(xf())

    x.counter = 1
    while x.counter < 10:
        x.counter *= 2
    print(x.counter)
    del x.counter

    x = Complex(3.0,-4.4)
    print(x.r,x.i,sep='+',end='j\n')

    x.counter = 1
    while x.counter < 10:
        x.counter *= 2
    print(x.counter)
    del x.counter

    c = C1()
    print(c.f(3,54))
    print(c.h())

    mybag = Bag()
    mybag.add('apple')
    mybag.addtwice('pear')
    print(mybag.data)

    #结构体使用
    john = Employee()
    john.name ='John Doe'
    john.dept = 'R&D'
    john.salary = 1000

    # 迭代器
    for c in [B,C,D]:
        try:
            raise c()
        except D:
            print('D')
        except C:
            print('C')
        except B:
            print('B')

    for n in [1,2,3]:
        print(n,end=',')
    print()

    for n in (4,5,6):
        print(n,end=',')
    print()

    for k,v in {'one': 1,'two':2}.items():
        print(k,v,sep=':',end=' ')
    print()

    for char in 'abc':
        print(char,end=',')
    print()

    with open('myfile.txt') as f:
        for line in f:
            print(line,end='')
    print()

    rev = Reverse('abcderfd');
    iter(rev)
    for char in rev:
        print(char,end=',')
    print()

    #发生器  用于创建迭代器的简单而强大的工具
    def reverse(data):
        for index in range(len(data)-1,-1,-1):
            yield data[index]
    for char in reverse('golf'):
        print(char,end=',')
    print()
    #功能同上
    data = 'golf'
    ls = list(data[i] for i in range(len(data) - 1,-1,-1))
    for i in range(len(ls)):
        print(ls[i],end=',')
    print()

    #几个生成器的example
    res = sum(i * i  for i in range(10))
    print(res)

    xvec = [10,20,30]
    yvec = [7,5,3]
    res = sum(x * y for x,y in zip(xvec,yvec))
    print(res)

    from math import pi, sin
    sine_table = {x:sin(x*pi/180) for x in range(0,9)}
    # unique_words = set(word for line in page for word in line.split())


