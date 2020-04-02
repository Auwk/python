import datetime

def file_hdl(a,b,name='jianhui.txt'):
    with open(name,'a',encoding='utf-8') as f :
        a=int(a)
        b=int(b)
        c=str(datetime.datetime.now())
        f.write('\n')
        f.writelines('%s,胸围为:%d,腰围为:%d'%(c,a,b))
        f.write('\n')
def du(name='jianhui.txt'):
        with open(name,encoding='utf-8') as w :
            for i in w:                 
                print(i,end='')
        '''a=f.read()
        print(a)'''
a=input('输入腰围：')
b=input('输入胸围：')
file_hdl(a,b)
du()
input()
