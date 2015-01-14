__author__ = 'liuhuiping'

import  fibo
import sys
from fibo import  fib,fib2


#只有本模块当做主程序使用时，一下代码才会执行
#跟java类似，用于测试本模块的函数 类功能
if __name__ == '__main__':
    fib = fib2(100)
    print(fib)
    print(fibo.__name__) #__name__ 相当于模块名字
    print(fibo.__author__)

    print(dir(fibo)) #显示模块中定义的名字
    print(dir(sys))