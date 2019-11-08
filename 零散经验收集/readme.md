# 闭包的结构：
1.有嵌套函数，且嵌套函数用到外部函数的参数
2.外部函数的返回值为嵌套函数名
3.调用的形式为funx(x)(y)


```def funx(x):
    def funy(y):
        return x*y
    return funy


f = funx(2)(3)
print(f)
```

# while condition  ---> input  if  else 结构，用于一直循环，输入什么时候退出的场景

```
q = True
while q:
    num = input("请输入数字(输入Q退出)： ")
    if num != Q:
        
    else:
        q = False
```

# 求两数最大公约数

1.欧几里得算法
  1.1. a余b,得余数c,再用b去余c,的余数d,依此循环，直到余数为0，最大公约数即被余数
  1.2. 逻辑转换成代码即如下，输出都为2

def gcd(x,y):

   while y:
       z = x%y   # 取余数
       x = y
       y = z
   return x

print(gcd(4, 6))
print(gcd(6, 4))

# 问题：为何x<y 也能正常运行？以上面个例子来说：
x=4,y=6,z=4%6即4
再执行x=y,即x=6
再执行y=z,即y=4
此时就跟gcd(6,4)一样了。
