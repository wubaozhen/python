# 写一个函数，传入一个参数n,返回n的阶乘
```
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
```
# 对列表我们知道用切片来取若干元素，对生成器对象呢？
```
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

 
 ```
