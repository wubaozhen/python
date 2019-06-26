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

#普通：
def Fun(n):
    ret = 1
    for i in range(n,0,-1):
        ret *= i
    return ret

print(Fun(5))
```
