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

    #元组  序列
    t = 12345,54321,'hello'
    print(t)
    print(t[0])
    u = t
    print(u)
    del t[0]
    print(t)
    print(u)

    





