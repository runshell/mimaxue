from AES import AES

def main(e=[0x0189fe76,0x23abdc54,0x45cdba32,0x67ef9810],key=[0x0f470caf,0x15d9b77f,0x71e8ad67,0xc959d698],state='D'):
    """参数依次为明/密文(4个32bit数组成的列表)，密钥(4个32bit数组成的列表)，状态('E' or 'D')"""
    aes=AES()
    e=[0xff086964,0xb533414,0x84bfab8f,0x4a7c43b9]

    key=aes.keyall(key[:])
    if state=='D':
        i=10
    elif state=='E':
        i=0
    else:
        print('参数错误！')
        return
    print('=======最美如初见（初始状态）=======')
    print(hex(e[0])+'\n'+hex(e[1])+'\n'+hex(e[2])+'\n'+hex(e[3])+'密/明文\n')
    print(hex(key[i][0])+'\n'+hex(key[i][1])+'\n'+hex(key[i][2])+'\n'+hex(key[i][3])+'初始密钥\n\n=======第{}轮======='.format(i))
    e=aes.addRoundKey(e,key[i],'E')
    print(hex(e[0])+'\n'+hex(e[1])+'\n'+hex(e[2])+'\n'+hex(e[3])+'轮开始\n')
    
    for i in range(9):
        if state=='D':
            i=9-i
        elif state=='E':
            i=i+1
        e=aes.substitute_bytes(e,state)
        print(hex(e[0])+'\n'+hex(e[1])+'\n'+hex(e[2])+'\n'+hex(e[3])+'字节代替\n')
        e=aes.shiftrows(e,state)
        print(hex(e[0])+'\n'+hex(e[1])+'\n'+hex(e[2])+'\n'+hex(e[3])+'行移位\n')
        e=aes.mixColumns(e,state)
        print(hex(e[0])+'\n'+hex(e[1])+'\n'+hex(e[2])+'\n'+hex(e[3])+'列混淆\n')
        print(hex(key[i][0])+'\n'+hex(key[i][1])+'\n'+hex(key[i][2])+'\n'+hex(key[i][3])+'轮密钥\n\n=======第{}轮======='.format(i))
        e=aes.addRoundKey(e,key[i],state)
        print(hex(e[0])+'\n'+hex(e[1])+'\n'+hex(e[2])+'\n'+hex(e[3])+'轮开始\n')
    if state=='D':
        i=0
    elif state=='E':
        i=10   
    e=aes.substitute_bytes(e,state)
    print(hex(e[0])+'\n'+hex(e[1])+'\n'+hex(e[2])+'\n'+hex(e[3])+'字节代替\n')
    e=aes.shiftrows(e,state)
    print(hex(e[0])+'\n'+hex(e[1])+'\n'+hex(e[2])+'\n'+hex(e[3])+'行移位\n')
    print(hex(key[i][0])+'\n'+hex(key[i][1])+'\n'+hex(key[i][2])+'\n'+hex(key[i][3])+'轮密钥\n\n=======明/密文=======')
    e=aes.addRoundKey(e,key[i],'E')
    print(hex(e[0])+'\n'+hex(e[1])+'\n'+hex(e[2])+'\n'+hex(e[3])+'密文\n')

if __name__=='__main__':
    print('示例展示')
    main()
