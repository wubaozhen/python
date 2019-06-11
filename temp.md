import datetime
import time

def cache(s,curr_time = datetime.datetime.now(),times=1):
    def _cache(fn):
        def wrap(a,b):
            if times == 1:
                ret = fn(a,b)
                times += 1
                start_time = datetime.datetime.now()
            else:
                if (curr_time - start_time).total_seconds() < s:
                    return ret
                else:
                    ret = fn(a,b)
                    start_time = datetime.datetime.now()
                    return ret

        return wrap
    return _cache

@cache(60)
def add(a,b):
    time.sleep(2)
    return a+b

#print(add(2,2))
print(add(4,1))



#时间没弄好

第一次需要执行fn(a,b),第二次的时候就要判断时间，可执行（返回新结果）可不执行（返回上一次结果）
