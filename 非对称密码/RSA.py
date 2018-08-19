from miller_rabin import *
from Bezout import *

def arguments():
    p=big_prime()
    q=big_prime()
    n=p*q
    nn=(p-1)*(q-1)
    e=random.randint(2**1000,2**1024)
    tup=Bezout(e,nn)
    while tup[1]!=1:
        e=random.randint(2**1000,2**1024)
        tup=Bezout(e,nn)
    d=tup[0]
    return(e,d,n)
(e,d,n)=arguments()

#test
print(pow(pow(125,e,n),d,n))
