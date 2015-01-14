__author__ = 'liuhuiping'


#PI
def GetPI(index = 3):
    return round(355/113,index)

if __name__ =="__main__":
    print('date strunct test')

    print("list's method example" )
    a = [665.3,443,45,23,665.3]
    print(a.count(333),a.count(665.3),a.count('x'))
    a.insert(2,-1)
    a.append(333)
    print(a)
    print(a.index(333))
    a.remove(333)
    a.reverse()
    print(a)
    a.sort()
    print(a)

    #把列表当堆栈使用
    stack = [3,4,5]
    stack.append(6)
    stack.append(7)
    print(stack)
    for i in range(len(stack)):
        print(stack.pop(),end=',')
    print()

    #把列表当队列使用
    from collections import  deque
    queue = deque(['Eric','john','Michael'])
    queue.append('Terry')
    queue.append('Grahm')
    for i in range(len(queue)):
        print(queue.popleft(),end=',')
    print()

    #列表推导式
    vec = [2,3,4]
    vec2 = [3 * x for x in vec]
    print(vec2)
    vec3 = [[x, x **2] for x in vec]
    print(vec3)

    freshfruit = [' banana','loganberry  ',' passion fruit']
    print(freshfruit)
    test = [weap.strip() for weap in freshfruit]
    print(test)

    vec4 = [3 * x for x in vec if x > 3]
    vec5 = [3 * x for x in vec if x < 2]
    print(vec4)
    print(vec5)

    #这里是一些循环的嵌套和其它技巧的演示:
    vecX = [2,4,6]
    vecY = [4,3,-9]
    vecXY = [x * y  for x in vecX for y in vecY]
    print('vecXY: ',vecXY)
    vecXplusY = [x + y for x in vecX for y in vecY]
    print('vecXplusY: ',vecXplusY)
    vecXY2 = [vecX[i] * vecY[i] for i in range(len(vecX))]
    print('vecXY2: ',vecXY2)
    print([str(round(355/113,i)) for i in range(1,6)]) # PI 的值
    print(GetPI(10))

    #嵌套列表推导
    mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print([[row[i] for row in mat] for i in [0,1,2]])
    #上句的冗长表达式
    for i in [0,1,2]:
        for row in mat:
            print(row[i],end=" ")
        print()
    #现实中, 你应当选择内建函式来处理复杂流程. 这里, 函式 zip() 就非常好用.
    print(list(zip(*mat)))

    #del 语句
    a = [-1,1,43.4,333,456,1234.5]
    del a[0]
    print(a)
    del a[-1]
    print(a)
    del a[2:3]
    print(a)
    del a
    # print(a) # exception a has been deleted

    #元组  序列 tuple
    t = 12345,54321,'hello' #元组打包
    print(t)
    print(t[0])
    u = t,(1,2,3,4)
    print(u)
    u += (6,7,8,9)
    print(u)
    x,y,z = t #序列解包
    print(z,y,x,sep='|')

    #集合 Set 集合是种无序不重复的元素集
    # 集合对象也支持合 (union),交 (intersection), 差 (difference), 和对称差 (sysmmetric difference) 等数学操作.
    basket = {'apple','orange','apple','apple','pear'}
    print(basket) #重复的被移除
    #集合操作
    a = set('badadebdeade')
    b = set('edefohde')
    print(a)
    print(b)
    print(a-b) #交集
    print(a|b) #并集
    print(a&b) #同或
    print(a^b) #异或
    a ={x for x in 'abracadabra' if x not in 'abc'}
    print(a)

    #字典 Mapping types - dict key-value
    tel = {'jack':4098,'sape':9832}
    tel['guilo'] = 4271
    print(tel)
    del tel['sape']
    print(tel)
    tel['Iris'] = 8451
    print(tel)
    lst = list(tel.keys())
    print(lst)
    sorted(tel.keys())
    print(tel)
    print('jack' in tel)

    tel2 = dict(jack=1024,sape=2048,Iris=8983,guilo=4343)
    print(tel2)

    #遍历技巧
    knights = {'gallahad':'the pure','robin':'the brave'}
    for k,v in knights.items():
        print(k,v,sep=':')

    for i, v in enumerate(['tic','tac','toel']):
	    print(i,v)
    print()

    row = ['jack','broc','sepx']
    for i,v in enumerate(row):
        print(i,v)
    print()


    question = ['name','quest','favorite color']
    answer = ['lancelot','the holy grail','blue']
    for q,a in zip(question,answer):
        print('what is your {0} ? It is {1}'.format(q,a))
    print()

    for i in reversed(range(1,20,2)):
        print(i,end=',')
    print()

    for f in sorted(set(basket)):
        print(f)
    print()












