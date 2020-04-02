import datetime

def file_hdl(a,b,name='石头数量.txt'):
    with open(name,'a',encoding='utf-8') as f :
        a=int(a)
        b=int(b)
        c=str(datetime.datetime.now())
        f.write('\n')
        f.writelines('%s,仓库石头数为：%d,总石头数为:%d,记录点为:\'%s\',还差%d个石头'%(c,a,b,d,168*3-b))
        f.write('\n')
def du(name='石头数量.txt'):
        with open(name,encoding='utf-8') as w :
            for i in w:                 
                print(i,end='')
        '''a=f.read()
        print(a)'''
a=input('输入邮件石头数：')
b=input('输入总石头数：')
d=input('输入时间点：')
file_hdl(a,b)
du()
input()
