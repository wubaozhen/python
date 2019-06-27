```
import datetime


def cache(s,curr_time = datetime.datetime.now()):
    def _cache(fn):
        def wrap(a,b):
            with open('result.txt','r+') as fr:
                content = fr.read()
            if not content:
                ret = fn(a,b)
                with open('result.txt', 'w+') as fr:
                    fr.write(str(ret))
                time = datetime.datetime.now().strftime( '%Y-%m-%d %H:%M:%S')
                with open('time.txt', 'w+') as ft:
                    ft.write(time)
                return ret
            else:
                with open('time.txt', 'r+') as ft:
                    content_time = ft.read()

                delta = curr_time - datetime.datetime.strptime(content_time,'%Y-%m-%d %H:%M:%S')
                delta_s = delta.seconds

                if delta_s < s:
                    with open('result.txt', 'r+') as fr:
                        content = fr.read()
                        return content
                else:
                    ret = fn(a,b)
                    with open('result.txt', 'w+') as fr:
                        fr.write(str(ret))
                    return ret
        return wrap
    return _cache

@cache(3)
def add(a,b):
    return a+b


print(add(4,7))
```



```
import functools

fun_List = []

def register(fn):
    global  fun_List
    fun_List.append(fn)
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        ret = fn(*args,**kwargs)
        return ret
    return wrapper

@register
def add(x,y):
    return int(x) + int(y)

@register
def test(x):
    return x

while True:
    fun_name = input('>>输入指令：')
    result = 'default'
    for fn in fun_List:
        if fun_name == fn.__name__:
            args = input('>>输入参数：')
            args_list = args.split(',')
            result = fn(*args_list)
            break

    print('>>结果',result)
    
    ############################################
    # 







```
