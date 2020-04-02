import fileinput



'''def duqu(a,b,c,d=''):
    fname = '机器人班费收支情况.xlsx'
    js1 = int(0)
    js2 = int(0)
    jl = ''
    jl2 = ''
    flag = int(0)
    f=open('机器人班费收支情况.xlsx','a+')
    for i in f:
        print(i)
        for n in i:
            if a == 1:
                if flag == 1:
                    jl2 += n
                if n == '/t':
                    js1+=1
                else :
                    jl += n
                if js1 == 3:
                    if jl :
                        break
                    else :
                        flag = 1
        e=f.tell()
        print(e)
        if flag == 1:
            f.writelines(b+'/t'+c+'/t'+d+n)
            f.close()
if __name__=='__main__':
    duqu(1,2,3,0)'''
flag = 0
n=0
with open('机器人班费收支情况.csv','r+') as f:
    for i in f :
        n+=1
        if n == 1 :
            f.writelines('wdnmd')
        print(i)
    f.close()
