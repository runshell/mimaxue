import struct
from AES import AES
class WorkMode(AES):
    def ECB(self,path='IMG_20160506_174717.jpg.aes',state=''):
        key=super().keyall([0x0f470caf,0x15d9b77f,0x71e8ad67,0xc959d698])
        f=open(path,'rb')
        path+='.aes'#待优化
        g=open(path,'wb')
        temp=f.read(16)
        i=0;j=1
        while len(temp)==16:
            i+=1
            temp=list(struct.unpack('IIII',temp))
            temp=super().AES_D(temp,key)
            g.write(struct.pack('IIII',temp[0],temp[1],temp[2],temp[3]))
            temp=f.read(16)
            if i==6400:
                print(j)
                j+=1
                i=0
        g.write(temp)
        g.close()
        


        
a=WorkMode()

print(a.ECB())
