#作者：xbillow

#求最大公约数
def gcd(a=1,b=2):
    if b==0:
        return a
    else:
        return(gcd(b,a%b))

#贝祖算法求逆元
def Bezout(a=1,b=2):
    s1=1;s2=0
    t1=0;t2=1
    r1=a;r2=b
    q=r1//r2
    temp=r2;r2=-q*r2+r1;r1=temp
    while r2!=0:
        temp=s2;s2=-q*s2+s1;s1=temp
        temp=t2;t2=-q*t2+t1;t1=temp
        q=r1//r2
        temp=r2;r2=-q*r2+r1;r1=temp
    return(s2%b,s2*a+t2*b)

print("""此代码无主函数，请自行调用函数：
求最大公约数函数：gcd(a=1,b=2)
求sa+tb=(a,b)中的s和t的函数：Bezout(a=1,b=2) 函数返回元祖（逆元,最大公约数）""")
