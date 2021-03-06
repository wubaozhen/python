### 类和对象

### 类方法,调用类属性
class A():
    var = 100
    @classmethond
    def fun(cls)：
        print(cls.var)
A.fun()

### 实例方法：类需要实例化
class B():
  var = 'a'
  def fun(self):
      print(self.var)
b = B()
b.fun()

### 类属性和实例属性：
1.类属性更改会同步到所有实例化的对象的属性，反之实例属性的更改不会影响类属性的值和其他实例对象属性的值。
2.实例A属性如果更改在前，类属性更改在后，此时类属性已不能更改实例A的属性，但会更改实例B的属性。以下代码为例
```
class 类:
    变量 = 100 #类属性

实例1 = 类() # 实例化
实例2 = 类() # 实例化

实例1.变量 = 10  ----->理解为实例1新建了个变量与类属性同名
类.变量 = 1   -----> 更改所有实例

print(实例1.变量) -----> 命名空间，由近即远，因实例1有自己新建了个变量，所以取那个变量的值
print(实例2.变量)

输出：
10
1
```
### 类方法和实例方法

#### 重写类方法：“重写类方法”分成两个步骤：第一个步骤是在类的外部写一个函数，第二个步骤是把这个新函数的名字赋值给类.原始函数：
例子1
```
class 类():
    def 原始函数(self):
        print('我是原始函数！')

def 新函数(self):
    print('我是重写后的新函数!')

a = 类()  # 实例化
a.原始函数()

# 用新函数代替原始函数，也就是【重写类方法】
类.原始函数 = 新函数

# 现在原始函数已经被替换了
a.原始函数()

```
输出：
我是原始函数！
我是重写后的新函数!


例子2：
```
class 幸运():
    def 好运翻倍(self):
        print('好的，我把它存了起来，然后翻了888倍还给你：' + str(self.幸运数*888))

def 新好运翻倍(self):
    print('我是重写后的新函数!')
    print('好的，我把它存了起来，然后翻了666倍还给你：' + str(self.幸运数*666))

幸运.幸运数 = int(input('你的幸运数是多少？请输入一个整数。'))

幸运.好运翻倍 = 新好运翻倍
实例 = 幸运()  # 实例化
实例.好运翻倍()
```
输出：
你的幸运数是多少？请输入一个整数。1
我是重写后的新函数!
好的，我把它存了起来，然后翻了666倍还给你：666

### 总结：实例的属性和方法
1.修改类属性和类方法，将会影响所有实例
2.修改某个实例的属性，只会影响这个实例自身
3.不能修改实例的方法

### print(flush=True) 参数

例子,想实现隔1s打印一个点：
```
import time
print('Loading',end='')
for i in range(6):
    print('.',end='')
    time.sleep(1)

# 上面会一次性打印Loading.....

import time
print('Loading',end='')
for i in range(6):
    print('.',end=''，flush=True)  # 加一个flush=True即可，及时刷新，默认为false
    time.sleep(1)
```
### 模块（module）一般是一个文件，而包（package）是一个目录，一个包中可以包含很多个模块，可以说包是“模块打包”组成的。Python中的包都必须默认包含一个init.py的文件。
init.py控制着包的导入行为。假如这个文件为空，那么我们仅仅导入包的话，就什么都做不了。

### 代码结构
导入模块
定义变量
使用方法

