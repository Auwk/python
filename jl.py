class jl:
    weight = 100
    color = 'blue'
    height = 160
    power = 100
    zb ={'x':0,'y':0}
    
    def sd(self):
        jl.weight = input('input weight:')
        jl.color = input('input color:')
        jl.height = input('input height:')

    def ztxs(self):
        print('weight:%d color:%s height:%d power:%d 坐标:(%d,%d) '%(jl.weight,jl.color,jl.height,jl.power,jl.zb['x'],jl.zb['y']))

    def xz(self,x):
        a = jl.zb['x']
        jl.zb['x'] = a+x*2
        jl.power -= x*5
        print('in (%d,%d),power is %d'%(jl.zb['x'],jl.zb['y'],jl.power))

    def tg(self):
        a=int(jl.zb['x'])
        b=int(jl.zb['y'])
        jl.zb['x'] = a+2
        jl.zb['y'] = b+2
        print('他跳起来啦,最高点为(%d,%d)')
        a=int(jl.zb['x'])
        b=int(jl.zb['y'])
        jl.zb['x'] =a+2
        jl.zb['y'] =b-2
        jl.power -= 10
        print('他下来啦吗，他在(%d,%d),还有%d能量'%(jl.zb['x'],jl.zb['y'],jl.power))

SBYH = jl()
A = '0'
while A != 5:
    A = input('修改信息输入1，状态显示输入2，行走输入3，跳跃输入4，退出输入5\n')
    if A == '1' :
        SBYH.sd()
    elif A == '2' :
        SBYH.ztxs()
    elif A == '3' :
        x=int(input('要走：'))
        SBYH.xz(x)
    elif A == '4' :
        SBYH.tg()
    
        
    
            
