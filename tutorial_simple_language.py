__author__ = 'liuhuiping'


#最小异常类
class SyntaxException(Exception):
    pass

class Caculator:
    def __init__(self,s=None):
        self.ls = []
        self.p = 0



if __name__ == '__main__':
    c = Caculator();
    try:
        while True:
            try:
                s = input('-->')
                print(c(s))
            except SyntaxException as e:
                print(e)
    except (EOFError,KeyboardInterrupt):
        print('bye')


