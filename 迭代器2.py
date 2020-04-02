class ddq:
    def __init__(self,a=0):
        self.mul=a

DDQ=ddq()

def used():
    DDQ.mul += 3
    return DDQ.mul

for i in iter(used,9):
    print('迭代器数值为：',i,sep='')
