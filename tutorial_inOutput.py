__author__ = 'liuhuiping'

#递增模型
def calcc(n,step=3):
    i = 1
    cnt = 1
    result = 0
    while cnt < n:
        if cnt == 1:
            i = 1
        else:
            i *= step
        result += i
        print(cnt, ': number is  ',i)
        cnt += 1
    return result


if __name__ =='__main__':
    s = 'hello world.'
    print(str(s))
    print(repr(s))

    #string模块包含一个类模板
    print(str(1.0/7.0))
    print(repr(1.0/7.0))
    x = 10 * 3.25
    y = 200 * 200
    s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y)
    print(s)

    for x in range(1,11):
        print(repr(x).rjust(2), repr(x*x).rjust(3),end=' ')
        print(repr(x*x*x).rjust(4))

    # n = int(input('please input the step you want to query: '))
    n = 20
    res = calcc(n,3)
    print('the %d'%n, 'step count is ', res)


    for x in range(1,11):
        print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))
    print()
    print('12'.zfill(5))


    #文件的读写
    # f = open('readme.txt','w')
    # str = f.read()
    # print(str)
    # str = f.readline()
    # print(str)
    # f.write('this is a test')
    with open('readme.txt','r+') as f: # w: write   r+: write and read r: read default mode a: append file
        read_data = f.readline()
        # print(read_data)
    # f.write("# w: write   r+: write and read r: read default mode a: append file ")
    f.closed
    # print(read_data)

    # pickle 模块
    #这个模块可以将几乎任何的 Python 对象 (甚至是 Python 的代码), 转换为字符串表示; 这个过程称为 pickling. 而要从里面重新构造回原来的对象, 则称为 unpickling.
    #在 pickling 和 unpickling 之间, 表示这些对象的字符串表示, 可以存于一个文件, 也可以通过网络在远程机器间传输.

    import  pickle
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    t1 = ('this is a string', 42, [1, 2, 3], None)

    p1 = pickle.dumps(t1)
    print(p1)
    t2 = pickle.loads(p1)
    print(t2)
    p2 = pickle.dumps(t1,True)
    print(p2)
    t3 = pickle.loads(p2)
    print(t3)

    a1 = 'apple'
    b1 = {1:'one',2:'two',3:'three'}
    c1 ={'fee','fie','foe','fum'}
    f1 = open('temp.pkl','wb')
    pickle.dump(a1,f1)
    pickle.dump(b1,f1,True)
    pickle.dump(c1,f1,True)
    f1.close
    f2 = open('temp.pkl','rb')
    a2 = pickle.load(f2)
    print(a2)
    b2 = pickle.load(f2)
    print(b2)
    c2 = pickle.load(f2)
    print(c2)
    f2.close
