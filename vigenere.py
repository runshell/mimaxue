print("""此代码没有主函数，使用时请自行调用加解密函数
加密：E(mingwen="family",key="good")\n解密：D(miwen="",key="good")""")
ss=""
for i in range(26):
    ss+=chr(ord('A')+i)

#实现将字符串改为大写并删去非字母字符处理的函数
def deal(dd=""):
    temp=""
    for c in dd:
        if c.upper() in ss:
            temp+=c.upper()
    return temp

#加密函数
def E(mingwen="family",key="good"):
    i=0
    miwen=""
    key=deal(key)
    mingwen=deal(mingwen)
    LEN=len(key)
    for c in mingwen:
        miwen+=chr((ord(c)+ord(key[i%LEN]))%26+ord("A"))
        i+=1
    return miwen

#解密函数
def D(miwen="family",key="good"):
    i=0
    mingwen=""
    key=deal(key)
    miwen=deal(miwen)
    LEN=len(key)
    for c in miwen:
        mingwen+=chr((ord(c)-ord(key[i%LEN]))%26+ord("A"))
        i+=1
    return mingwen
