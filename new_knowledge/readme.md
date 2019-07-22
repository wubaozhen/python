```
# 写一个函数，传入一个参数n,返回n的阶乘

# 高阶函数：
from functools import reduce

num = 5
print(reduce(lambda x,y:x*y,range(1,num+1)))

# 递归：
def Fun(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * Fun(n-1)

print(Fun(5))

# 普通：
def Fun(n):
    ret = 1
    for i in range(n,0,-1):
        ret *= i
    return ret

print(Fun(5))

# 提问：求1+2!+3!+...+20!的和

#递归
def fun(n):
    if n == 1:
        return 1
    return  n*fun(n-1)

s = 0
for i in range(1,21):
    s += fun(i)

print(s)

注：用map()函数求和
# map(function, iterable, ...)
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
print(sum(map(fun,range(1,21))))

#循环
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x+1):
        r *= i
    return r

s= sum(map(op,l))
print('1! + 2! + 3! +... + 20! = %d' % s)

# 常规
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t

print(s)

# 对列表我们知道用切片来取若干元素，对生成器对象呢？

from itertools import  islice

gen = iter(range(10))  # gen是一个生成器

for i in islice(gen,0,4): # 第二个参数为起始位置，第三个参数为结束位置，无负数索引
    print(i)

 输出
 0
 1
 2
 3
 # 现在不推荐使用filter,map 因为用列表生成式也能完成
 # 三元运算符  形式为： val = 1 if 条件成立 else 2
 a = 2
 b = 5
 # 普通写法
 if a > b:
    val = True
 else:
    val = False
 # 改成三元运算符后 val = True if a > b else False
 
 # lambda map 
>>>a = [('a',1),('b',2),('c',3),('d',4)]
>>>a_1 = list(map(lambda x:x[0],a))
>>>a_1
>>>['a', 'b', 'c', 'd']

 

# 实参解包

def add(x,y):
   return x + y
t = [1,2]
print(add(*t)）  # *t

输出：3


# next用法

with open('score.txt','r',encoding='utf-8') as src:
    next(src) # 相当于del sc[0],删除文件的第一行
    sc = src.readlines()  # 列表

# while -- print -- input

while True:
    print('请选择功能：\n1:输入\n2:查找\n3:退出')  # \n在字符串里是实现换行
    c = input()  # 直接接收输入，无提示
    if c == '1':
        add_dic()
    elif c == '2':
        search_dic()
    elif c == '3':
        break
    else:
        print('输入有误')

# while try except else

写一个函数，接收用户输入的2个整数，求和
def add():
    while True:
        try:
            x = int(input('x='))
        except ValueError:
            print('输入的内容必须为整数，请重新输入！')
        else:    # else代表没走except
            break
        
    while True:
        try:
            y = int(input('y='))
        except ValueError:
            print('输入的内容必须为整数，请重新输入！')
        else:
            break

    print('x+y=',x+y)

add()

# eval() ：函数用来执行一个字符串表达式，并返回表达式的值。 简单理解就是去掉引号，返回引号内的内容
>>>x = 7
>>> eval( '3 * x' )
21
>>> eval('pow(2,2)')
4
例子：写一个函数，实现列表的切片功能，例如用户输入[1,2,3,4,5,6]和2,5,程序输出[3,4,5,6]
#参考代码
def slice():
    l = input('请输入一个列表：')
    l = eval(l)
    start,end = eval(input('pls input start position and end position:'))
    print(l[start:end+1])

slice()
输出：
E:\python3.6.5\python.exe D:/dongshiwei/power_on_sequence3.0/config/3.py
请输入一个列表：[1,2,3,4,5,6]
pls input start position and end position:2,5
[3, 4, 5, 6]

# 我的答案：
def slice():
    l = [int(i) for i in input('请输入一个列表:').split(',')]  # 得到一个整数列表
    n1,n2 = [int(i) for i in input('请输入2个整数作为起始和结束下标:').split(',')]  # 得到2个整数下标
    for i in range(len(l)):
        if  n1 <= i <= n2:
            print(l[i],end='')

slice()

# for ... else ...  :如果for 迭代到最后一个了，才会走else 从句。
目前else有三种用途：
if ... else...  : 不满足if 条件，走 else
try ... except ... else ...  : 不走except就走else ，走了except就不走else
for ... else ... :for 循环到最后了，走else# 

# 两种不同方法计算100以内所有奇数的和
x = [i for i in range(1,100) if i%2]
print(sum(x))
-------------------------------
print(sum(range(1,100)[::2])

# 获取时间并转换为易读格式 
用到的模块time中的strftime, localtime
import time
from time import strftime,localtime

print(strftime('%Y-%m-%d %H:%M:%S',localtime()))
time.sleep(1)
print(strftime('%Y-%m-%d %H:%M:%S',localtime(time.time())))

输出：
2019-07-15 11:38:36
2019-07-15 11:38:37

# 给定下面数据，用一行代码和多行代码实现预期的结果
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# expected outout:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
# {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
# {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]

# 我的答案--多行代码：
l = []
d = {}
for val in values:
    d = dict(zip(attributes,val))
    l.append(d)

print(l)

# 我的答案-- 一行代码
print([dict(zip(attributes,val)) for val in values])

思路：
1.利用zip(seq1,seq2)能将两序列对应位置凑成一对，因values是嵌套结构，所以用个for遍历

```
