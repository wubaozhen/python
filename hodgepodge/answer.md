#### 七位不重复的数字
```
# 定义最小的不重复的7位数
i = 1023456

def isDiff(i):
    '''
    判断一个7位数i是否每个数字不重复
    :param i:  i 为7位数
    :return:  return 布尔值
    '''
    si = str(i)
    if len(set((list(si)))) == 7:
        return True
    return False

def isSeven(i2,i3,i6):
    '''
    传3个数字，判断3个数字均为7位数
    :param i2: 
    :param i3: 
    :param i6: 
    :return:  return 布尔值
    '''
    if len(str(i2)) == len(str(i3)) == len(str(i6)) == 7:
        return True
    return  False

# 9876543为7位不重复的数中最大值
while i < 9876543:
    if isDiff(i):
        i2 = i * 2
        i3 = i * 3
        i6 = i * 6
        if isSeven(i2,i3,i6) and isDiff(i2) and isDiff(i3) and isDiff(i6):
            print(i)
    i += 1
    
    ####################################################
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

## 参考答案：
def output_avg(L):
    sum1,sum2 = 0,0
    for line in L:
        L1 = line.strip().split()  # strip()清除字符串头尾指定的字符（默认为空格或换行符）
        sum1 += int(L1[1])
        sum2 += int(L1[2])
    count = len(L)
    avg1 = round(sum1/count,1)  # round()指定小数位数
    avg2 = round(sum2/count,1)
    print('这个班的数学平均分为:%.1f,语文平均分为：%.1f' % (avg1,avg2))

def output_notpass(L):
    print('两门课均不及格的学生学号及数学、语文成绩为：')
    for line in L:
        L1 = line.strip().split()
        if int(L1[1]) < 60 and int(L1[2]) < 60:
            print(line,end='')

def output_good(L):
    print('两门课平均分在90分以上的学生学号及数学、语文成绩为：')
    for line in L:
        L1 = line.strip().split()
        f_score = round((int(L1[1])+int(L1[2]))/2)
        if f_score >= 90:
            print(line,end='')

with open("class_score.txt") as f:
    L = f.readlines()
    del L[0]  # 删除标题行

output_avg(L)
output_notpass(L)
output_good(L)
    
注：
1.写程序前先想好代码执行后长什么样子
2.借鉴参考答案，只执行一次打开文件，传参

# 3. 当前目录下有一个文件名为score.txt的文本文件，存放着计算机课成绩。共有学号、总评成绩两列，请查找最高分和最低分的学生，并在屏幕上显示其学号和成绩

# 我的答案：
def res(L):
    temp_L = []
    for line in L:
        temp = int(line.strip().split()[1])  # 获取分数
        temp_L.append(temp)  # 把分数存到列表

    max_res = max(temp_L)
    min_res = min(temp_L)

    for line in L:
        if str(max_res) in line:
            print('最高分的学号和成绩为：',line)
            break
    for line in L:
        if str(min_res) in line:
            print('最低分的学号和成绩为：',line)
            break

with open('score.txt','r') as f:
    L = f.readlines()
    del L[0]  # 删掉标题

res(L)

# 参考答案：
with open('score.txt','r',encoding='utf-8') as src:
    next(src)   # 这行代码的意思相当于去掉了标题行，src是个可迭代对象，有__next__()方法
    sc = src.readlines()
def max_min(sc):
        num1 = ''
        num2 = ''
        max = 0
        min = 100
        for line in sc:
            ll = line.strip().split()
            if int(ll[1]) >= max:
                max = int(ll[1])
                num1 = ll[0]
            if int(ll[1]) <= min:
                min = int(ll[1])
                num2 = ll[0]
        print(num1,max)
        print(num2,min)

 max_min(sc)
 
# 记录新学的英文单词和其中文翻译，所有设计一个添加单词函数，一个查找单词函数
d = {}
def add_dic():
    while True:
        print('按回车则退出添加！')
        word = input('今天新学的单词为：')
        if len(word) == 0:   # 即直接按回车
            break
        d[word] = input('其中文意思为：')
        print('该单词已添加到字典库')

def search_dic():
    while True:
        print('按回车则退出查找！')
        word = input('今天新学的单词为：')
        if len(word) == 0:
            break
        if word in d:
            print('这个单词已存在')
            print('%s的中文意思为:%s' % (word,d[word]))
        else:
            print('这是个新单词，将加入到字典库中')
            d[word] = input('其中文意思为：')

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
        
   



  ```
