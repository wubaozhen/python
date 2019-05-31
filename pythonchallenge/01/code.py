

### 给定一个字符串，将每个字母往后移两个，组成一个新的字符串
例如K--> M ;O --> Q;E --> G

# 原始字符串
text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
 bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
 lmu ynnjw ml rfc spj.'''
 
#定义一个新的变量存改变后的字符串
text_translate = ''

#遍历每一个字符，判断是不是字母，如果是就用ord()换成十进制做运算，再chr()返回到字符
for i in text:
    if i.isalpha():
        n = ord(i)
        if i >= 'y':  # 这里以y为界限是因为最后2个字母是y和z,他们往后移两位就到开头了
            n = ord(i) + 2 - 26
        else:
            n = ord(i) + 2
        text_translate += chr(n)


    else:
        text_translate += i

print(text_translate)

备注：
>>>ord('a')
97
>>>ord('b')
98
>>>chr(100)
'd'



