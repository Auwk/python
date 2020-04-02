import datetime
time=datetime.datetime.now()
class person:
    '''def __init__(self):
        self.name=''
        self.brithday=''
        self.height=''
        self.weight='''
        
    def sx(self):
        self.name=input('input your name:')
        self.brithday=int(input('imput your brithday:'))
        self.height=int(input('input your height:'))
        self.weight=int(input('input your weight'))
    def xs(self):
        print('岁数为：%d'%(time.year-self.brithday))
        if self.weight > self.height-140+20 and self.weight < self.height-110+20 :
            print('体重合格')
        else:
            print('体重不合格')

a=person()
a.sx()
a.xs()
