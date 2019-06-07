http://www.pythonchallenge.com/pc/def/peak.html
知识点：爬虫;字符串转字节；pickle.load()解析成python数据结构

import requests
import pickle
res = requests.get('http://www.pythonchallenge.com/pc/def/banner.p').text
# 将字符串转换为字节类型
res_b = str.encode(res)
# 把网页内容存到本地banner.p文件中
with open('banner.p','wb') as f:
    f.write(res_b)

# 用pickle解析成python内置数据结构
pkl_file = open('banner.p','rb')
data = pickle.load(pkl_file)
print(data)

print('\n'.join([''.join([p[0] * p[1] for p in row]) for row in data]))
#一行代码可拆解成如下：
for row in data:
    for p in row:
        s = p[0] *p[1]
        print(s,end='')
    print()
   
输出:
channel
