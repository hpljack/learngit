__author__ = 'liuhuiping'

# Fibonacci 数列模块

def fib(n):
    a,b = 0,1
    while b < n:
        print(b,end=' ')
        a,b = b, a + b
    print()

def fib2(n):
    result = []
    a,b = 0,1
    while b < n:
        result.append(b)
        a,b = b, a + b
    return result

if __name__ =='__main__':
    import sys
    fib(int(sys.argv[1]))
    ls = fib2(int(sys.argv[1]))
    if len(ls) > 0:
        print(ls)