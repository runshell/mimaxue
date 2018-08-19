#auther:xbillow

#求多项式的余数和商
def div_pol(a=127,b=23):
    q=0                                 #初始化商
    if b==0: return(0,float('inf'))     #若除数为零，返回商为正无穷，余数为零
    if len(bin(a))==len(bin(b)):        #长度相同再执行一遍且只执行一遍
        temp=len(bin(a))-len(bin(b))
        q=q^(1<<temp)
        a=a^(b<<temp)
    while a>b:                         #当被除多项式小于除多项式时得到余数，终止循环
        temp=len(bin(a))-len(bin(b))    #单步商单项式
        q=q^(1<<temp)                   #累计商多项式
        a=a^(b<<temp)                   #更新被除多项

    return(a,q)                         #返回余数和商多项式

#多项式乘法
def mul_pol(a=127,b=23):
    sum=0                               #初始化变量，用于存放乘积多项式
    temp=list(bin(a))                   #将其中一个多项式转化成二进制串并转化成列表
    temp.reverse()                      #颠倒列表顺序
    for i in range(len(temp)-2):        #遍历除'0b'以外元素
        if(temp[i]=='1'):               #若该指数的项的系数为1
            sum=sum^b<<i                #用该项与另一多项式相乘并与sum相加
    return sum

#求逆元，返回逆元和最大公因式
#当且仅当最大公约式为1时，返回的逆元有意义。
def inv(a=11,b=23):
    s1=1;s2=0
    t1=0;t2=1
    r1=a;r2=b
    q=div_pol(r1,r2)[1]                 #q为多项式得我不完全商多项式
    temp=r2;r2=div_pol(r1,r2)[0];r1=temp#r为多项式的余多项式
    while r2!=0:                        #余多项式不为0
        temp=s2;s2=mul_pol(q,s2)^s1;s1=temp#求s
        temp=t2;t2=mul_pol(q,t2)^t1;t1=temp#求t
        q=div_pol(r1,r2)[1]             #更新q
        temp=r2;r2=div_pol(r1,r2)[0];r1=temp#更新r
    return(div_pol(s2,b)[0],div_pol(mul_pol(s2,a)^mul_pol(t2,b),b)[0])#返回逆元和最大公因式

print("""\t\t\t此代码包含三个函数：
返回多项式的余数和商:div_pol(a=127,b=23)
返回多项式乘积:\t     mul_pol(a=127,b=23)
返回逆元和最大公因式:inv(a=11,b=23)""")
