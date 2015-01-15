__author__ = 'Administrator'


def fib(x):
    a,b = 0,1
    while b < x:
        print(b)
        a,b = b,a + b

def fib2(x):
    a, b = 0,1
    while b < x:
        print(b,end=',')
        a,b = b, a + b

# 判断语句
# if elif else
#

def condition_test():
    x = int(input('please input an integer: '))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    else:
        print('More')

# for 语句
def for_test():
    a = ['cat','window','defenestrate']
    for x in a:
        print(x,len(x))

def for_test2(x = 5):
    for i in range(x):
        print(i,end='|')

def for_test3():
    b = ['Marry','had','a','little','lamb']
    for i in range(len(b)):
        print(i,b[i],end=', ')

def break_test(x = 10):
    for n in range(2,x):
        for x in range(2,n):
            if n % x == 0:
                print(n ,' equals ',x ,'*',n//x)
                break
        else:
            print(n,' is a primer number')

def isPrimer(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def Primer_Test(x):
    for i in range(2,x):
        if isPrimer(i):
            print(i,end=',')

def test():
    n = int(input('please input a integer, to get the primer number in this range: '))
    print('The primer number is ', Primer_Test(n))

if __name__ == '__main__':
    fib(10)
    fib2(10)
    print()
    fib(100)
    fib2(100)
    print()
    for_test()
    for_test2(10)
    print()
    # condition_test()
    for_test3()
    break_test(100)
    test()