### 循环对象
```循环对象是这样一个对象，它包含有一个next()方法(__next__()方法，在python 3x中)， 这个方法的目的是进行到下一个结果，而在结束一系列结果之后，举出StopIteration错误。

当一个循环结构（比如for）调用循环对象时，它就会每次循环的时候调用next()方法，直到StopIteration出现，for循环接收到，就知道循环已经结束，停止调用next()。

假设我们有一个test.txt的文件:

1234
abcd
efg
我们运行一下python命令行：

>>>f = open('test.txt')

>>>f.next()

>>>f.next()

...


不断输入f.next()，直到最后出现StopIteration

open()返回的实际上是一个循环对象，包含有next()方法。而该next()方法每次返回的就是新的一行的内容，到达文件结尾时举出StopIteration。这样，我们相当于手工进行了循环。

自动进行的话，就是：

for line in open('test.txt'):
    print line
在这里，for结构自动调用next()方法，将该方法的返回值赋予给line。循环知道出现StopIteration的时候结束。

 

相对于序列，用循环对象的好处在于：不用在循环还没有开始的时候，就生成好要使用的元素。所使用的元素可以在循环过程中逐次生成。这样，节省了空间，提高了效率，编程更灵活。

 

迭代器
从技术上来说，循环对象和for循环调用之间还有一个中间层，就是要将循环对象转换成迭代器(iterator)。这一转换是通过使用iter()函数实现的。但从逻辑层面上，常常可以忽略这一层，所以循环对象和迭代器常常相互指代对方。

 

生成器
生成器(generator)的主要目的是构成一个用户自定义的循环对象。

生成器的编写方法和函数定义类似，只是在return的地方改为yield。生成器中可以有多个yield。当生成器遇到一个yield时，会暂停运行生成器，返回yield后面的值。当再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield。生成器自身又构成一个循环器，每次循环使用一个yield返回的值。

 

下面是一个生成器:

复制代码
def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000
复制代码
该生成器共有三个yield， 如果用作循环器时，会进行三次循环。

for i in gen():
    print i
 

再考虑如下一个生成器:

def gen():
    for i in range(4):
        yield i
它又可以写成生成器表达式(Generator Expression):

G = (x for x in range(4))
生成器表达式是生成器的一种简便的编写方式。读者可进一步查阅。

 

表推导
表推导(list comprehension)是快速生成表的方法。它的语法简单，很有实用价值。

 

假设我们生成表L：

L = []
for x in range(10):
    L.append(x**2)
以上产生了表L，但实际上有快捷的写法，也就是表推导的方式:

L = [x**2 for x in range(10)]
这与生成器表达式类似，只不过用的是中括号。
```
### 函数对象
```
秉承着一切皆对象的理念，我们再次回头来看函数(function)。函数也是一个对象，具有属性（可以使用dir()查询）。作为对象，它还可以赋值给其它对象名，或者作为参数传递。

 

lambda函数
在展开之前，我们先提一下lambda函数。可以利用lambda函数的语法，定义函数。lambda例子如下：

func = lambda x,y: x + y
print func(3,4)
lambda生成一个函数对象。该函数参数为x,y，返回值为x+y。函数对象赋给func。func的调用与正常函数无异。

 

以上定义可以写成以下形式：

def func(x, y):
    return x + y
 

函数作为参数传递
函数可以作为一个对象，进行参数传递。函数名(比如func)即该对象。比如说:

def test(f, a, b):
    print 'test'
    print f(a, b)

test(func, 3, 5)
test函数的第一个参数f就是一个函数对象。将func传递给f，test中的f()就拥有了func()的功能。

 

我们因此可以提高程序的灵活性。可以使用上面的test函数，带入不同的函数参数。比如:

test((lambda x,y: x**2 + y), 6, 9)
 

map()函数
map()是Python的内置函数。它的第一个参数是一个函数对象。

re = map((lambda x: x+3),[1,3,5,6])
这里，map()有两个参数，一个是lambda所定义的函数对象，一个是包含有多个元素的表。map()的功能是将函数对象依次作用于表的每一个元素，每次作用的结果储存于返回的表re中。map通过读入的函数(这里是lambda函数)来操作数据（这里“数据”是表中的每一个元素，“操作”是对每个数据加3）。

在Python 3.X中，map()的返回值是一个循环对象。可以利用list()函数，将该循环对象转换成表。

 

如果作为参数的函数对象有多个参数，可使用下面的方式，向map()传递函数参数的多个参数：

re = map((lambda x,y: x+y),[1,2,3],[6,7,9])
map()将每次从两个表中分别取出一个元素，带入lambda所定义的函数。

 

filter()函数
filter函数的第一个参数也是一个函数对象。它也是将作为参数的函数对象作用于多个元素。如果函数对象返回的是True，则该次的元素被储存于返回的表中。filter通过读入的函数来筛选数据。同样，在Python 3.X中，filter返回的不是表，而是循环对象。

 

filter函数的使用如下例:

复制代码
def func(a):
    if a > 100:
        return True
    else:
        return False

print filter(func,[10,56,101,500])
复制代码
 

reduce()函数
reduce函数的第一个参数也是函数，但有一个要求，就是这个函数自身能接收两个参数。reduce可以累进地将函数作用于各个参数。如下例：

print reduce((lambda x,y: x+y),[1,2,5,7,9])
reduce的第一个参数是lambda函数，它接收两个参数x,y, 返回x+y。

reduce将表中的前两个元素(1和2)传递给lambda函数，得到3。该返回值(3)将作为lambda函数的第一个参数，而表中的下一个元素(5)作为lambda函数的第二个参数，进行下一次的对lambda函数的调用，得到8。依次调用lambda函数，每次lambda函数的第一个参数是上一次运算结果，而第二个参数为表中的下一个元素，直到表中没有剩余元素。

上面例子，相当于(((1+2)+5)+7)+9

 

根据mmufhy的提醒： reduce()函数在3.0里面不能直接用的，它被定义在了functools包里面，需要引入包，见评论区。
```
### 异常处理
流程如下，

