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
    
  ```
