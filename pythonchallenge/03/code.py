http://www.pythonchallenge.com/pc/def/equality.html

    
#### 一个小写字母左右两边均有3个大小字母
#### 知识点：获取网页源代码；正则表达式

import requests
import re
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
res = requests.get(url).text
#找出以<!--开头以-->结尾并打印，text打印后是一个列表，只包含一个长字符串元素
text = re.findall('.*?<!--(.*)-->',res,re.S)
#把列表转换为字符串，便于遍历字符，并去掉换行符
text = ''.join(text).replace('\n','')
#找到符合条件的小写字母
patt = re.compile(r'[a-z]+[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]+')
ret = patt.findall(text)
print(ret)

备注：
to line12:最后的参数re.S 必须要，re.S的意思是正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。
    如果去掉了re.S,那么匹配到的是个[]
