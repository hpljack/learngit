__author__ = 'Administrator'


def this_fail():
     x = 1/ 0

def input_exception():
    try:
        while True:
            try:
                x = int(input('please enter a number: '))
                break
            except ValueError:
                print('Ops!, That was no valid number, Try again...')
    except Exception as error:
        print(error)

# 自定义异常
class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def MyError_test(n=2):
    try:
        raise MyError(n*n)
    except MyError as error:
        print('My exception occurred, value: ', error.value)

def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(e)
    else:
        print('result is ', result)
    finally:
        print('executing finally clause')



if __name__ =='__main__':
    # division by zero
    try:
        10 *(1/0)
    except Exception as e:
        print(e)

    try:
        this_fail()
    except ZeroDivisionError as error:
        print('Handling  run-time error ', error)

    import sys
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except IOError as error:
        print('I/O error:{0}'.format(error))
    except ValueError:
        print('could not convert datat to an integer.')


    try:
        raise NameError('Hi There')
    except NameError:
        print('An exception flew by!')
        # raise

    # input_exception()

    MyError_test()
    MyError_test(43)

    #异常的清理工作
    try:
        # raise  KeyboardInterrupt
        pass
    except Exception as e:
        print(e)
    finally:
        print('Good bye')

    divide(2,3)
    divide(2,0)

    for line in open('myfile.txt'):
        print(line,end='')
    print()

    #with 语句就允许像文件这样的对象在使用后会被正常的清理掉
    with open('myfile.txt') as f:
        for line in f:
            print(line,end='')
