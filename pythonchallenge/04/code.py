#### 一个URL，改nothing后面的值而跳转到一个新的URL
#### 知识点：正则加爬虫

import os
#首页URL
resp = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345').text
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
#计数器
count = 0
while True:
    try:
        # 提取下一页动态数值
        nextid = re.search('\d+',resp).group()
        count += 1
        nextid = int(nextid)
    except:
        print('最后一个URL为：%s' % nexturl)
        break
    #获取下一页URL
    nexturl = url + str(nextid)
    print('url %s:%s' % (count,nexturl))
    #重复请求
    resp = requests.get(nexturl).text
    
    备注：
    to line 13： \d+ 表示至少匹配一个数字，group()返回re匹配到的字符串
    re.search()一旦匹配成功，就会返回一个search对象，此对象就有group方法。详见：
    https://www.cnblogs.com/tina-python/p/5508402.html
