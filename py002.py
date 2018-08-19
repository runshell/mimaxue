
kk="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""#明文
k1=7
k2=19

ee=""#密文
ss=""#A到Z的列表
for i in range(26):
    ss+=chr(ord('A')+i)
for c in kk:
    if c.upper() in ss:
        if c in ss:
            c=chr((ord(c)*k1+k2)%26+ord('A'))
        else:
            c=chr((ord(c)*k1+k2)%26+ord('a'))
    ee+=c
print ("k1={}   k2={}".format(k1,k2))
print ("################################")
print(ee)#输出密文
