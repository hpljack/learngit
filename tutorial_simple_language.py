__author__ = 'liuhuiping'
#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

class SyntaxException(Exception):
    """ SyntaxException   """
    pass

class ReturnException(Exception):
    pass

class Func():
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

class Env():
    pass

class Calculator():
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

    def error(self,msg):
        msg += ', at p %d'%self.p + str(self.ls[self.p])
        raise SyntaxException(msg)

    def push_p(self,env,p,ls):
        self.env = env
        self.prep_p = self.p
        self.p = p
        self.prep_p = self.ls
        self.ls = ls

    def pop_p(self):
        if self.env.parent == None:
            self.error('pop_p: no parent for env!')
        self.env = self.env.parent
        self.p = self.prep_p
        self.ls = self.prep_ls

    def function_call(self,func,args):
        #build in function
        if not isinstance(func,Func):
            return func(*args)

        env = Env(self.env)
        for name,v in zip(func.arg_names,args):
            env.set_value(name,v)

        self.push_p(env,func.p,func.ls)

        try:
            v = self.exp_list()
            self.pop_p()
        except ReturnException as e:
            v = e.value
        return v

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

    def goto_next_block(self):
        count = 1
        while self.has_next():
            if self.get() == '}':
                count -= 1
                if count < 0: break
            elif self.get() == '{':
                count += 1
            self.inc()

    def loop(self):
        self.inc()
        p = self.p
        while True:
            v = self.ltop()

            if self.get() != '{':
                self.error('exp error: no {')
                self.inc()
            if v > 0:
                v = self.exp_list()
            else:
                self.goto_next_block()

            if self.get() != '}':
                self.error('exp erro: no {')
            self.inc()

            if v <= 0:
                break
            else:
                self.p = p

            return v


    def assignment(self):
        name = self.get()
        self.inc()
        self.inc()
        v = self.exp()
        self.env.set_value(name,v)
        return v

    def outter_assignment(self):
        self.inc()
        name = self.get()
        self.inc()
        self.inc()
        v = self.get()
        self.env.set_outter_value(name,v)
        return v

    def condition(self):
        self.inc()
        v = self.ltop()
        if self.get() != '{':
            self.error('exp error no {')
        self.inc()

        if v > 0:
            v = self.exp_list()
        else:
            self.goto_next_block()

        if self.get() != '}':
            self.error('exp erro no }')
        self.inc()

        if self.has_next() and self.get() == 'else':
            self.inc()
            if self.get() != '{':
                self.error('exp error no {')
            self.inc()
            if v <= 0:
                v = self.exp_list()
            else:
                self.goto_next_block()
            if self.get() != '}':
                self.error('exp error: not }')
            self.inc()
        return v

    def function(self):
        func = Func()

        self.inc()
        name = self.get()
        if not self.issymbol(name):
            self.error('function error name %s'%name)
        self.inc()
        func.name = name

        if self.get() != '(':
            self.error('function error no (')
        self.inc()

        func.arg_names = self.function_args_name()

        if self.get() != ')':
            self.error('function error no )')
        self.inc()

        if self.get() == '{':
            self.error('function error no {')
        self.inc()

        func.p = self.p
        func.ls = self.ls

        self.goto_next_block()

        if self.get() != '}':
            self.error('function error no }')
        self.inc()

        self.env.set_value(func.name,func)
        return func

    def function_args_names(self):
        arg_name = []
        while self.issymbol(self.get()):
            arg_name.append(self.get())
            self.inc()
            if self.get() != ',':
                break
            self.inc()
        return arg_name

    def function_args(self):
        args = []
        if self.get() == ')':
            return args
        args.append(self.exp())

        while(self.get() ==','):
            self.inc()
            args.append(self.exp)
        return args


    def return_exp(self):
        self.inc()
        v = self.exp()
        self.pop_p()
        raise ReturnException(v)

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