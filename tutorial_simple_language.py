__author__ = 'liuhuiping'

#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

class SyntaxException(Exception):
    """ SyntaxException   """
    pass

def syntax_analysis(s):
    # """
    # >>> syntax_analysis("1+1")
    # [1,'+',1]
    # >>>syntax_analysis('2 * 3 + 1')
    # [2,'*',3,'+',1]
    # """
    p = 0
    ls = []
    while p < len(s):
        if(p < len(s) - 1
            and s[p: p + 2] == '=='):
            ls.append('==')
            p += 2
            continue
        if s[p] in '*/-+();=><{}':
            ls.append(s[p])
            p += 1
            continue
        elif s[p] in '0123456789.':
            d = []
            while p < len(s) and s[p] in '0123456789.':
                d.append(s[p])
                p += 1
                d = ''.join(d)
                try:
                    if '.' in d:
                        d = float(d)
                    else:
                        d = int(d)
                except:
                    raise SyntaxException('syntax error: value error on p%d: %s'%(p,d))
            ls.append(d)
            continue
        #Name
        elif s[p] in 'abcdefghijklmnopqrstuvwxyz':
            d = []
            while p < len(s) and s[p] in 'abcdefghijklmnopqrstuvwxyz':
                d.append(s[p])
                p += 1
            ls.append(''.join(d))
            continue
    return ls

class Calculator:
    """ Calculator """
    def __init__(self,s = None):
        pass

    def analysis(self,s):
        self.p = 0
        if s:
            self.ls = syntax_analysis(s)
        else:
            self.ls = []

    def __call__(self, s = None):
        if s:
            self.analysis(s)
        return self.program()

    def has_next(self,v = 0):
        return self.p < len(self.ls) - v

    def inc(self):
        self.p += 1

    def get(self,v = 0):
        return self.ls[self.p + v]

    def isstr(self,s):
        return (type(s) is str)

    def issymbol(self,s):
        return (type(s) is str and s[0] in 'abcdefghijklmnopqrstuvwxyz')

    def program(self):
        if self.has_next():
            return self.exp_list()

    def exp_list(self):
        v = self.exp()
        while self.has_next():
            if self.get() == ';':
                self.inc()
            if self.get() == '}':
                break
            v = self.exp()
        return v

    def exp(self):
        if self.has_next(1):
            if self.get(1) == '=':
                return self.assignment()
            if self.get() == 'outter':
                return self.outter_assignment()
            if self.get() =='if':
                return self.condition()
            if self.get() == 'while':
                return self.loop()
            if self.get() == 'def':
                return self.function()
            if self.get() =='return':
                return self.return_exp()
        return self.ltop()

    def ltop(self):
        return self.l3()

    def l3(self):
        v = self.l2()
        if not self.has_next():
            return v
        if self.get() == '<':
            self.inc()
            v2 = self.l2()
            if v < v2: return 1
            else: return 0
        elif self.get() =='>':
            self.inc()
            v2 = self.l2()
            if v > v2: return 1
            else: return 0
        elif self.get() == '==':
            self.inc()
            v2 = self.l2()
            if v == v2: return 1
            else: return 0
        return v

    def l2(self):
        v = self.l1()
        while (self.has_next()
            and self.isstr(self.get())
            and self.get() in '-+'):
            if self.get() == '+':
                self.inc()
                v2 = self.l1()
                v += v2
            elif self.get() == '-':
                self.inc()
                v2 = self.l1()
                v -= v2
        return v


    def l1(self):
        v = self.l0()
        while (self.has_next()
            and self.isstr(self.get())
            and self.get() in '*/'):
            if self.get() == '*':
                self.inc()
                v2 = self.l0()
                v *= v2
            elif self.get() == '/':
                self.inc()
                v2 = self.l0()
                if v2 == 0:
                    raise SyntaxException('divide by 0 from p: %d',self.p)
                v /= v2
        return v

    def l0(self):
        if not self.has_next():
            return
        g = self.get()
        if g == '(':
            self.inc()
            v = self.ltop()
            self.inc()
            return v
        elif(self.has_next(2)
            and self.issymbol(g)
            and self.get(1) == '('):
            func = self.env.get_value(g)
            self.inc()
            self.inc()
            args = self.function_args()

            if not self.get() == ')':
                self.error('l0 function call error')
            self.inc()
            return self.function_call(func,args)
        elif self.issymbol(g):
            self.inc()
            return self.env.get_value(g)
        elif self.has_next(1) and g =='-':
            self.inc()
            v = -self.ls[self.p]
            self.inc()
            return v
        else:
            self.inc()
            return g


    def loop(self):
        pass
    def assignment(self):
        pass
    def outter_assignment(self):
        pass
    def condition(self):
        pass
    def function(self):
        pass
    def return_exp(self):
        pass

if __name__ =='__main__':
    c = Calculator()
    try:
        while True:
            try:
                s = input('-->')
                print(c(s))
            except SyntaxException as e:
                print(e)
    except (EOFError,KeyboardInterrupt):
        print('bye')








