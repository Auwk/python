import os
import fileinput
d=0                                     #d为d列表的序号
o=[]
p=[]
    
def read(f):
    a=0                                     #a为检测空格的变量
    b=''                                   #b为收集姓名的变量
    c=0                                     #c为b列表的序号
    y=''
    t=0
    for g in f:
        t+=1
    for i in range(0,100,1):
        if i <t:
            if f[i]==' ':
                a+=1
            if a==1 and f[i+1] != ' ':
                b+=f[i+1]
            if a==2 and f[i+1] != ' ':
                y+=f[i+1]
    return b,y
            



if __name__=='__main__':
    u=os.listdir('pho')
    for z in u:
        m=z[:-4]
        with fileinput.input('me.txt') as f:
            for x in f:
                o,p=read(x)
                if p==m:
                    n='pho' +'\\'+ z
                    os.rename(n,'pho' +'\\'+o+'.'+'jpg')
    input()
                    
            

            
