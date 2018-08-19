print("""此代码没有主函数，使用时请自行调用加解密函数
加密：E(mingwen="family",key="family")\n解密：D(miwen="",key="family")""")
ss=""
for i in range(26):                                 #产生26个大写字母
    ss+=chr(ord('A')+i)

#预处理明/密文
def pre_wen(wen=''):
    temp=''
    for c in wen:
        if c.upper() in ss:                         #除去非字母字符并转换为大写
            temp+=c.upper()
            
    temp=temp.replace("J","I")                #用I代替J
    wen=""                                           #清空字符串
    i=0
    LEN=len(temp)
    
    while i <LEN:                                   #两个字母相同则插入Z
        if temp[i:i+1]==temp[i+1:i+2]:
            wen+=temp[i:i+1]+'Z'
            i+=1
        else:
            wen+=temp[i:i+1]+temp[i+1:i+2]
            i+=2
    if len(wen)%2!=0:                               #若字符串长度为奇数就在最后添加字母“Z”
        wen+='Z'
    return wen

#预处理密钥
def pre_key(key=''):
    temp=''
    for c in key:                                    #除去非字母字符并转换为大写
        if c.upper() in ss and c.upper() not in temp:
            temp+=c.upper()
    for c in ss:                                      #产生包含J在内的26个字母的完整密钥
        if c not in temp:
            temp+=c
    key=temp.replace("J","")                    #除去“J”
    return key


#加密处理
def E(mingwen="family",key="family"):   #为形参设默认值为family
    miwen=""
    mingwen=pre_wen(mingwen)
    key=pre_key(key)
    i=0
    while i<len(mingwen)-1:    
        xuhao1=key.index(mingwen[i])
        hang1=xuhao1//5
        lie1=xuhao1%5
        xuhao2=key.index(mingwen[i+1])
        hang2=xuhao2//5
        lie2=xuhao2%5
        if lie1==lie2:                              #同列
            miwen+=key[hang1*5+(lie1+1)%5]+key[hang2*5+(lie2+1)%5]
        elif hang1==hang2:                    #同行
            miwen+=key[((hang1+1)%5)*5+lie1]+key[((hang2+1)%5)*5+lie2]
        else:                                         #不同行不同列
            miwen+= key[hang1*5+lie2]+key[hang2*5+lie1]
        i+=2
    print("key=",key)
    print("明文：\n",mingwen)
    print("密文：")
    return(miwen)

#解密处理
def D(miwen="",key="family"):
    miwen=pre_wen(miwen)
    key=pre_key(key)
    mingwen=""
    for i in range(0,len(miwen)-1,2):
        xuhao1=key.index(miwen[i])
        hang1=xuhao1//5
        lie1=xuhao1%5
        xuhao2=key.index(miwen[i+1])
        hang2=xuhao2//5
        lie2=xuhao2%5
        if lie1==lie2:
            mingwen+=key[hang1*5+(lie1-1)%5]+key[hang2*5+(lie2-1)%5]
        elif hang1==hang2:
            mingwen+=key[((hang1-1)%5)*5+lie1]+key[((hang2-1)%5)*5+lie2]
        else:
            mingwen+= key[hang1*5+lie2]+key[hang2*5+lie1]
    print("key=",key)
    print("密文：\n",miwen)
    print("明文：")
    return(mingwen)
