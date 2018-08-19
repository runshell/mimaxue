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