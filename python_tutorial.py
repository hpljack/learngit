__author__ = 'liuhuiping'


def fib(x):
    a,b = 0,1
    while b < x:
        print(b,end=',')
        a,b = b,a+b
    print()

def fib2(x):
    result = []
    a,b = 0,1
    while b < x:
        result.append(b)
        a,b = b, a + b
    return result

def isPrimer(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def primer(x):
    lst = []
    for i in range(2,x):
        if isPrimer(i):
            lst.append(i)
            # print(i,end=',')
    return lst

def print_primer(x):
    print("Primer in %s " %x,' is  ', primer(x))
    # print()

def pass_test():
    while True:
        pass


#pass create min class
#用pass创建最小类

class MyEmptyClass:
    pass


def ask_ok(prompt,retries=4,compliant='Yes or no , Please'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nope'):
           return False
        retries -= retries
    if retries < 0:
        raise IOError('refusenink user')
    print(compliant)

#多次调用，L中的结果会累加
def f(a,L=[]):
    L.append(a)
    return L

def f1(a,L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def f3(*args, L= None):
    if L is None:
        L = []
    L.append(args)
    return L

#关键字参数 key-value
def parrot(voltage,state='a stiff',action='voom',type='Norwegan Blue'):
    print(" This is parrot wouldn't ",action,end='')
    print('If you put ',voltage,"voltage through it ")
    print('Lovely plumage, the ', type)
    print("It's ",state, "!")

# *name必须在 **name 之前使用
def cheesshop(kind, *argments,**keywords):
    print('-- Do you have any ', kind, '?')
    print("-- I'm sorry , we are all out of  ", kind)
    for arg in argments:
        print(arg)
    print('-' * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

def concat(*arg,sep='/'):
    return sep.join(arg)


# lambda 表达式
def make_inc(n):
    return lambda x : x + n

#
def my_func():
	"""do nothing, but document it.

         No,really, id does'nt do anything.
         """
	pass

if __name__ =='__main__':
    print(my_func.__doc__)

    f = make_inc(23)
    print(f(20))
    print(f(234))

    print(concat('earth','mars','venus'))
    print(concat('earch','mars','venus',sep='.'))

    cheesshop("Limburger","It's very runny, sir.",
              "It's really very ,VERY, runny sir.",
              shopkeeper="Michael palin",
              client="John Cleesse",
              sketch="Cheese shop sketch")

    parrot(1000)
    parrot(action='V000m',voltage=100000)
    fib(10)
    # pass_test()
    x = 100
    print_primer(x)
    fib(100)
    fib(1000)
    fib(3000)

    print(fib2(20))

    # ask_ok('Do you want to quit?')

    print(f(2))
    print(f(3))
    print(f(4))

    print(f1(2))
    print(f1(3))
    print(f1(4))

    print(f3(5,6,7,8))
    print(f3(4,5,))