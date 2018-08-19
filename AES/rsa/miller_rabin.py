# -*- coding: utf8 -*-
#生成大质数，素数检测。
import random
import time
def isPrimenum(n=29):
    i=1;j=0
    m=n-1
    while m&i==0:
        i<<=1
    k=i.bit_length()-1
    q=m>>k
    for i in range(11,21):
        if pow(i,q,n)==1:   continue
        for j in range(0,k):
            if pow(i,(2**j)*q,n)==m:
                break
            j+=1
        if j==k:
            return False
    return True
    
def big_prime():
    m=time.time()
    a=2**1024
    b=2**1000
    x=random.randint(b,a)
    while x&1==0:
        x=random.randint(b,a)
    while not isPrimenum(x):
        x=random.randint(b,a)
        while x&1==0:
            x=random.randint(b,a)
    print('耗时：',time.time()-m,'秒\n')
    return x


