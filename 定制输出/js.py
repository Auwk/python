
def js(a):
    print('平方为：%d'%(a*a))
    if a>=0 :
        print('绝对值为%d'%a)
    else :
        print('绝对值为%d'%(a*(-1)))
def ss(a):
    for i in range(2,a-1,1):
        if a%i == 0 :
            print('该数不是素数')
            return 0
    print('该数是素数')
        
def qd():
    a=int(input('请输入数值：'))
    return a

            

