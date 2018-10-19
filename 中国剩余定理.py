#作者：xbillow

#扩展欧几里德除法，返回逆元和最大公约数，
#当且仅当最大公约数为1时，返回的逆元有意义。
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

#本函数根根据**中国剩余定理之递归证明**编写
def crt():
    print("逐个输入同余式方程：x≡b(mod m)当输入m为0时结束输入！")
    b1=int(input("请输入b:\t"))                #输入第一个同余式方程
    m1=int(input("请输入m:\t"))
    while True:
        b2=int(input("请输入b:\t"))            #输入第二个同余式方程
        m2=int(input("请输入m:\t"))
        if(m2==0): break                       #终止条件：若模数为0，就跳出循环       
        (inv,gcd)=Bezout(m1,m2)                #inv存放逆元，gcd存放最大公约数
        if gcd!=1:                             #若最大公约数不为1，本次输入无意义，提示重新输入
            print("模数不互质，本次输入无效！")
            continue                           #结束本次循环
        b1=(((inv*(b2-b1))%m2)*m1+b1)%(m2*m1)  #求得两个同余式方程的公共解更新余数
        m1=m2*m1                               #更新模数
        #用当前结果与下一轮输入的同余式组进行求解，使得永远在做两个同余式方程构成的方程组的解
    return(b1,m1)                              #返回余数和模数

print("计算同余式组请调用无参函数crt()。")