try->异常->except->finally

try->无异常->else->finally

### python内置函数int()向下取整，ceil()向上取整。 from math import ceil

### 请使用一句代码，将 [1, 2, 3, 4, 5, 6, 7, 8, 9] 变成 [(1, 2, 3), (4, 5, 6), (7, 8, 9)]:
```
答案一： 详见https://fishc.com.cn/thread-140340-1-1.html
>>> list(zip(*[iter([1, 2, 3, 4, 5, 6, 7, 8, 9])] * 3))
[(1, 2, 3), (4, 5, 6), (7, 8, 9)]

```
```
答案二：
l = [1,2,3,4,5,6,7,8,9]
L = list(map(lambda x : tuple(l[x*3:x*3 + 3]),list(range(0,3))))
print(L)
[(1, 2, 3), (4, 5, 6), (7, 8, 9)]
```

### 编写一个 chunk() 函数，将列表分割成指定大小的块。
例如：
>>> chunk([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
[[1, 2], [3, 4], [5, 6], [7, 8], [9]]

```
答案一： 详见https://fishc.com.cn/thread-141451-1-1.html
>>> from math import ceil
>>> def chunk(lst, size):
                return list(map(lambda x: lst[x * size : x * size + size], list(range(0, ceil(len(lst) / size)))))
               
```
```
答案二：
def chunk(array,num):
    res = []

    # 确定循环次数
    lenth = len(array)/num
    if lenth > int(lenth):
        lenth = int(lenth) + 1
    else:
        lenth = int(lenth)

    for i in range(lenth):
        res.append(array[num*i:num*(i+1)])
    return res
array = [1,2,3,4,5,6,7,8,9]
num = 2
print(chunk(array,num))

```
### globals()的应用
```
data1 = '99320,ROME,MALE'
data2 = '99321,JERRY,MALE'
data3 = '99322,TIM,MALE'
MyDict = {}
for i in range(1, 4):
    MyDict['id'], MyDict['name'], MyDict['sex'] = globals()['data' + str(i)].split(',')# 如果去掉globals()，程序会报错

    print("ID:   " + MyDict['id'])
    print("Name: " + MyDict['name'])
    print("Sex:  " + MyDict['sex'])
```
打印
ID:   99320
Name: ROME
Sex:  MALE
ID:   99321
Name: JERRY
Sex:  MALE
ID:   99322
Name: TIM
Sex:  MALE

###  else 语句用法

答：在 Python 中，else 语句不仅能跟 if 语句搭，构成“要么怎样，要么不怎样”的语境；Ta 还能跟循环语句（for 语句或者 while 语句），构成“干完了能怎样，干不完就别想怎样”的语境；其实 else 语句还能够跟我们刚刚讲的异常处理进行搭配，构成“没有问题，那就干吧”的语境。

### with 处理多个项目的时候
with 语句处理多个项目的时候，可以用逗号隔开写成一条语句
```
with A() as a, B() as b:
    suite
```

