import datetime
import time

def cache(s,curr_time = datetime.datetime.now()):
    def _cache(fn):
        def wrap(a,b):
            ret = fn(a,b)
            time = datetime.datetime.now()
            # a = (time - curr_time).total_seconds()
            # print(a)
            if  (time - curr_time).total_seconds() < s:
                return ret
            else:
                return fn(a,b)
        return wrap
    return _cache

@cache(60)
def add(a,b):
    time.sleep(2)
    return a+b

#print(add(2,2))
print(add(4,1))

#时间没弄好
