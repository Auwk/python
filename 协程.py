def lf():
    print('dnmd任务呢')
    while(1):
        pz = (yield)
        print('收到任务：',pz,sep='')

def xc():
    c = lf()
    c.__next__()
    for i in range(3):
        print('发送任务',i,sep='')
        c.send(i)

xc()
