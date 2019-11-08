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
