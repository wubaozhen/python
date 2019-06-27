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
    # 文件，有三列，分别为学号，数学成绩，语文成绩

def average_score():
    '''
    求数学和语文平均分，保留一位小数输出
    :return:
    '''
    math_list = []
    chinese_list = []
    with open('class_score.txt') as f:
        for line in f.readlines():
            temp1 = line.split()[1]
            temp2 = line.split()[2]
            math_list.append(int(temp1))
            chinese_list.append(int(temp2))
    math_score = sum(math_list)/len(math_list)
    chinese_score = sum(chinese_list)/len(chinese_list)
    print('数学平均分为：%.1f' % math_score)  # %.1f 表示取小数点后1位
    print('语文平均分为：%.1f' % chinese_score)

def donot_pass():
    '''
    找出2门课都不及格的学生，输出他们的学号和各科成绩
    :return:
    '''
    with open('class_score.txt') as f:
        L_all = []
        for line in f.readlines():
            L_temp = []
            temp1 = line.split()[1]
            temp2 = line.split()[2]
            if int(temp1) < 60 and int(temp2) < 60:
                L_temp.append(int(line.split()[0]))
                L_temp.append(int(line.split()[1]))
                L_temp.append(int(line.split()[2]))
                L_all.append(L_temp)
        print('2门课都不及格的学生：',L_all)

def score_90():
    '''
    找出两门课的平均分在90分以上的学生，输出他们的学号和各科成绩
    :return:
    '''
    with open('class_score.txt') as f:
        L_all = []
        for line in f.readlines():
            L_temp = []
            temp1 = line.split()[1]
            temp2 = line.split()[2]
            if (int(temp1)+int(temp2))/2 > 90:
                L_temp.append(int(line.split()[0]))
                L_temp.append(int(line.split()[1]))
                L_temp.append(int(line.split()[2]))
                L_all.append(L_temp)
        print('2门课平均分在90分以上的学生：',L_all)


if __name__ == '__main__':
    average_score()
    donot_pass()
    score_90()

```
