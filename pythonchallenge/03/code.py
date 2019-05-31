#### 从一大串字符里找到出现次数最少的几个字符
### 知识点：正则表达式提取字符串；list计数；条件语句

import requests
import re
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
res = requests.get(url).text
#找出以<!--开头以-->结尾并打印，text打印后是一个列表，包含一个长字符串的元素
text = re.findall('.*?<!--.*-->.*<!--(.*)-->',res,re.S)
#把列表转换为字符串，便于遍历字符
text = str(text) # 也可以写成 str = ''.join(text)
#统计每个字符出现的个数
lst = [] # 用于存放无重复的
for i in text:
    if i not in lst:
        l.append(i)
for items in lst:
    print(f'{items} 出现了 {text.count(items)} 次' )
    
